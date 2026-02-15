import React, { createContext, useContext, useState, useEffect, useCallback } from 'react';
import type { Agent, AgentLog, AgentEvent, EventType } from '../types/agents';
import { processAgentReaction, delay } from '../lib/agentEngine';

const INITIAL_AGENTS: Agent[] = [
    { id: '1', name: 'Dr. Sentiment', role: 'Analyst', status: 'idle', avatar: '📰', personality: 'Excited about news' },
    { id: '2', name: 'Quantos', role: 'Quant', status: 'idle', avatar: '📈', personality: 'Data-driven, cold' },
    { id: '3', name: 'Guardian', role: 'Risk', status: 'idle', avatar: '🛡️', personality: 'Cautious, pessimistic' },
    { id: '4', name: 'Boss', role: 'Manager', status: 'idle', avatar: '⚖️', personality: 'Decisive' },
];

const AgentContext = createContext<any>(null);

export const AgentProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [agents, setAgents] = useState<Agent[]>(INITIAL_AGENTS);
    const [logs, setLogs] = useState<AgentLog[]>([]);
    const [events, setEvents] = useState<AgentEvent[]>([]);
    const [isSimulating, setIsSimulating] = useState(false);

    // 1. Event Emitter
    const emit = useCallback((type: EventType, payload: any) => {
        const event: AgentEvent = { type, payload, timestamp: Date.now() };
        setEvents(prev => [...prev, event]);
    }, []);

    // 2. Event Listener (The "Brain" Loop)
    useEffect(() => {
        if (events.length === 0) return;

        const latestEvent = events[events.length - 1];

        // Each agent processes the event
        agents.forEach(async (agent) => {
            // Add a small random delay for realism
            await delay(Math.random() * 1500 + 500);

            const reaction = processAgentReaction(agent, latestEvent);
            if (reaction) {
                addLog(agent.id, reaction.message!, reaction.sentiment);

                // If Manager votes, we might trigger a new event (e.g., TRADE_EXECUTED)
                // For MVP, we just log it.
            }
        });

    }, [events]);

    const addLog = useCallback((agentId: string, message: string, sentiment: 'positive' | 'negative' | 'neutral' = 'neutral') => {
        const newLog: AgentLog = {
            id: Math.random().toString(36).substr(2, 9),
            agentId,
            timestamp: Date.now(),
            message,
            sentiment
        };
        setLogs(prev => [newLog, ...prev].slice(0, 50));

        setAgents(prev => prev.map(a => a.id === agentId ? { ...a, status: 'speaking' } : a));
        setTimeout(() => {
            setAgents(prev => prev.map(a => a.id === agentId ? { ...a, status: 'idle' } : a));
        }, 3000);
    }, []);

    // 3. Simulation Orchestrator (The "Director")
    useEffect(() => {
        let timeout: any;

        const runScenario = async () => {
            // Step 1: Analyst spots news
            addLog('1', "BREAKING: Tech sector earnings are beating expectations by 20%! This is a massive signal.", 'positive');
            setAgents(prev => prev.map(a => a.id === '1' ? { ...a, status: 'speaking' } : a));
            await delay(3000);
            setAgents(prev => prev.map(a => a.id === '1' ? { ...a, status: 'idle' } : a));

            // Step 2: Quant analyzes data
            addLog('2', "Processing... Correlation matrices updated. Momentum indicators for Tech are showing 3-sigma divergence. Calculating optimal entry...", 'neutral');
            setAgents(prev => prev.map(a => a.id === '2' ? { ...a, status: 'speaking' } : a));
            await delay(3000);
            setAgents(prev => prev.map(a => a.id === '2' ? { ...a, status: 'idle' } : a));

            // Step 3: Risk Manager intervenes
            addLog('3', "Hold on. Volatility is elevated. I'm seeing a potential bull trap. We need to cap our exposure to 15% max to stay within VaR limits.", 'negative');
            setAgents(prev => prev.map(a => a.id === '3' ? { ...a, status: 'speaking' } : a));
            await delay(3000);
            setAgents(prev => prev.map(a => a.id === '3' ? { ...a, status: 'idle' } : a));

            // Step 4: Manager makes call
            addLog('4', "Acknowledged. Dr. Sentiment is bullish, but Guardian is right about the risk. I'm authorizing a partial buy. Executing BUY orders for Tech, but hedging with Bonds.", 'neutral');
            setAgents(prev => prev.map(a => a.id === '4' ? { ...a, status: 'speaking' } : a));
            emit('CONSENSUS_REACHED', { decision: 'BUY_HEDGE' });
            await delay(3000);
            setAgents(prev => prev.map(a => a.id === '4' ? { ...a, status: 'idle' } : a));

            setIsSimulating(false);
        };

        if (isSimulating) {
            runScenario();
        }

        return () => clearTimeout(timeout);
    }, [isSimulating, emit]);

    const startSimulation = useCallback(() => {
        setLogs([]);
        setEvents([]);
        setIsSimulating(true);
    }, []);

    const stopSimulation = useCallback(() => setIsSimulating(false), []);

    return (
        <AgentContext.Provider value={{ agents, logs, isSimulating, startSimulation, stopSimulation }}>
            {children}
        </AgentContext.Provider>
    );
};

export const useAgents = () => useContext(AgentContext);
