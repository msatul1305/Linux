import React, { useMemo } from 'react';
import type { Asset } from '../types';
import { ArrowUp, PieChart, RefreshCw } from 'lucide-react';

interface Trade {
    ticker: string;
    action: string;
    amount: number;
    shares: number;
}

interface AssetClassDetailsProps {
    category: string;
    assets: Asset[];
    trades: Trade[];
    onClose: () => void;
}

export const AssetClassDetails: React.FC<AssetClassDetailsProps> = ({ category, assets, trades, onClose }) => {
    const totalValue = assets.reduce((sum, asset) => sum + (asset.currentPrice * asset.quantity), 0);

    // Filter trades for this category
    const categoryTrades = useMemo(() => {
        return trades.filter(trade => assets.some(a => a.ticker === trade.ticker));
    }, [trades, assets]);

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
            <div className="bg-white dark:bg-[#111] border border-gray-200 dark:border-white/10 rounded-xl shadow-2xl w-full max-w-2xl overflow-hidden flex flex-col max-h-[80vh] animate-in fade-in zoom-in duration-200">
                {/* Header */}
                <div className="p-6 border-b border-gray-200 dark:border-white/10 flex justify-between items-center bg-gray-50 dark:bg-white/5">
                    <div>
                        <h3 className="text-xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
                            <PieChart className="text-indigo-500" size={24} />
                            {category} Holdings
                        </h3>
                        <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
                            Total Exposure: <span className="font-mono font-medium text-gray-900 dark:text-gray-200">${totalValue.toLocaleString()}</span>
                        </p>
                    </div>
                    <button
                        onClick={onClose}
                        className="p-2 hover:bg-gray-200 dark:hover:bg-white/10 rounded-full transition-colors"
                    >
                        ✕
                    </button>
                </div>

                {/* Content */}
                <div className="overflow-y-auto p-6 space-y-8">

                    {/* AI Prediction Section */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="p-4 bg-indigo-50 dark:bg-indigo-900/10 border border-indigo-100 dark:border-indigo-500/20 rounded-lg">
                            <h4 className="text-sm font-semibold text-indigo-900 dark:text-indigo-300 mb-2 flex items-center gap-2">
                                <ArrowUp size={16} /> Dr. Sentiment (Analyst)
                            </h4>
                            <p className="text-xs text-indigo-700 dark:text-indigo-400">
                                {category === 'Stock' && "Bullish momentum detected in Tech and Consumer Discretionary. Earnings surprises are driving valuations higher."}
                                {category === 'Bond' && "Yield curve inversion suggests caution. Favor short-term duration until rates stabilize."}
                                {category === 'Crypto' && "High social volume and on-chain activity. Volatility expected to remain elevated."}
                                {category === 'Commodity' && "Supply constraints in energy sector are supporting prices. Gold acts as a strong hedge."}
                                {!['Stock', 'Bond', 'Crypto', 'Commodity'].includes(category) && `Neutral outlook for ${category}. Monitoring macro indicators for directional cues.`}
                            </p>
                        </div>
                        <div className="p-4 bg-purple-50 dark:bg-purple-900/10 border border-purple-100 dark:border-purple-500/20 rounded-lg">
                            <h4 className="text-sm font-semibold text-purple-900 dark:text-purple-300 mb-2 flex items-center gap-2">
                                <PieChart size={16} /> Quantos (Mathematician)
                            </h4>
                            <p className="text-xs text-purple-700 dark:text-purple-400">
                                {category === 'Stock' && "RSI indicates overbought conditions on daily timeframe. Mean reversion probability: 65%."}
                                {category === 'Bond' && "Correlation with Equities has dropped to 0.2, restoring diversification benefits."}
                                {category === 'Crypto' && "30-day volatility is 2.5x the S&P 500. Sharpe ratio remains attractive at 1.8."}
                                {!['Stock', 'Bond', 'Crypto'].includes(category) && "Statistical models show standard deviation within expected range. No anomaly detected."}
                            </p>
                        </div>
                    </div>

                    {/* Holdings Table */}
                    <div>
                        <div className="flex items-center justify-between mb-3">
                            <h4 className="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase">Portfolio Holdings</h4>
                            <span className="text-xs text-gray-400">{assets.length} Assets</span>
                        </div>
                        <div className="border border-gray-200 dark:border-white/10 rounded-lg overflow-hidden">
                            <table className="w-full text-sm text-left">
                                <thead className="text-xs text-gray-500 dark:text-gray-400 uppercase bg-gray-50 dark:bg-white/5 border-b border-gray-200 dark:border-white/10">
                                    <tr>
                                        <th className="px-4 py-3">Ticker</th>
                                        <th className="px-4 py-3">Name</th>
                                        <th className="px-4 py-3 text-right">Qty</th>
                                        <th className="px-4 py-3 text-right">Price</th>
                                        <th className="px-4 py-3 text-right">Value</th>
                                        <th className="px-4 py-3 text-right">Allocation</th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-gray-100 dark:divide-white/5">
                                    {assets.map(asset => {
                                        const value = asset.currentPrice * asset.quantity;
                                        const allocation = totalValue > 0 ? (value / totalValue) * 100 : 0;
                                        return (
                                            <tr key={asset.id} className="hover:bg-gray-50 dark:hover:bg-white/5 transition-colors">
                                                <td className="px-4 py-3 font-medium text-gray-900 dark:text-white">{asset.ticker}</td>
                                                <td className="px-4 py-3 text-gray-600 dark:text-gray-400">{asset.name}</td>
                                                <td className="px-4 py-3 text-right font-mono text-gray-600 dark:text-gray-300">{asset.quantity}</td>
                                                <td className="px-4 py-3 text-right font-mono text-gray-600 dark:text-gray-300">${asset.currentPrice.toFixed(2)}</td>
                                                <td className="px-4 py-3 text-right font-mono font-medium text-gray-900 dark:text-white">
                                                    ${value.toLocaleString()}
                                                </td>
                                                <td className="px-4 py-3 text-right font-mono text-gray-500 dark:text-gray-400">
                                                    {allocation.toFixed(1)}%
                                                </td>
                                            </tr>
                                        );
                                    })}
                                </tbody>
                            </table>
                        </div>
                    </div>

                    {/* Rebalancing Recommendations */}
                    {categoryTrades.length > 0 ? (
                        <div>
                            <h4 className="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase mb-3 flex items-center gap-2">
                                <RefreshCw size={14} /> Recommended Actions
                            </h4>
                            <div className="bg-yellow-50 dark:bg-yellow-900/10 border border-yellow-100 dark:border-yellow-900/20 rounded-lg p-4">
                                <ul className="space-y-2">
                                    {categoryTrades.map((trade, idx) => (
                                        <li key={idx} className="flex items-center justify-between text-sm">
                                            <span className="flex items-center gap-2">
                                                <span className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase ${trade.action === 'BUY'
                                                    ? 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400'
                                                    : 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400'
                                                    }`}>
                                                    {trade.action}
                                                </span>
                                                <span className="font-medium text-gray-900 dark:text-white">{trade.ticker}</span>
                                            </span>
                                            <span className="font-mono text-gray-600 dark:text-gray-300">
                                                {trade.shares} shares (${trade.amount.toLocaleString()})
                                            </span>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        </div>
                    ) : (
                        <div className="p-4 bg-green-50 dark:bg-green-900/10 border border-green-100 dark:border-green-900/20 rounded-lg flex items-center justify-center gap-2 text-green-700 dark:text-green-400 text-sm">
                            <RefreshCw size={14} />
                            No rebalancing needed for {category}. Target allocation matched.
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};
