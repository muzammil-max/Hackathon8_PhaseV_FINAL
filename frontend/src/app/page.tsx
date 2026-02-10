"use client";

import { useEffect, useState, useCallback } from 'react';
import { useRouter } from 'next/navigation';
import { Task, taskService } from '@/services/tasks';
import { authClient } from '@/lib/auth-client';
import TaskForm from '@/components/TaskForm';
import TaskList from '@/components/TaskList';
import { LogOut, CheckCircle2, LayoutDashboard, User, TrendingUp, Zap, Sparkles, Bell } from 'lucide-react';
import { Toaster } from 'sonner';
import { motion, AnimatePresence } from 'framer-motion';
import { ThemeToggle } from '@/components/ThemeToggle';

export default function DashboardPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const { data: session, isPending } = authClient.useSession();
  const router = useRouter();

  const fetchTasks = useCallback(async () => {
    try {
      const data = await taskService.getTasks();
      setTasks(data);
    } catch (error) {
      console.error('Failed to fetch tasks:', error);
    }
  }, []);

  useEffect(() => {
    if (!isPending && !session) {
      router.push('/login');
    } else if (session) {
      fetchTasks();
    }
  }, [session, isPending, router, fetchTasks]);

  const handleLogout = async () => {
    await authClient.signOut({
        fetchOptions: {
            onSuccess: () => {
                router.push("/login");
            }
        }
    });
  };

  if (isPending) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-white dark:bg-gray-950 transition-colors duration-500">
        <div className="flex flex-col items-center gap-6">
          <div className="relative">
            <div className="h-20 w-20 rounded-[2rem] bg-indigo-50 dark:bg-indigo-900/20 animate-pulse"></div>
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="h-10 w-10 rounded-full border-t-2 border-indigo-600 animate-spin"></div>
            </div>
          </div>
          <div className="text-center">
            <h3 className="text-2xl font-black text-gray-900 dark:text-white tracking-tighter">TaskFlow</h3>
            <p className="text-gray-400 dark:text-gray-500 mt-1 font-medium italic">Setting up your workspace...</p>
          </div>
        </div>
      </div>
    );
  }

  if (!session) return null;

  const completedCount = tasks.filter(t => t.status === 'DONE').length;
  const progress = tasks.length > 0 ? Math.round((completedCount / tasks.length) * 100) : 0;

  return (
    <main className="min-h-screen bg-[#F8FAFC] dark:bg-gray-950 transition-colors duration-500 pb-20">
      
      {/* Navbar */}
      <nav className="bg-white/70 dark:bg-gray-900/70 border-b border-gray-100 dark:border-gray-800 sticky top-0 z-50 backdrop-blur-2xl transition-colors duration-500">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-20 items-center">
            <div className="flex items-center gap-4">
              <motion.div 
                whileHover={{ scale: 1.05, rotate: 5 }}
                className="bg-indigo-600 p-2.5 rounded-2xl shadow-lg shadow-indigo-200 dark:shadow-none"
              >
                <CheckCircle2 className="w-6 h-6 text-white" />
              </motion.div>
              <h1 className="text-2xl font-black tracking-tighter text-gray-900 dark:text-white">
                Task<span className="text-indigo-600">Flow</span>
              </h1>
            </div>
            
            <div className="flex items-center gap-4 sm:gap-8">
              <div className="hidden sm:flex items-center gap-3 px-4 py-2 bg-gray-50/50 dark:bg-gray-800/50 rounded-2xl border border-gray-100 dark:border-gray-800 transition-colors">
                <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-indigo-500 to-indigo-600 flex items-center justify-center text-white font-bold shadow-sm">
                  {session.user.name?.[0]?.toUpperCase() || <User className="w-4 h-4" />}
                </div>
                <div className="flex flex-col">
                  <span className="text-sm font-bold text-gray-900 dark:text-gray-100 leading-none mb-1">
                    {session.user.name || 'Member'}
                  </span>
                  <span className="text-[10px] font-black text-indigo-500 uppercase tracking-widest">
                    Pro Workspace
                  </span>
                </div>
              </div>
              
              <div className="flex items-center gap-2">
                <ThemeToggle />
                <button className="p-2.5 text-gray-400 hover:text-indigo-600 hover:bg-indigo-50 dark:hover:bg-indigo-950/30 rounded-xl transition-all relative">
                   <Bell className="w-5 h-5" />
                   <span className="absolute top-2.5 right-2.5 w-2 h-2 bg-indigo-600 rounded-full border-2 border-white dark:border-gray-900"></span>
                </button>
                <button
                  onClick={handleLogout}
                  className="p-2.5 text-gray-400 hover:text-red-500 hover:bg-red-50 dark:hover:bg-red-950/30 rounded-xl transition-all"
                  title="Logout"
                >
                  <LogOut className="w-5 h-5" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12">
        
        {/* Welcome Section */}
        <header className="mb-12 flex flex-col md:flex-row md:items-end justify-between gap-8">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
          >
            <div className="flex items-center gap-2 mb-4">
              <span className="inline-block px-3 py-1 bg-indigo-50 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400 rounded-full text-[10px] font-black uppercase tracking-[0.2em] border border-indigo-100 dark:border-indigo-800 transition-colors">
                Productivity Hub
              </span>
              <span className="text-gray-300 dark:text-gray-700">•</span>
              <span className="text-gray-400 dark:text-gray-500 text-xs font-bold uppercase tracking-widest">
                {new Date().toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' })}
              </span>
            </div>
            <h2 className="text-5xl font-black text-gray-900 dark:text-white tracking-tight leading-[1.1] transition-colors">
              Hello, {session.user.name?.split(' ')[0] || 'User'} <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 via-purple-600 to-indigo-600 bg-[length:200%_auto] animate-gradient">Get things done.</span>
            </h2>
          </motion.div>

          <motion.div 
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className="bg-white dark:bg-gray-900 p-6 rounded-[2.5rem] shadow-xl shadow-gray-200/50 dark:shadow-none border border-gray-100 dark:border-gray-800 flex items-center gap-6 min-w-[320px] transition-all duration-500"
          >
            <div className="relative w-20 h-20 flex items-center justify-center">
              <svg className="w-full h-full transform -rotate-90">
                <circle
                  cx="40"
                  cy="40"
                  r="34"
                  stroke="currentColor"
                  strokeWidth="8"
                  fill="transparent"
                  className="text-gray-50 dark:text-gray-800"
                />
                <circle
                  cx="40"
                  cy="40"
                  r="34"
                  stroke="currentColor"
                  strokeWidth="8"
                  fill="transparent"
                  strokeDasharray={213.6}
                  strokeDashoffset={213.6 - (213.6 * progress) / 100}
                  className="text-indigo-600 transition-all duration-1000 ease-out"
                  strokeLinecap="round"
                />
              </svg>
              <span className="absolute text-xl font-black text-gray-900 dark:text-white">{progress}%</span>
            </div>
            <div className="flex flex-col">
              <span className="text-[10px] font-black text-gray-400 dark:text-gray-500 uppercase tracking-[0.2em] mb-1">Success Rate</span>
              <span className="text-3xl font-black text-gray-900 dark:text-white tabular-nums">
                {completedCount}<span className="text-gray-200 dark:text-gray-700 text-xl font-medium mx-1">/</span>{tasks.length}
              </span>
              <span className="text-xs font-bold text-green-500 mt-1 flex items-center gap-1">
                <TrendingUp className="w-3 h-3" /> +12% this week
              </span>
            </div>
          </motion.div>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
          {/* Main Content */}
          <div className="lg:col-span-8 space-y-10">
            <TaskForm onTaskCreated={fetchTasks} />
            
            <div className="bg-white dark:bg-gray-900 rounded-[3rem] p-10 shadow-xl shadow-gray-200/30 dark:shadow-none border border-gray-100 dark:border-gray-800 min-h-[600px] relative overflow-hidden transition-all duration-500">
              <div className="absolute top-0 right-0 p-8 opacity-5">
                 <LayoutDashboard className="w-40 h-40 text-indigo-600" />
              </div>
              
              <div className="flex items-center justify-between mb-10 relative z-10">
                <div className="flex items-center gap-4">
                  <div className="p-3 bg-indigo-50 dark:bg-indigo-900/30 rounded-2xl transition-colors">
                    <Zap className="w-6 h-6 text-indigo-600 dark:text-indigo-400 fill-indigo-600 dark:fill-indigo-400" />
                  </div>
                  <div>
                    <h3 className="text-2xl font-black text-gray-900 dark:text-white tracking-tight">Focus List</h3>
                    <p className="text-sm text-gray-400 dark:text-gray-500 font-bold uppercase tracking-widest mt-0.5">Primary Objectives</p>
                  </div>
                </div>
                
                <div className="flex items-center gap-3">
                  <div className="flex -space-x-2">
                    {[1,2,3].map(i => (
                      <div key={i} className="w-8 h-8 rounded-full border-2 border-white dark:border-gray-900 bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-[10px] font-bold text-gray-400">
                        U{i}
                      </div>
                    ))}
                  </div>
                  <span className="text-xs font-black text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-900/30 px-3 py-1.5 rounded-xl border border-indigo-100 dark:border-indigo-800 transition-colors">
                    {tasks.length} Active
                  </span>
                </div>
              </div>
              
              <div className="relative z-10">
                <TaskList tasks={tasks} onUpdate={fetchTasks} />
              </div>
            </div>
          </div>

          {/* Sidebar */}
          <div className="lg:col-span-4 space-y-10">
            {/* Pro Tip Card */}
            <motion.div 
              whileHover={{ y: -5 }}
              className="bg-gray-900 dark:bg-indigo-900/20 rounded-[3rem] p-10 text-white shadow-2xl shadow-indigo-100 dark:shadow-none border border-transparent dark:border-indigo-800/30 relative overflow-hidden group transition-all duration-500"
            >
              <div className="absolute top-0 right-0 p-4 translate-x-4 -translate-y-4 group-hover:translate-x-0 group-hover:translate-y-0 transition-transform duration-500 opacity-20">
                <Sparkles className="w-24 h-24 text-indigo-400" />
              </div>
              <div className="relative z-10">
                <div className="bg-indigo-600 w-12 h-12 rounded-2xl flex items-center justify-center mb-8 shadow-lg shadow-indigo-500/20">
                  <TrendingUp className="w-6 h-6" />
                </div>
                <h3 className="font-black text-2xl mb-4 tracking-tight leading-tight">Master Your <br /> Workflow</h3>
                <p className="text-gray-400 dark:text-gray-300 text-sm leading-relaxed font-medium mb-8">
                  Try the &quot;Two-Minute Rule&quot;: if a task takes less than two minutes, do it immediately.
                </p>
                <button className="w-full py-4 bg-white dark:bg-indigo-600 text-gray-900 dark:text-white font-black rounded-2xl hover:bg-indigo-50 dark:hover:bg-indigo-700 transition-colors shadow-lg">
                  Read Guide
                </button>
              </div>
            </motion.div>

            {/* Analysis Card */}
            <div className="bg-white dark:bg-gray-900 rounded-[3rem] p-10 shadow-xl shadow-gray-200/30 dark:shadow-none border border-gray-100 dark:border-gray-800 transition-all duration-500">
              <h3 className="font-black text-gray-900 dark:text-white text-sm mb-8 uppercase tracking-[0.2em] text-gray-400 dark:text-gray-500">Task Analysis</h3>
              <div className="space-y-8">
                {['HIGH', 'MEDIUM', 'LOW'].map(p => {
                   const count = tasks.filter(t => t.priority === p).length;
                   const percentage = tasks.length ? (count / tasks.length) * 100 : 0;
                   const theme = {
                     HIGH: { color: 'bg-rose-500', shadow: 'shadow-rose-100 dark:shadow-none', text: 'text-rose-600' },
                     MEDIUM: { color: 'bg-amber-500', shadow: 'shadow-amber-100 dark:shadow-none', text: 'text-amber-600' },
                     LOW: { color: 'bg-sky-500', shadow: 'shadow-sky-100 dark:shadow-none', text: 'text-sky-600' }
                   }[p as 'HIGH' | 'MEDIUM' | 'LOW'];
                   
                   return (
                     <div key={p}>
                       <div className="flex justify-between items-end mb-3">
                         <span className="text-xs font-black text-gray-900 dark:text-gray-100 uppercase tracking-widest">{p}</span>
                         <span className={`text-xs font-black ${theme.text}`}>{count} Tasks</span>
                       </div>
                       <div className="w-full bg-gray-50 dark:bg-gray-800 rounded-full h-3.5 p-1 border border-gray-100 dark:border-gray-700">
                         <motion.div 
                           initial={{ width: 0 }}
                           animate={{ width: `${percentage}%` }}
                           transition={{ duration: 1.5, ease: "circOut" }}
                           className={`h-full rounded-full ${theme.color} ${theme.shadow} shadow-sm`}
                         />
                       </div>
                     </div>
                   );
                })}
              </div>
              
              <div className="mt-10 pt-10 border-t border-gray-50 dark:border-gray-800 flex items-center justify-between">
                 <div className="flex flex-col">
                    <span className="text-[10px] font-black text-gray-400 dark:text-gray-500 uppercase tracking-widest mb-1">Weekly</span>
                    <span className="text-xl font-black text-gray-900 dark:text-white">74% Avg</span>
                 </div>
                 <div className="w-20 h-10 bg-indigo-50 dark:bg-indigo-900/30 rounded-xl flex items-center justify-center transition-colors">
                    <div className="flex gap-1 items-end h-4">
                       {[0.4, 0.7, 0.5, 0.9, 0.6].map((h, i) => (
                         <div key={i} className="w-1.5 bg-indigo-600 dark:bg-indigo-400 rounded-full" style={{ height: `${h * 100}%` }}></div>
                       ))}
                    </div>
                 </div>
              </div>
            </div>

            <p className="text-center text-gray-400 dark:text-gray-600 text-[10px] font-black uppercase tracking-[0.3em] px-10">
              TaskFlow Pro v2.0.4
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}