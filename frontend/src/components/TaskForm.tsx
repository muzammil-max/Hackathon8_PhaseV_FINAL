"use client";

import { useState } from 'react';
import { taskService } from '@/services/tasks';
import { Plus, Loader2, Target, Flag } from 'lucide-react';
import { toast } from 'sonner';
import { motion } from 'framer-motion';

interface TaskFormProps {
  onTaskCreated: () => void;
}

export default function TaskForm({ onTaskCreated }: TaskFormProps) {
  const [title, setTitle] = useState('');
  const [priority, setPriority] = useState<'LOW' | 'MEDIUM' | 'HIGH'>('MEDIUM');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;

    setIsSubmitting(true);
    try {
      await taskService.createTask({ title, priority });
      toast.success('Task created successfully');
      setTitle('');
      setPriority('MEDIUM');
      onTaskCreated();
    } catch (error) {
      toast.error('Failed to create task');
      console.error('Failed to create task:', error);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <motion.div 
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="mb-10"
    >
      <form 
        onSubmit={handleSubmit} 
        className="bg-white dark:bg-gray-900 p-2 rounded-[24px] shadow-xl shadow-indigo-100/50 dark:shadow-none border border-gray-100 dark:border-gray-800 flex flex-col md:flex-row gap-2 transition-all duration-500"
      >
        <div className="relative flex-grow">
          <div className="absolute inset-y-0 left-0 pl-5 flex items-center pointer-events-none">
            <Target className="h-5 w-5 text-indigo-400" />
          </div>
          <input
            type="text"
            placeholder="Capture your next big goal..."
            className="w-full pl-12 pr-4 py-4 bg-transparent border-none focus:ring-0 text-gray-700 dark:text-gray-200 text-lg placeholder-gray-400 font-medium"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            disabled={isSubmitting}
          />
        </div>
        
        <div className="flex items-center gap-2 p-1 md:p-0">
          <div className="relative group">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <Flag className={`h-4 w-4 ${
                priority === 'HIGH' ? 'text-red-500' : priority === 'MEDIUM' ? 'text-orange-500' : 'text-blue-500'
              }`} />
            </div>
            <select
              className="pl-9 pr-8 py-3 bg-gray-50 dark:bg-gray-800 border-none rounded-2xl text-sm font-bold text-gray-600 dark:text-gray-300 cursor-pointer appearance-none focus:ring-2 focus:ring-indigo-100 dark:focus:ring-indigo-900 transition-all hover:bg-gray-100 dark:hover:bg-gray-700"
              value={priority}
              onChange={(e) => setPriority(e.target.value as any)}
              disabled={isSubmitting}
            >
              <option value="LOW">Low Priority</option>
              <option value="MEDIUM">Medium Priority</option>
              <option value="HIGH">High Priority</option>
            </select>
            <div className="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
              <svg className="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </div>
          </div>
          
          <button
            type="submit"
            disabled={isSubmitting || !title.trim()}
            className="flex-shrink-0 inline-flex items-center justify-center px-8 py-4 bg-indigo-600 text-white font-bold rounded-2xl hover:bg-indigo-700 disabled:bg-indigo-300 dark:disabled:bg-indigo-900/50 disabled:cursor-not-allowed transition-all shadow-lg shadow-indigo-200 dark:shadow-none active:scale-95 min-w-[140px]"
          >
            {isSubmitting ? (
              <Loader2 className="w-5 h-5 animate-spin" />
            ) : (
              <>
                <Plus className="w-5 h-5 mr-2 stroke-[3px]" />
                Add Task
              </>
            )}
          </button>
        </div>
      </form>
    </motion.div>
  );
}