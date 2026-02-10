"use client";

import { useState, useRef, useEffect } from 'react';
import { Task, taskService } from '@/services/tasks';
import { CheckCircle2, Circle, Trash2, Calendar, Flag, Clock, Edit2, X, Check } from 'lucide-react';
import { toast } from 'sonner';
import { motion, AnimatePresence } from 'framer-motion';

interface TaskItemProps {
  task: Task;
  onUpdate: () => void;
}

export default function TaskItem({ task, onUpdate }: TaskItemProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [editedTitle, setEditedTitle] = useState(task.title);
  const [isUpdating, setIsUpdating] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (isEditing && inputRef.current) {
      inputRef.current.focus();
    }
  }, [isEditing]);

  const handleToggle = async () => {
    try {
      await taskService.toggleComplete(task.id);
      toast.success(task.status === 'DONE' ? 'Task marked as active' : 'Excellent work! Task completed');
      onUpdate();
    } catch (error) {
      toast.error('Failed to update task');
      console.error('Failed to toggle task:', error);
    }
  };

  const handleDelete = async () => {
    try {
      await taskService.deleteTask(task.id);
      toast.success('Task removed');
      onUpdate();
    } catch (error) {
      toast.error('Failed to delete task');
      console.error('Failed to delete task:', error);
    }
  };

  const handleUpdate = async () => {
    if (!editedTitle.trim() || editedTitle === task.title) {
      setIsEditing(false);
      setEditedTitle(task.title);
      return;
    }

    setIsUpdating(true);
    try {
      await taskService.updateTask(task.id, { title: editedTitle });
      toast.success('Task updated');
      setIsEditing(false);
      onUpdate();
    } catch (error) {
      toast.error('Failed to update task');
      console.error('Failed to update task:', error);
    } finally {
      setIsUpdating(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') handleUpdate();
    if (e.key === 'Escape') {
      setIsEditing(false);
      setEditedTitle(task.title);
    }
  };

  const priorityConfig = {
    HIGH: { color: 'text-red-600 dark:text-red-400', bg: 'bg-red-50 dark:bg-red-900/20', border: 'border-red-100 dark:border-red-800', icon: 'text-red-500' },
    MEDIUM: { color: 'text-orange-600 dark:text-orange-400', bg: 'bg-orange-50 dark:bg-orange-900/20', border: 'border-orange-100 dark:border-orange-800', icon: 'text-orange-500' },
    LOW: { color: 'text-blue-600 dark:text-blue-400', bg: 'bg-blue-50 dark:bg-blue-900/20', border: 'border-blue-100 dark:border-blue-800', icon: 'text-blue-500' }
  };

  const config = priorityConfig[task.priority] || priorityConfig.MEDIUM;
  const isDone = task.status === 'DONE';

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, scale: 0.95 }}
      className={`group relative flex items-center justify-between p-5 bg-white dark:bg-gray-800/50 rounded-2xl border ${
        isDone ? 'border-gray-100 dark:border-gray-800 opacity-75' : 'border-gray-100 dark:border-gray-800 shadow-sm hover:shadow-md hover:border-indigo-100 dark:hover:border-indigo-900'
      } transition-all duration-300 mb-3`}
    >
      {/* Selection Overlay */}
      {!isDone && !isEditing && (
        <div className="absolute inset-0 bg-gradient-to-r from-indigo-50/0 via-indigo-50/0 to-indigo-50/30 dark:to-indigo-900/10 opacity-0 group-hover:opacity-100 rounded-2xl transition-opacity pointer-events-none" />
      )}

      <div className="flex items-center space-x-5 flex-grow relative z-10">
        <button 
          onClick={handleToggle} 
          disabled={isEditing}
          className={`flex-shrink-0 transition-transform active:scale-90 focus:outline-none ${isEditing ? 'opacity-20' : ''}`}
        >
          {isDone ? (
            <div className="bg-indigo-600 rounded-full p-0.5">
              <CheckCircle2 className="w-6 h-6 text-white" />
            </div>
          ) : (
            <div className="text-gray-300 dark:text-gray-600 hover:text-indigo-500 transition-colors">
              <Circle className="w-6 h-6 stroke-[1.5px] hover:stroke-[2px]" />
            </div>
          )}
        </button>
        
        <div className="flex flex-col min-w-0 flex-grow">
          {isEditing ? (
            <div className="flex items-center gap-2">
              <input
                ref={inputRef}
                type="text"
                className="flex-grow bg-gray-50 dark:bg-gray-800 border border-indigo-100 dark:border-indigo-900 rounded-xl px-3 py-1 text-[17px] font-semibold text-gray-800 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500/20"
                value={editedTitle}
                onChange={(e) => setEditedTitle(e.target.value)}
                onKeyDown={handleKeyDown}
                disabled={isUpdating}
              />
              <button 
                onClick={handleUpdate}
                disabled={isUpdating}
                className="p-1.5 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
              >
                <Check className="w-4 h-4" />
              </button>
              <button 
                onClick={() => { setIsEditing(false); setEditedTitle(task.title); }}
                disabled={isUpdating}
                className="p-1.5 bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          ) : (
            <span 
              className={`text-[17px] font-semibold truncate transition-all duration-300 ${
                isDone ? 'line-through text-gray-400 dark:text-gray-500 font-normal' : 'text-gray-800 dark:text-gray-100'
              }`}
            >
              {task.title}
            </span>
          )}
          
          {!isEditing && (
            <div className="flex flex-wrap items-center gap-3 mt-1.5">
              <span className={`inline-flex items-center px-2.5 py-0.5 rounded-lg text-[11px] font-bold tracking-wider uppercase ${config.bg} ${config.color} border ${config.border}`}>
                <Flag className={`w-3 h-3 mr-1.5 ${config.icon}`} />
                {task.priority}
              </span>
              <div className="flex items-center text-gray-400 dark:text-gray-500 text-xs font-medium">
                <Clock className="w-3.5 h-3.5 mr-1.5 opacity-70" />
                {new Date(task.created_at).toLocaleDateString(undefined, { month: 'short', day: 'numeric' })}
              </div>
            </div>
          )}
        </div>
      </div>

      <div className="flex items-center pl-4 relative z-10 gap-1">
        {!isEditing && !isDone && (
          <button 
            onClick={() => setIsEditing(true)}
            className="p-2.5 text-gray-300 dark:text-gray-600 hover:text-indigo-600 dark:hover:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-950/30 rounded-xl transition-all opacity-0 group-hover:opacity-100 focus:opacity-100"
            title="Edit task"
          >
            <Edit2 className="w-5 h-5" />
          </button>
        )}
        <button 
          onClick={handleDelete}
          className="p-2.5 text-gray-300 dark:text-gray-600 hover:text-red-500 dark:hover:text-red-400 hover:bg-red-50 dark:hover:bg-red-950/30 rounded-xl transition-all opacity-0 group-hover:opacity-100 focus:opacity-100"
          title="Delete task"
        >
          <Trash2 className="w-5 h-5" />
        </button>
      </div>
    </motion.div>
  );
}