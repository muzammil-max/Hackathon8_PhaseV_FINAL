import { authClient } from '@/lib/auth-client';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface FetchOptions extends RequestInit {
  token?: string;
}

export async function fetchClient<T>(endpoint: string, options: FetchOptions = {}): Promise<T> {
  const { token, ...init } = options;
  const headers = new Headers(init.headers);

  headers.set('Content-Type', 'application/json');
  
  if (token) {
    headers.set('Authorization', `Bearer ${token}`);
  } else if (typeof window !== 'undefined') {
      try {
        const session = await authClient.getSession();
        if (session.data?.session.token) {
          headers.set('Authorization', `Bearer ${session.data.session.token}`);
        }
      } catch (e) {
        // Silently fail if session cannot be retrieved, backend will return 401 if needed
      }
  }

  const response = await fetch(`${API_URL}${endpoint}`, {
    ...init,
    headers,
  });

  if (!response.ok) {
    let errorDetail = `HTTP error! status: ${response.status}`;
    try {
        const errorData = await response.json();
        errorDetail = errorData.detail || errorDetail;
    } catch (e) {
        // Fallback if not JSON
    }
    throw new Error(errorDetail);
  }

  if (response.status === 204) {
      return {} as T;
  }

  return response.json();
}
