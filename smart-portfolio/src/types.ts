export type AssetCategory = 'Stock' | 'Bond' | 'Cash' | 'Crypto' | 'ETF' | 'Mutual Fund' | 'Commodity' | 'FX' | 'Other';

export interface Asset {
    id: string;
    ticker: string;
    name: string;
    currentPrice: number;
    quantity: number;
    targetWeight: number; // 0.0 to 1.0 (e.g., 0.5 for 50%)
    category: AssetCategory;
}

export interface PortfolioState {
    assets: Asset[];
    totalValue: number;
    cashBalance: number;
}

export interface MarketData {
    ticker: string;
    price: number;
    change24h: number; // Percentage
    volatility: number; // Annualized volatility
}
