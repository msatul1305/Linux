import React, { useState, useEffect, useMemo } from 'react';
import { usePortfolio } from '../hooks/usePortfolio';
import { AssetInput } from './AssetInput';
import { RiskMetrics } from './RiskMetrics';
import { AssetClassDetails } from './AssetClassDetails';
import { RebalanceTable } from './RebalanceTable';
import { AllocationChart } from './AllocationChart';
import { calculatePortfolioVolatility, calculateSharpeRatio } from '../lib/financeLogic';
import { Sun, Moon, TrendingUp, Activity } from 'lucide-react';
import { AgentCouncil } from './AgentCouncil';
import { useAgents } from '../context/AgentContext';
import { Toaster, toast } from 'sonner';
import { Background } from './ui/Background';
import { Panel, Group as PanelGroup, Separator as PanelResizeHandle } from 'react-resizable-panels';
import { GlassCard } from './ui/GlassCard';

export const Dashboard: React.FC = () => {
    const {
        assets,
        totalValue,
        currentWeights,
        trades,
        updateAsset,
        addAsset,
        removeAsset,
        loadDemoData,
        executeRebalance
    } = usePortfolio();

    const { logs } = useAgents();

    const [volatility, setVolatility] = useState(0);
    const [sharpe, setSharpe] = useState(0);
    const [maxDrawdown] = useState(0.15);
    const [isDarkMode, setIsDarkMode] = useState(false);
    const [selectedCategory, setSelectedCategory] = useState<string | null>(null);

    // Theme Effect
    useEffect(() => {
        if (isDarkMode) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    }, [isDarkMode]);

    const toggleTheme = () => setIsDarkMode(!isDarkMode);

    const processedLogsRef = React.useRef<Set<string>>(new Set());

    // Auto-Pilot: Listen for Manager's decision
    useEffect(() => {
        if (logs.length === 0) return;
        const latestLog = logs[0];

        // Prevent processing the same log multiple times
        if (processedLogsRef.current.has(latestLog.id)) return;

        // Check if Manager (ID '4') decided to buy
        if (latestLog.agentId === '4' && latestLog.message.includes('Executing BUY orders')) {
            const tradeSummary = trades.length > 0
                ? trades.map(t => `${t.action} ${t.shares.toFixed(2)} ${t.ticker}`).join(', ')
                : 'No executable trades currently.';

            toast.message('Manager Requesting Approval', {
                description: `Authorized partial buy. Proposed Trades: ${tradeSummary}`,
                action: {
                    label: 'Approve',
                    onClick: () => {
                        executeRebalance();
                        toast.success('Trades Executed Successfully');
                    }
                },
                cancel: {
                    label: 'Deny',
                    onClick: () => toast.dismiss()
                },
                duration: 15000, // Extended time to read details
            });
            processedLogsRef.current.add(latestLog.id);
        }
        // Check if Manager decided to sell/risk-off
        if (latestLog.agentId === '4' && latestLog.message.includes('defensive positioning')) {
            const tradeSummary = trades.length > 0
                ? trades.map(t => `${t.action} ${t.shares.toFixed(2)} ${t.ticker}`).join(', ')
                : 'No executable trades currently.';

            toast.message('Manager Requesting Approval', {
                description: `Defensive move (Risk-Off). Proposed Trades: ${tradeSummary}`,
                action: {
                    label: 'Approve',
                    onClick: () => {
                        executeRebalance();
                        toast.success('De-Risking Complete');
                    }
                },
                cancel: {
                    label: 'Deny',
                    onClick: () => toast.dismiss()
                },
                duration: 15000,
            });
            processedLogsRef.current.add(latestLog.id);
        }
    }, [logs, executeRebalance, trades]);

    // Recalculate metrics when assets change
    useEffect(() => {
        if (totalValue > 0) {
            // Mock volatility for assets
            const assetsWithVol = assets.map(a => ({
                weight: (a.currentPrice * a.quantity) / totalValue || 0,
                volatility: a.category === 'Stock' ? 0.20 : a.category === 'Bond' ? 0.05 : 0.8
            }));

            const portVol = calculatePortfolioVolatility(assetsWithVol);
            setVolatility(portVol);

            // Assume 8% portfolio return and 2% risk free for Sharpe
            setSharpe(calculateSharpeRatio(0.08, 0.02, portVol));
        }
    }, [assets, totalValue]);

    // Filter assets for the selected category
    const selectedAssets = useMemo(() => {
        if (!selectedCategory) return [];
        return assets.filter(a => a.category === selectedCategory);
    }, [assets, selectedCategory]);

    // Live Heartbeat Simulation
    const [marketHeartbeat, setMarketHeartbeat] = useState({
        daily: 1.24,
        ytd: 8.56,
        alpha: 2.3
    });

    useEffect(() => {
        const interval = setInterval(() => {
            setMarketHeartbeat(prev => ({
                daily: prev.daily + (Math.random() - 0.5) * 0.05,
                ytd: prev.ytd + (Math.random() - 0.5) * 0.02,
                alpha: prev.alpha + (Math.random() - 0.5) * 0.01
            }));
        }, 3000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className={`min-h-screen font-sans text-gray-900 bg-gray-50 dark:bg-[#0a0a0a] transition-colors duration-500`}>
            {/* Background Effects */}
            <Background />

            {/* Header */}
            <header className="fixed top-0 inset-x-0 z-50 border-b border-gray-200 dark:border-white/10 bg-white/90 dark:bg-[#0a0a0a]/90 backdrop-blur-md transition-colors duration-300">
                <div className="max-w-[1600px] mx-auto px-6 h-16 flex items-center justify-between">
                    <div className="flex items-center gap-3">
                        <div className="w-8 h-8 rounded bg-gradient-to-br from-indigo-500 to-violet-600 flex items-center justify-center text-white font-bold shadow-lg shadow-indigo-500/20">
                            S
                        </div>
                        <h1 className="text-lg font-bold tracking-tight text-gray-900 dark:text-white">
                            SMART PORTFOLIO <span className="text-indigo-500 font-mono text-xs px-1.5 py-0.5 rounded bg-indigo-50 dark:bg-indigo-900/30 ml-1">INSTITUTIONAL</span>
                        </h1>
                    </div>
                    <div className="flex items-center gap-4">
                        <div className="hidden md:flex items-center gap-6 text-sm font-medium text-gray-500 dark:text-gray-400">
                            <span className="flex items-center gap-2">
                                <span className="w-2 h-2 rounded-full bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.5)] animate-pulse"></span>
                                MARKET OPEN
                            </span>
                            <span className="font-mono text-xs opacity-70">LATENCY: {Math.floor(Math.random() * 20) + 5}ms</span>
                        </div>
                        <div className="h-6 w-px bg-gray-200 dark:bg-white/10 mx-2"></div>
                        <button
                            onClick={toggleTheme}
                            className="p-1.5 bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 text-gray-500 dark:text-gray-400 rounded hover:bg-gray-200 dark:hover:bg-white/10 transition-colors"
                            title={isDarkMode ? "Switch to Day Mode" : "Switch to Night Mode"}
                        >
                            {isDarkMode ? <Sun size={14} /> : <Moon size={14} />}
                        </button>
                    </div>
                </div>
            </header>

            {/* Main Content */}
            <main className="max-w-[1600px] mx-auto pt-24 pb-12 px-6">

                {/* Live Ticker Widget */}
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
                    <GlassCard className="p-4 flex items-center justify-between">
                        <div>
                            <p className="text-xs text-gray-500 uppercase font-medium">Daily Return</p>
                            <p className={`text-xl font-mono ${marketHeartbeat.daily >= 0 ? 'text-emerald-500' : 'text-red-500'}`}>
                                {marketHeartbeat.daily >= 0 ? '+' : ''}{marketHeartbeat.daily.toFixed(2)}%
                            </p>
                        </div>
                        <TrendingUp className={`${marketHeartbeat.daily >= 0 ? 'text-emerald-500' : 'text-red-500'} opacity-50`} size={24} />
                    </GlassCard>
                    <GlassCard className="p-4 flex items-center justify-between">
                        <div>
                            <p className="text-xs text-gray-500 uppercase font-medium">YTD Return</p>
                            <p className="text-xl font-mono text-emerald-500">+{marketHeartbeat.ytd.toFixed(2)}%</p>
                        </div>
                        <Activity className="text-emerald-500 opacity-50" size={24} />
                    </GlassCard>
                    <GlassCard className="p-4 flex items-center justify-between">
                        <div>
                            <p className="text-xs text-gray-500 uppercase font-medium">Beta</p>
                            <p className="text-xl font-mono text-gray-900 dark:text-white">0.92</p>
                        </div>
                        <Activity className="text-indigo-500 opacity-50" size={24} />
                    </GlassCard>
                    <GlassCard className="p-4 flex items-center justify-between">
                        <div>
                            <p className="text-xs text-gray-500 uppercase font-medium">Alpha</p>
                            <p className={`text-xl font-mono ${marketHeartbeat.alpha >= 0 ? 'text-emerald-500' : 'text-red-500'}`}>
                                {marketHeartbeat.alpha >= 0 ? '+' : ''}{marketHeartbeat.alpha.toFixed(2)}%
                            </p>
                        </div>
                        <TrendingUp className="text-indigo-500 opacity-50" size={24} />
                    </GlassCard>
                </div>

                <div className="h-[calc(100vh-7rem)]">
                    <PanelGroup orientation="horizontal" id="dashboard-panels">
                        {/* Left Panel: Input and Risk */}
                        <Panel defaultSize={30} minSize={20}>
                            <div className="flex flex-col gap-6 h-full overflow-y-auto pr-2 custom-scrollbar">
                                <GlassCard className="flex-none">
                                    <div className="p-6">
                                        <AssetInput
                                            assets={assets}
                                            onUpdate={updateAsset}
                                            onRemove={removeAsset}
                                            onAdd={addAsset}
                                        />
                                        <div className="mt-6 pt-6 border-t border-gray-200 dark:border-white/10">
                                            <button
                                                onClick={loadDemoData}
                                                className="w-full py-2 bg-gray-100 dark:bg-white/5 hover:bg-gray-200 dark:hover:bg-white/10 text-gray-600 dark:text-gray-300 rounded text-xs font-mono uppercase tracking-wider transition-colors"
                                            >
                                                Load Demo Portfolio
                                            </button>
                                        </div>
                                    </div>
                                </GlassCard>

                                <div className="flex-none">
                                    <RiskMetrics
                                        volatility={volatility}
                                        sharpeRatio={sharpe}
                                        maxDrawdown={maxDrawdown}
                                    />
                                </div>
                            </div>
                        </Panel>

                        <PanelResizeHandle className="w-1.5 bg-gray-200 dark:bg-white/5 hover:bg-indigo-500 transition-colors mx-2 rounded-full cursor-col-resize" />

                        {/* Middle Panel: Allocation and Rebalance */}
                        <Panel defaultSize={40} minSize={30}>
                            <div className="flex flex-col gap-6 h-full px-2 overflow-y-auto custom-scrollbar">
                                <div className="flex-none h-[300px]">
                                    <AllocationChart assets={assets} onSelectCategory={setSelectedCategory} />
                                </div>
                                <div className="flex-1 min-h-[300px] bg-white dark:bg-[#111] rounded-xl border border-gray-200 dark:border-white/10 overflow-hidden flex flex-col">
                                    <RebalanceTable
                                        assets={assets}
                                        currentWeights={currentWeights}
                                        trades={trades}
                                    />
                                </div>
                            </div>
                        </Panel>

                        <PanelResizeHandle className="w-1.5 bg-gray-200 dark:bg-white/5 hover:bg-indigo-500 transition-colors mx-2 rounded-full cursor-col-resize" />

                        {/* Right Panel: Agent System */}
                        <Panel defaultSize={30} minSize={20}>
                            <div className="h-full pl-2">
                                <AgentCouncil />
                            </div>
                        </Panel>
                    </PanelGroup>
                </div>
            </main>

            {/* Drill Down Modal */}
            {selectedCategory && (
                <AssetClassDetails
                    category={selectedCategory}
                    assets={selectedAssets}
                    trades={trades}
                    onClose={() => setSelectedCategory(null)}
                />
            )}
            <Toaster position="top-right" theme="dark" richColors />
        </div>
    );
};
