import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { Asset } from '../types';

interface PortfolioState {
    assets: Asset[];
    cashBalance: number;
    // Actions
    setAssets: (assets: Asset[]) => void;
    updateAsset: (id: string, updates: Partial<Asset>) => void;
    addAsset: (asset: Asset) => void;
    removeAsset: (id: string) => void;
    setCashBalance: (amount: number) => void;
}

const INITIAL_ASSETS: Asset[] = [
    { id: '1', ticker: 'VTI', name: 'US Total Stock', currentPrice: 220.50, quantity: 10, targetWeight: 0.60, category: 'Stock' },
    { id: '2', ticker: 'BND', name: 'US Total Bond', currentPrice: 75.20, quantity: 40, targetWeight: 0.40, category: 'Bond' },
];

export const usePortfolioStore = create<PortfolioState>()(
    persist(
        (set) => ({
            assets: INITIAL_ASSETS,
            cashBalance: 0,
            setAssets: (assets) => set({ assets }),
            updateAsset: (id, updates) => set((state) => ({
                assets: state.assets.map(a => a.id === id ? { ...a, ...updates } : a)
            })),
            addAsset: (asset) => set((state) => ({
                assets: [...state.assets, asset]
            })),
            removeAsset: (id) => set((state) => ({
                assets: state.assets.filter(a => a.id !== id)
            })),
            setCashBalance: (amount) => set({ cashBalance: amount }),
        }),
        {
            name: 'portfolio-storage', // unique name
        }
    )
);
