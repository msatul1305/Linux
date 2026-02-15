import type { Agent, AgentLog, AgentEvent } from '../types/agents';

// Helper to generate a delay
export const delay = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

// The "Brain" of each agent
export const processAgentReaction = (agent: Agent, event: AgentEvent): Partial<AgentLog> | null => {

    // Analyst reacts to News
    if (agent.role === 'Analyst' && event.type === 'NEWS_FLASH') {
        const sentiment = event.payload.sentiment > 0.5 ? 'positive' : 'negative';
        return {
            message: `Analyzing news: "${event.payload.headline}". Sentiment scrore: ${event.payload.sentiment}. Outlook: ${sentiment.toUpperCase()}.`,
            sentiment: sentiment,
            vote: sentiment === 'positive' ? 'buy' : 'sell'
        };
    }

    // Quant reacts to Market Updates
    if (agent.role === 'Quant' && event.type === 'MARKET_UPDATE') {
        const trend = event.payload.trend; // 'up' | 'down' | 'flat'
        if (trend === 'up') {
            return {
                message: "Technical indicators align. Moving averages suggest strong accumulation.",
                sentiment: 'positive',
                vote: 'buy'
            };
        } else if (trend === 'down') {
            return {
                message: "Bearish divergence detected. Momentum is fading fast.",
                sentiment: 'negative',
                vote: 'sell'
            };
        }
    }

    // Risk Guardian reacts to Volatility
    if (agent.role === 'Risk' && event.type === 'VOLATILITY_SPIKE') {
        return {
            message: `⚠️ CRITICAL: Volatility spike detected (${event.payload.level}%). Breaching safety thresholds! Recommendation: DE-RISK IMMEDIATELY.`,
            sentiment: 'negative',
            vote: 'sell'
        };
    }

    // Manager makes the final call
    if (agent.role === 'Manager' && event.type === 'CONSENSUS_REACHED') {
        const votes = event.payload.votes; // ['buy', 'buy', 'sell']..
        const buyCount = votes.filter((v: string) => v === 'buy').length;
        const sellCount = votes.filter((v: string) => v === 'sell').length;

        if (buyCount > sellCount) {
            return {
                message: `Consensus is BULLISH (${buyCount} vs ${sellCount}). Executing BUY orders across the board.`,
                sentiment: 'positive',
                vote: 'buy'
            };
        } else {
            return {
                message: `Consensus is BEARISH (${sellCount} vs ${buyCount}). We are taking chips off the table. Defensive positioning engaged.`,
                sentiment: 'negative',
                vote: 'sell'
            };
        }
    }

    return null;
};
