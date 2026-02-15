export type AgentRole = 'Analyst' | 'Quant' | 'Risk' | 'Manager';

export interface Agent {
    id: string;
    name: string;
    role: AgentRole;
    status: 'idle' | 'thinking' | 'speaking' | 'voting';
    avatar: string; // Emoji or URL
    personality: string;
}

export interface AgentLog {
    id: string;
    agentId: string;
    timestamp: number;
    message: string;
    sentiment?: 'positive' | 'negative' | 'neutral';
    vote?: 'buy' | 'sell' | 'hold';
}

export type EventType = 'MARKET_UPDATE' | 'NEWS_FLASH' | 'VOLATILITY_SPIKE' | 'CONSENSUS_REACHED';

export interface AgentEvent {
    type: EventType;
    payload: any;
    timestamp: number;
}

export interface AgentContextState {
    agents: Agent[];
    logs: AgentLog[];
    isSimulating: boolean;
    startSimulation: (scenario: string) => void;
    stopSimulation: () => void;
}
