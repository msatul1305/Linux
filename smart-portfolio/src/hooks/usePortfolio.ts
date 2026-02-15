import { useMemo, useCallback } from 'react';
import { calculateDrift, calculateRebalanceTrade } from '../lib/financeLogic';
import { usePortfolioStore } from '../store/portfolioStore';

export const usePortfolio = () => {
    // Select state and actions from Zustand store
    const { assets, cashBalance, updateAsset, addAsset, removeAsset, setCashBalance, setAssets } = usePortfolioStore();

    const totalValue = useMemo(() => {
        const assetsValue = assets.reduce((sum, asset) => sum + (asset.currentPrice * asset.quantity), 0);
        return assetsValue + cashBalance;
    }, [assets, cashBalance]);

    const currentWeights = useMemo(() => {
        if (totalValue === 0) return {};
        const weights: Record<string, number> = {};
        assets.forEach(asset => {
            weights[asset.ticker] = (asset.currentPrice * asset.quantity) / totalValue;
        });
        return weights;
    }, [assets, totalValue]);

    const drift = useMemo(() => {
        return calculateDrift(assets.map(a => ({
            ticker: a.ticker,
            currentWeight: currentWeights[a.ticker] || 0,
            targetWeight: a.targetWeight
        })));
    }, [assets, currentWeights]);

    const trades = useMemo(() => {
        return assets.map(asset => {
            const currentVal = asset.currentPrice * asset.quantity;
            const tradeAmount = calculateRebalanceTrade(currentVal, asset.targetWeight, totalValue);
            return {
                ticker: asset.ticker,
                action: tradeAmount > 0 ? 'BUY' : 'SELL',
                amount: Math.abs(tradeAmount),
                shares: Math.abs(tradeAmount / asset.currentPrice)
            };
        }).filter(t => t.amount > 1);
    }, [assets, totalValue]);

    const executeRebalance = useCallback(() => {
        const newAssets = assets.map(asset => {
            const trade = trades.find(t => t.ticker === asset.ticker);
            if (trade) {
                const newQuantity = trade.action === 'BUY'
                    ? asset.quantity + trade.shares
                    : asset.quantity - trade.shares;
                return { ...asset, quantity: newQuantity };
            }
            return asset;
        });
        setAssets(newAssets);
    }, [assets, trades, setAssets]);

    const loadDemoData = useCallback(() => {
        setAssets([
            { id: '1', ticker: 'SPY', name: 'S&P 500 ETF', currentPrice: 500.25, quantity: 15, targetWeight: 0.40, category: 'Stock' },
            { id: '2', ticker: 'QQQ', name: 'Nasdaq 100 ETF', currentPrice: 430.10, quantity: 10, targetWeight: 0.30, category: 'Stock' },
            { id: '3', ticker: 'BND', name: 'Total Bond Market', currentPrice: 72.50, quantity: 50, targetWeight: 0.20, category: 'Bond' },
            { id: '4', ticker: 'GLD', name: 'Gold Trust', currentPrice: 200.80, quantity: 5, targetWeight: 0.05, category: 'Other' },
            { id: '5', ticker: 'BTC', name: 'Bitcoin', currentPrice: 65000.00, quantity: 0.02, targetWeight: 0.05, category: 'Crypto' },
        ]);
    }, [setAssets]);

    return {
        assets,
        totalValue,
        cashBalance,
        currentWeights,
        drift,
        trades,
        updateAsset,
        addAsset,
        removeAsset,
        setCashBalance,
        loadDemoData,
        executeRebalance
    };
};
