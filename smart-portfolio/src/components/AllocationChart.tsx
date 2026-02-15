import React, { useMemo } from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from 'recharts';
import type { Asset } from '../types';

interface AllocationChartProps {
    assets: Asset[];
    onSelectCategory: (category: string) => void;
}

const COLORS = {
    'Stock': '#6366f1', // Indigo
    'Bond': '#10b981', // Emerald
    'Cash': '#94a3b8', // Slate
    'Crypto': '#f59e0b', // Amber
    'ETF': '#8b5cf6', // Violet
    'Mutual Fund': '#ec4899', // Pink
    'Commodity': '#eab308', // Yellow
    'FX': '#3b82f6', // Blue
    'Other': '#64748b' // Gray
};

export const AllocationChart: React.FC<AllocationChartProps> = ({ assets, onSelectCategory }) => {
    const data = useMemo(() => {
        const categoryMap = new Map<string, number>();

        assets.forEach(asset => {
            const currentVal = asset.currentPrice * asset.quantity;
            if (currentVal > 0) {
                categoryMap.set(asset.category, (categoryMap.get(asset.category) || 0) + currentVal);
            }
        });

        return Array.from(categoryMap.entries()).map(([name, value]) => ({
            name,
            value,
            displayValue: `$${value.toLocaleString(undefined, { maximumFractionDigits: 0 })}`
        })).sort((a, b) => b.value - a.value);
    }, [assets]);

    return (
        <div className="bg-white dark:bg-[#111] p-6 rounded-xl shadow-sm border border-gray-200 dark:border-white/10 h-full flex flex-col transition-colors duration-300">
            <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">Asset Class Allocation</h2>
            <div className="flex-1 min-h-[300px]">
                <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                        <Pie
                            data={data}
                            cx="50%"
                            cy="50%"
                            innerRadius={60}
                            outerRadius={100}
                            paddingAngle={5}
                            dataKey="value"
                            cursor="pointer"
                            onClick={(data) => onSelectCategory(data.name)}
                        >
                            {data.map((entry, index) => (
                                <Cell
                                    key={`cell-${index}`}
                                    fill={COLORS[entry.name as keyof typeof COLORS] || COLORS['Other']}
                                    className="stroke-white dark:stroke-[#111] stroke-2 outline-none hover:opacity-80 transition-opacity"
                                />
                            ))}
                        </Pie>
                        <Tooltip
                            formatter={(value: any) => [`$${(value || 0).toLocaleString()}`, 'Value']}
                            contentStyle={{
                                backgroundColor: 'rgba(255, 255, 255, 0.9)',
                                borderRadius: '8px',
                                border: 'none',
                                boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)',
                                color: '#333'
                            }}
                            itemStyle={{ color: '#333' }}
                        />
                        <Legend
                            verticalAlign="bottom"
                            height={36}
                            iconType="circle"
                            formatter={(value) => <span className="text-gray-600 dark:text-gray-300 ml-1">{value}</span>}
                        />
                    </PieChart>
                </ResponsiveContainer>
            </div>
            <p className="text-center text-xs text-gray-400 mt-2">Click segments for details</p>
        </div>
    );
};
