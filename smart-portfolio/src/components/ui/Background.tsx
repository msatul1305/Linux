import React from 'react';

export const Background: React.FC = () => {
    return (
        <div className="fixed inset-0 z-[-1] bg-gray-50 dark:bg-[#0a0a0a] transition-colors duration-500">
            {/* Subtle Grid Pattern */}
            <div
                className="absolute inset-0 opacity-[0.05] dark:opacity-[0.03]"
                style={{
                    backgroundImage: `linear-gradient(var(--grid-color, #ccc) 1px, transparent 1px), linear-gradient(90deg, var(--grid-color, #ccc) 1px, transparent 1px)`,
                    backgroundSize: '40px 40px'
                }}
            >
                <style>{`
                    .dark .absolute { --grid-color: #333; }
                    :root { --grid-color: #cbd5e1; }
                `}</style>
            </div>

            {/* Vignette */}
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,rgba(0,0,0,0.05)_100%)] dark:bg-[radial-gradient(circle_at_center,transparent_0%,rgba(0,0,0,0.4)_100%)]" />
        </div>
    );
};
