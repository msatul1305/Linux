import React from 'react';
import type { Asset } from '../types';
import { ArrowDown, ArrowUp } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface Trade {
    ticker: string;
    action: string;
    amount: number;
    shares: number;
}

interface RebalanceTableProps {
    assets: Asset[];
    currentWeights: Record<string, number>;
    trades: Trade[];
}

export const RebalanceTable: React.FC<RebalanceTableProps> = ({ assets, currentWeights, trades }) => {
    return (
        <div className="overflow-hidden h-full">
            <div className="p-6 border-b border-gray-200 dark:border-white/10">
                <h2 className="text-xl font-semibold text-gray-900 dark:text-white">Rebalancing Recommendations</h2>
            </div>

            {trades.length === 0 ? (
                <div className="p-8 text-center text-gray-400 dark:text-gray-500">
                    <p>Portfolio is balanced. No trades needed.</p>
                </div>
            ) : (
                <div className="overflow-x-auto">
                    <table className="w-full text-sm text-left">
                        <thead className="bg-gray-50 dark:bg-white/5 text-gray-500 dark:text-gray-400 font-medium">
                            <tr>
                                <th className="p-4">Asset</th>
                                <th className="p-4">Current Weight</th>
                                <th className="p-4">Target Weight</th>
                                <th className="p-4">Action</th>
                                <th className="p-4">Amount</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-gray-200 dark:divide-white/5">
                            <AnimatePresence>
                                {trades.map((trade, idx) => {
                                    const asset = assets.find(a => a.ticker === trade.ticker);
                                    if (!asset) return null;

                                    const currentWeight = (asset.currentPrice * asset.quantity) / Object.values(currentWeights).reduce((a, b) => a + b, 0) || 0;
                                    const targetWeight = asset.targetWeight || 0;

                                    return (
                                        <motion.tr
                                            key={trade.ticker}
                                            initial={{ opacity: 0, x: -20 }}
                                            animate={{ opacity: 1, x: 0 }}
                                            exit={{ opacity: 0, x: 20 }}
                                            transition={{ delay: idx * 0.05 }}
                                            className="hover:bg-gray-50 dark:hover:bg-white/5 transition-colors"
                                        >
                                            <td className="p-4 font-medium text-gray-900 dark:text-white">{asset.name}</td>
                                            <td className="p-4 text-gray-600 dark:text-gray-300">{(currentWeight * 100).toFixed(1)}%</td>
                                            <td className="p-4 text-gray-600 dark:text-gray-300">{(targetWeight * 100).toFixed(1)}%</td>
                                            <td className="p-4">
                                                <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-medium ${trade.action === 'BUY'
                                                    ? 'bg-emerald-100 dark:bg-emerald-500/20 text-emerald-700 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-500/30'
                                                    : 'bg-red-100 dark:bg-red-500/20 text-red-700 dark:text-red-400 border border-red-200 dark:border-red-500/30'
                                                    }`}>
                                                    {trade.action === 'BUY' ? <ArrowUp size={12} /> : <ArrowDown size={12} />}
                                                    {trade.action}
                                                </span>
                                            </td>
                                            <td className="p-4 font-semibold text-gray-900 dark:text-gray-200">
                                                ${trade.amount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                                            </td>
                                        </motion.tr>
                                    );
                                })}
                            </AnimatePresence>
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
};
