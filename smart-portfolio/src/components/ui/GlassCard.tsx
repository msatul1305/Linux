import React from 'react';
import { cn } from '../../lib/utils';
import { motion, type HTMLMotionProps } from 'framer-motion';

interface GlassCardProps extends HTMLMotionProps<"div"> {
    children: React.ReactNode;
    className?: string;
    hoverEffect?: boolean;
}

export const GlassCard: React.FC<GlassCardProps> = ({ children, className, hoverEffect = true, ...props }) => {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            whileHover={hoverEffect ? { scale: 1.01, boxShadow: "0 20px 40px rgba(0,0,0,0.4)" } : {}}
            transition={{ duration: 0.4, ease: "easeOut" }}
            className={cn(
                "relative overflow-hidden rounded-lg border border-gray-200 dark:border-white/10 bg-white/80 dark:bg-[#111]/90 shadow-sm dark:shadow-none transition-colors duration-300",
                className
            )}
            {...props}
        >
            <div className="relative z-10">
                {children}
            </div>
        </motion.div>
    );
};
