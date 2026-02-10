"use client";

import { useState, useEffect, useRef } from "react";
import { chatService } from "@/services/chat";

export default function ChatPage() {
    const [messages, setMessages] = useState<{role: string, content: string, tool_calls?: any[]}[]>([]);
    const [input, setInput] = useState("");
    const [conversationId, setConversationId] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSendMessage = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!input.trim() || isLoading) return;

        const userMsg = { role: "user", content: input };
        setMessages((prev) => [...prev, userMsg]);
        setInput("");
        setIsLoading(true);

        try {
            const data = await chatService.sendMessage(input, conversationId);
            setMessages((prev) => [...prev, { 
                role: "assistant", 
                content: data.response,
                tool_calls: data.tool_calls 
            }]);
            if (data.conversation_id) setConversationId(data.conversation_id);
        } catch (error) {
            console.error("Chat error:", error);
            setMessages((prev) => [...prev, { role: "system", content: "Error: Failed to get response." }]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-[calc(100vh-100px)] max-w-2xl mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Todo Chatbot</h1>
            <div className="flex-1 overflow-y-auto mb-4 p-4 border rounded shadow-inner bg-gray-50 dark:bg-gray-900">
                {messages.length === 0 && (
                    <div className="text-center text-gray-500 mt-10">
                        Ask me to list your tasks or add a new one!
                    </div>
                )}
                {messages.map((msg, i) => (
                    <div key={i} className={`mb-4 flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                        <div className={`max-w-[80%] p-3 rounded-lg ${
                            msg.role === 'user' 
                                ? 'bg-blue-600 text-white rounded-br-none' 
                                : msg.role === 'system'
                                    ? 'bg-red-100 text-red-800'
                                    : 'bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border border-gray-200 dark:border-gray-700 rounded-bl-none'
                        }`}>
                            <div>{msg.content}</div>
                            {msg.tool_calls && msg.tool_calls.length > 0 && (
                                <div className="mt-2 pt-2 border-t border-gray-100 dark:border-gray-700 text-[10px] uppercase tracking-wider text-gray-400 font-semibold">
                                    Tools: {msg.tool_calls.map((tc: any) => tc.function.name).join(", ")}
                                </div>
                            )}
                        </div>
                    </div>
                ))}
                {isLoading && (
                    <div className="flex justify-start mb-4">
                        <div className="bg-white dark:bg-gray-800 p-3 rounded-lg border border-gray-200 dark:border-gray-700 italic text-gray-500">
                            Thinking...
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>
            <form onSubmit={handleSendMessage} className="flex gap-2 items-end">
                <textarea
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => {
                        if (e.key === 'Enter' && !e.shiftKey) {
                            e.preventDefault();
                            handleSendMessage(e as any);
                        }
                    }}
                    placeholder="e.g. Add a task to buy milk..."
                    className="flex-1 p-3 border rounded-lg dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none min-h-[50px] max-h-[200px]"
                    rows={1}
                    disabled={isLoading}
                />
                <button
                    type="submit"
                    className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-medium disabled:opacity-50 transition-colors h-fit"
                    disabled={isLoading}
                >
                    Send
                </button>
            </form>
        </div>
    );
}
