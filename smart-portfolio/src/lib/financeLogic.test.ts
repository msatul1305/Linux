import { describe, it, expect } from 'vitest';
import { calculateDrift, calculatePortfolioVolatility, calculateSharpeRatio, calculateRebalanceTrade } from './financeLogic';

describe('Finance Logic', () => {
    it('calculates drift correctly', () => {
        const assets = [
            { ticker: 'A', currentWeight: 0.5, targetWeight: 0.6 },
            { ticker: 'B', currentWeight: 0.5, targetWeight: 0.4 },
        ];
        const drift = calculateDrift(assets);
        expect(drift['A']).toBeCloseTo(0.1);
        expect(drift['B']).toBeCloseTo(0.1);
    });

    it('calculates portfolio volatility correctly (uncorrelated)', () => {
        const assets = [
            { weight: 0.5, volatility: 0.2 },
            { weight: 0.5, volatility: 0.2 },
        ];
        // Variance = (0.5*0.2)^2 + (0.5*0.2)^2 = 0.01 + 0.01 = 0.02
        // Volatility = sqrt(0.02) ≈ 0.1414
        const vol = calculatePortfolioVolatility(assets);
        expect(vol).toBeCloseTo(0.1414);
    });

    it('calculates Sharpe ratio correctly', () => {
        // Return 8%, Risk Free 2%, Volatility 10%
        // (0.08 - 0.02) / 0.10 = 0.6
        const sharpe = calculateSharpeRatio(0.08, 0.02, 0.10);
        expect(sharpe).toBeCloseTo(0.6);
    });

    it('calculates rebalance trade amount correctly', () => {
        // Total Portfolio: $10,000
        // Asset A: Current Value $4,000
        // Target Weight: 0.5 (50%) -> Target Value $5,000
        // Trade: Buy $1,000
        const trade = calculateRebalanceTrade(4000, 0.5, 10000);
        expect(trade).toBe(1000);

        // Asset B: Current Value $6,000
        // Target Weight: 0.5 (50%) -> Target Value $5,000
        // Trade: Sell $1,000 (-1000)
        const tradeSell = calculateRebalanceTrade(6000, 0.5, 10000);
        expect(tradeSell).toBe(-1000);
    });
});
