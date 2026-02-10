"use client";

import { Task } from '@/services/tasks';
import TaskItem from './TaskItem';
import { AnimatePresence, motion } from 'framer-motion';
import { Sparkles, Inbox } from 'lucide-react';

interface TaskListProps {
  tasks: Task[];
  onUpdate: () => void;
}

export default function TaskList({ tasks, onUpdate }: TaskListProps) {
  if (tasks.length === 0) {
    return (
      <motion.div 
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        className="flex flex-col items-center justify-center py-20 bg-gray-50/50 dark:bg-gray-900/50 rounded-[2.5rem] border-2 border-dashed border-gray-100 dark:border-gray-800 text-center transition-all duration-500"
      >
        <div className="relative mb-6">
          <div className="bg-white dark:bg-gray-800 p-6 rounded-3xl shadow-xl shadow-indigo-100/50 dark:shadow-none relative z-10 transition-colors">
            <Inbox className="w-12 h-12 text-indigo-500 stroke-[1.5px]" />
          </div>
          <motion.div 
            animate={{ scale: [1, 1.2, 1], opacity: [0.3, 0.6, 0.3] }}
            transition={{ repeat: Infinity, duration: 3 }}
            className="absolute -top-2 -right-2 bg-yellow-400 p-2 rounded-xl shadow-lg z-20"
          >
            <Sparkles className="w-4 h-4 text-white" />
          </motion.div>
        </div>
        <h3 className="text-2xl font-black text-gray-900 dark:text-white mb-2 tracking-tight">Clean Slate</h3>
        <p className="text-gray-400 dark:text-gray-500 max-w-[280px] font-medium leading-relaxed">
          Your workspace is empty and ready for new challenges. What will you achieve today?
        </p>
      </motion.div>
    );
  }

  return (
    <div className="space-y-1">
      <AnimatePresence mode="popLayout">
        {tasks.map((task) => (
          <TaskItem key={task.id} task={task} onUpdate={onUpdate} />
        ))}
      </AnimatePresence>
    </div>
  );
}