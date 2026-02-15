import React from 'react';
import type { Asset } from '../types';
import { Trash2, Plus } from 'lucide-react';

interface AssetInputProps {
    assets: Asset[];
    onUpdate: (id: string, updates: Partial<Asset>) => void;
    onRemove: (id: string) => void;
    onAdd: (asset: Asset) => void;
}

export const AssetInput: React.FC<AssetInputProps> = ({ assets, onUpdate, onRemove, onAdd }) => {
    return (
        <div>
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-bold text-gray-900 dark:text-white">Portfolio Assets</h3>
                <button
                    onClick={() => onAdd({
                        id: Date.now().toString(),
                        name: 'New Asset',
                        quantity: 0,
                        currentPrice: 100,
                        category: 'Stock',
                        targetWeight: 0,
                        ticker: 'NEW'
                    })}
                    className="flex items-center gap-2 px-3 py-1.5 bg-indigo-50 dark:bg-indigo-600 text-indigo-600 dark:text-white rounded-md text-sm font-medium hover:bg-indigo-100 dark:hover:bg-indigo-700 transition-colors"
                >
                    <Plus size={16} /> Add Asset
                </button>
            </div>

            {/* Header Row */}
            <div className="grid grid-cols-[repeat(15,minmax(0,1fr))] gap-2 px-2.5 mb-2 text-[10px] font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                <div className="col-span-5 pl-1">Asset / Class</div>
                <div className="col-span-3 text-right pr-2">Qty</div>
                <div className="col-span-3 text-right pr-2">Price</div>
                <div className="col-span-3 text-right pr-4">Target %</div>
                <div className="col-span-1"></div>
            </div>

            <div className="space-y-2 max-h-[calc(100vh-16rem)] overflow-y-auto pr-1 custom-scrollbar">
                {assets.map((asset) => (
                    <div key={asset.id} className="group grid grid-cols-[repeat(15,minmax(0,1fr))] gap-2 items-center p-2 rounded-lg bg-gray-50 dark:bg-white/5 border border-gray-200 dark:border-white/5 hover:border-indigo-500/50 transition-all">
                        <div className="col-span-5">
                            <input
                                type="text"
                                value={asset.name}
                                onChange={(e) => onUpdate(asset.id, { name: e.target.value })}
                                className="w-full bg-transparent text-gray-900 dark:text-white font-medium text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500 rounded px-1 -ml-1 truncate placeholder-gray-400"
                                placeholder="Asset Name"
                                title={asset.name}
                            />
                            <select
                                value={asset.category}
                                onChange={(e) => onUpdate(asset.id, { category: e.target.value as any })}
                                className="w-full bg-transparent text-[10px] text-gray-500 dark:text-gray-400 focus:outline-none -ml-1 truncate cursor-pointer hover:text-indigo-500 transition-colors"
                                title={asset.category}
                            >
                                <option value="Stock">Stock</option>
                                <option value="ETF">ETF</option>
                                <option value="Mutual Fund">Mutual Fund</option>
                                <option value="Bond">Bond</option>
                                <option value="Crypto">Crypto</option>
                                <option value="FX">FX</option>
                                <option value="Commodity">Commodity</option>
                                <option value="Cash">Cash</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>
                        <div className="col-span-3">
                            <input
                                type="number"
                                value={asset.quantity}
                                onChange={(e) => onUpdate(asset.id, { quantity: Number(e.target.value) })}
                                className="w-full bg-white dark:bg-black/20 border border-gray-200 dark:border-white/10 rounded px-1.5 py-1 text-sm text-gray-900 dark:text-gray-200 font-mono focus:border-indigo-500 focus:outline-none text-right"
                            />
                        </div>
                        <div className="col-span-3">
                            <div className="relative">
                                <span className="absolute left-1.5 top-1 text-gray-400 text-xs">$</span>
                                <input
                                    type="number"
                                    value={asset.currentPrice}
                                    onChange={(e) => onUpdate(asset.id, { currentPrice: Number(e.target.value) })}
                                    className="w-full bg-white dark:bg-black/20 border border-gray-200 dark:border-white/10 rounded pl-4 pr-1.5 py-1 text-sm text-gray-900 dark:text-gray-200 font-mono focus:border-indigo-500 focus:outline-none text-right"
                                />
                            </div>
                        </div>
                        <div className="col-span-3">
                            <div className="relative">
                                <input
                                    type="number"
                                    value={asset.targetWeight * 100}
                                    onChange={(e) => onUpdate(asset.id, { targetWeight: Number(e.target.value) / 100 })}
                                    className="w-full bg-white dark:bg-black/20 border border-gray-200 dark:border-white/10 rounded px-1.5 py-1 text-sm text-gray-900 dark:text-gray-200 font-mono focus:border-indigo-500 focus:outline-none text-right"
                                />
                                <span className="absolute right-4 top-1 text-gray-400 text-xs opacity-0 group-hover:opacity-100 transition-opacity">%</span>
                            </div>
                        </div>
                        <div className="col-span-1 flex justify-end">
                            <button
                                onClick={() => onRemove(asset.id)}
                                className="p-1.5 text-gray-400 dark:text-gray-500 hover:text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded transition-colors opacity-0 group-hover:opacity-100"
                            >
                                <Trash2 size={14} />
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};
