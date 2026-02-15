
/**
 * Calculates the portfolio drift between current and target weights.
 * Returns a map of ticker -> drift percentage (absolute difference).
 */
export const calculateDrift = (
    assets: { ticker: string; currentWeight: number; targetWeight: number }[]
): Record<string, number> => {
    const drift: Record<string, number> = {};
    assets.forEach((asset) => {
        drift[asset.ticker] = Math.abs(asset.currentWeight - asset.targetWeight);
    });
    return drift;
};

/**
 * Calculates the standard deviation (volatility) of a portfolio based on asset weights and individual volatilities.
 * Simplified for MVP: Assumes correlation of 0 between all assets (naive).
 * In a real app, we'd need a covariance matrix.
 */
export const calculatePortfolioVolatility = (
    assets: { weight: number; volatility: number }[]
): number => {
    // Variance of portfolio = sum (weight^2 * volatility^2) assuming 0 correlation
    let variance = 0;
    assets.forEach((asset) => {
        variance += (asset.weight * asset.volatility) ** 2;
    });
    return Math.sqrt(variance);
};

/**
 * Calculates the Sharpe Ratio of the portfolio.
 * (Portfolio Return - Risk Free Rate) / Portfolio Volatility
 */
export const calculateSharpeRatio = (
    portfolioReturn: number,
    riskFreeRate: number,
    portfolioVolatility: number
): number => {
    if (portfolioVolatility === 0) return 0;
    return (portfolioReturn - riskFreeRate) / portfolioVolatility;
};

/**
 * Calculates the recommended trade amount to rebalance an asset.
 * Positive = Buy, Negative = Sell
 */
export const calculateRebalanceTrade = (
    currentValue: number,
    targetWeight: number,
    totalPortfolioValue: number
): number => {
    const targetValue = totalPortfolioValue * targetWeight;
    return targetValue - currentValue;
};
