import React from 'react';
import { Activity, TrendingUp, AlertTriangle } from 'lucide-react';

interface RiskMetricsProps {
    volatility: number;
    sharpeRatio: number;
    maxDrawdown: number;
}

export const RiskMetrics: React.FC<RiskMetricsProps> = ({ volatility, sharpeRatio, maxDrawdown }) => {
    return (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-0 border border-gray-200 dark:border-white/10 bg-white dark:bg-[#111] rounded-lg overflow-hidden transition-colors duration-300">
            <div className="p-4 border-r border-gray-200 dark:border-white/10 last:border-r-0">
                <div className="flex items-center gap-2 mb-1">
                    <Activity size={14} className="text-gray-400 dark:text-gray-500" />
                    <span className="text-xs font-medium text-gray-500 uppercase tracking-wider">Portfolio Volatility</span>
                </div>
                <p className="text-2xl font-mono text-gray-900 dark:text-white">{(volatility * 100).toFixed(2)}%</p>
                <div className="w-full bg-gray-200 dark:bg-gray-800 h-0.5 mt-3">
                    <div className="bg-blue-500 h-0.5" style={{ width: `${Math.min(volatility * 100 * 2, 100)}%` }} />
                </div>
            </div>

            <div className="p-4 border-r border-gray-200 dark:border-white/10 last:border-r-0">
                <div className="flex items-center gap-2 mb-1">
                    <TrendingUp size={14} className="text-gray-400 dark:text-gray-500" />
                    <span className="text-xs font-medium text-gray-500 uppercase tracking-wider">Sharpe Ratio</span>
                </div>
                <p className={`text-2xl font-mono ${sharpeRatio >= 2 ? 'text-green-600 dark:text-green-500' : sharpeRatio >= 1 ? 'text-yellow-600 dark:text-yellow-500' : 'text-red-600 dark:text-red-500'}`}>
                    {sharpeRatio.toFixed(2)}
                </p>
                <p className="text-[10px] text-gray-500 dark:text-gray-600 mt-1">Risk Adjusted Return</p>
            </div>

            <div className="p-4 last:border-r-0">
                <div className="flex items-center gap-2 mb-1">
                    <AlertTriangle size={14} className="text-gray-400 dark:text-gray-500" />
                    <span className="text-xs font-medium text-gray-500 uppercase tracking-wider">Max Drawdown</span>
                </div>
                <p className="text-2xl font-mono text-red-600 dark:text-red-500">{(maxDrawdown * 100).toFixed(2)}%</p>
                <p className="text-[10px] text-gray-500 dark:text-gray-600 mt-1">Historical Stress Test</p>
            </div>
        </div>
    );
};
