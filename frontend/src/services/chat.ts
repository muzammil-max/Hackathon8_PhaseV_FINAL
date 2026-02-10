import { fetchClient } from '@/lib/api';

export interface ChatResponse {
    conversation_id: string;
    response: string;
    tool_calls: any[];
}

export const chatService = {
    async sendMessage(message: string, conversationId?: string | null): Promise<ChatResponse> {
        return fetchClient<ChatResponse>('/chat/', {
            method: 'POST',
            body: JSON.stringify({
                message,
                conversation_id: conversationId || undefined
            }),
        });
    }
};
