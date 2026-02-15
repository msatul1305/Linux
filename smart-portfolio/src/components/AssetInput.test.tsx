import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { AssetInput } from '../components/AssetInput';
import type { Asset } from '../types';

describe('AssetInput Component', () => {
    const mockAssets: Asset[] = [
        {
            id: '1',
            name: 'Apple',
            ticker: 'AAPL',
            quantity: 10,
            currentPrice: 150,
            targetWeight: 0.5,
            category: 'Stock'
        }
    ];

    const mockOnUpdate = vi.fn();
    const mockOnRemove = vi.fn();
    const mockOnAdd = vi.fn();

    it('renders asset input fields correctly', () => {
        render(
            <AssetInput
                assets={mockAssets}
                onUpdate={mockOnUpdate}
                onRemove={mockOnRemove}
                onAdd={mockOnAdd}
            />
        );

        expect(screen.getByDisplayValue('Apple')).toBeInTheDocument();
        expect(screen.getByDisplayValue('10')).toBeInTheDocument();
        expect(screen.getByDisplayValue('150')).toBeInTheDocument();
        // Target weight is displayed as percentage (0.5 * 100 = 50)
        expect(screen.getByDisplayValue('50')).toBeInTheDocument();
    });

    it('calls onUpdate when fields are changed', () => {
        render(
            <AssetInput
                assets={mockAssets}
                onUpdate={mockOnUpdate}
                onRemove={mockOnRemove}
                onAdd={mockOnAdd}
            />
        );

        const nameInput = screen.getByDisplayValue('Apple');
        fireEvent.change(nameInput, { target: { value: 'Apple Inc' } });
        expect(mockOnUpdate).toHaveBeenCalledWith('1', { name: 'Apple Inc' });

        const qtyInput = screen.getByDisplayValue('10');
        fireEvent.change(qtyInput, { target: { value: '20' } });
        expect(mockOnUpdate).toHaveBeenCalledWith('1', { quantity: 20 });
    });

    it('calls onRemove when delete button is clicked', () => {
        render(
            <AssetInput
                assets={mockAssets}
                onUpdate={mockOnUpdate}
                onRemove={mockOnRemove}
                onAdd={mockOnAdd}
            />
        );

        // Find the delete button (it has a Trash icon, but might be hard to select by icon alone if no aria-label. 
        // The component has a button with onClick => onRemove. 
        // Let's assume it's the only button in the row or select by role)
        const buttons = screen.getAllByRole('button');
        // First button is "Add Asset", second is "Remove" (inside the map)
        const removeButton = buttons[1];

        fireEvent.click(removeButton);
        expect(mockOnRemove).toHaveBeenCalledWith('1');
    });

    it('calls onAdd when Add Asset button is clicked', () => {
        render(
            <AssetInput
                assets={mockAssets}
                onUpdate={mockOnUpdate}
                onRemove={mockOnRemove}
                onAdd={mockOnAdd}
            />
        );

        const addButton = screen.getByText(/Add Asset/i);
        fireEvent.click(addButton);
        expect(mockOnAdd).toHaveBeenCalled();
    });
});
