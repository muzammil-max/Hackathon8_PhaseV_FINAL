import { fetchClient } from '@/lib/api';

export interface Task {
  id: string;
  title: string;
  status: 'TODO' | 'IN_PROGRESS' | 'DONE';
  priority: 'LOW' | 'MEDIUM' | 'HIGH';
  created_at: string;
  updated_at: string;
}

export type TaskCreate = Pick<Task, 'title'> & Partial<Pick<Task, 'priority'>>;
export type TaskUpdate = Partial<Pick<Task, 'title' | 'status' | 'priority'>>;

export const taskService = {
  async getTasks(): Promise<Task[]> {
    return fetchClient<Task[]>('/tasks/');
  },

  async createTask(task: TaskCreate): Promise<Task> {
    return fetchClient<Task>('/tasks/', {
      method: 'POST',
      body: JSON.stringify(task),
    });
  },

  async updateTask(id: string, update: TaskUpdate): Promise<Task> {
    return fetchClient<Task>(`/tasks/${id}`, {
      method: 'PUT',
      body: JSON.stringify(update),
    });
  },

  async deleteTask(id: string): Promise<void> {
    return fetchClient<void>(`/tasks/${id}`, {
      method: 'DELETE',
    });
  },

  async toggleComplete(id: string): Promise<Task> {
    return fetchClient<Task>(`/tasks/${id}/complete`, {
      method: 'PATCH',
    });
  },
};