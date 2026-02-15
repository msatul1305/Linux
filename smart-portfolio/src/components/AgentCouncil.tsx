import React, { useEffect, useRef } from 'react';
import { useAgents } from '../context/AgentContext';
import { useVoiceCommands } from '../hooks/useVoiceCommands';
import { usePortfolio } from '../hooks/usePortfolio';
import type { Agent, AgentLog } from '../types/agents';

export const AgentCouncil: React.FC = () => {
    const { agents, logs, isSimulating, startSimulation, stopSimulation } = useAgents();
    const { loadDemoData } = usePortfolio();
    const logsEndRef = useRef<HTMLDivElement>(null);

    const commands = React.useMemo(() => [
        { phrase: 'start analysis', action: startSimulation },
        { phrase: 'stop analysis', action: stopSimulation },
        { phrase: 'load demo', action: loadDemoData },
        { phrase: 'risk check', action: () => console.log('Risk check triggered via voice') }
    ], [startSimulation, stopSimulation, loadDemoData]);

    const { isListening, toggleListening, transcript, support } = useVoiceCommands(commands);

    useEffect(() => {
        logsEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [logs]);

    return (
        <div className="flex flex-col h-full border border-gray-200 dark:border-white/10 bg-white dark:bg-[#111] rounded-lg overflow-hidden font-mono text-sm transition-colors duration-300">
            {/* Toolbar */}
            <div className="flex items-center justify-between p-3 bg-gray-50 dark:bg-[#1a1a1a] border-b border-gray-200 dark:border-white/10">
                <div className="flex items-center gap-4">
                    <h3 className="font-semibold text-gray-700 dark:text-gray-200 uppercase tracking-widest text-xs">System Intelligence</h3>
                    {isSimulating && <span className="flex items-center gap-2 text-[10px] text-green-600 dark:text-green-500 animate-pulse">● PROCESSING LIVE DATA</span>}
                </div>

                <div className="flex gap-2">
                    <button
                        onClick={isSimulating ? stopSimulation : startSimulation}
                        className={`px-3 py-1 text-[10px] uppercase tracking-wider border transition-colors
                        ${isSimulating
                                ? 'border-red-500 text-red-600 dark:text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20'
                                : 'border-green-600 dark:border-green-900 text-green-700 dark:text-green-500 hover:bg-green-50 dark:hover:bg-green-900/20'}`}
                    >
                        {isSimulating ? '[HALT]' : '[EXECUTE ANALYSIS]'}
                    </button>
                    {support && (
                        <button
                            onClick={toggleListening}
                            className={`px-3 py-1 text-[10px] uppercase tracking-wider border transition-colors
                            ${isListening ? 'border-red-500 text-red-600 animate-pulse' : 'border-gray-300 dark:border-gray-700 text-gray-600 dark:text-gray-500 hover:border-gray-500'}`}
                        >
                            {isListening ? '[REC]' : '[VOICE]'}
                        </button>
                    )}
                </div>
            </div>

            <div className="flex flex-1 overflow-hidden">
                {/* Agent Status Panel (Sidebar) */}
                <div className="w-48 bg-gray-50 dark:bg-[#0a0a0a] border-r border-gray-200 dark:border-white/10 p-4 space-y-4 transition-colors duration-300">
                    <p className="text-[10px] text-gray-500 dark:text-gray-600 uppercase mb-2">Active Nodes</p>
                    {agents.map((agent: Agent) => (
                        <div key={agent.id} className="flex items-center justify-between py-2 border-b border-gray-200 dark:border-white/5 last:border-0">
                            <div>
                                <div className={`text-xs font-medium ${agent.status === 'speaking' ? 'text-black dark:text-white' : 'text-gray-500'}`}>
                                    {agent.name}
                                </div>
                                <div className="text-[9px] text-gray-400 dark:text-gray-600">{agent.role}</div>
                            </div>
                            <div className={`w-1.5 h-1.5 rounded-full ${agent.status === 'speaking' ? 'bg-green-500' : 'bg-gray-300 dark:bg-gray-800'}`} />
                        </div>
                    ))}
                </div>

                {/* Terminal Output */}
                <div className="flex-1 bg-white dark:bg-black flex flex-col relative transition-colors duration-300">
                    <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-green-500/20 to-transparent opacity-20" />

                    <div className="flex-1 overflow-y-auto p-4 space-y-1 font-mono text-xs">
                        {/* Transcript Overlay (In-line) */}
                        {transcript && (
                            <div className="mb-4 p-2 border border-dashed border-gray-300 dark:border-gray-700 text-gray-500 dark:text-gray-400">
                                {'>'} SPEECH_INPUT: "{transcript}"
                            </div>
                        )}

                        {logs.length === 0 && (
                            <div className="text-gray-400 dark:text-gray-700 mt-10 text-center">
                                // AWAITING COMMAND_
                            </div>
                        )}

                        {logs.map((log: AgentLog) => (
                            <div key={log.id} className="grid grid-cols-[80px_100px_1fr] gap-2 hover:bg-gray-50 dark:hover:bg-white/5 p-1 transition-colors">
                                <span className="text-gray-500 dark:text-gray-600">
                                    {new Date(log.timestamp).toLocaleTimeString([], { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' })}
                                </span>
                                <span className={`${log.agentId === '1' ? 'text-blue-600 dark:text-blue-400' :
                                    log.agentId === '2' ? 'text-cyan-600 dark:text-cyan-400' :
                                        log.agentId === '3' ? 'text-orange-600 dark:text-orange-400' : 'text-purple-600 dark:text-purple-400'
                                    }`}>
                                    [{agents.find((a: Agent) => a.id === log.agentId)?.name || 'UNKNOWN'}]
                                </span>
                                <span className={`text-gray-800 dark:text-gray-300 ${log.sentiment === 'positive' ? 'text-green-600 dark:text-green-400/90' : log.sentiment === 'negative' ? 'text-red-600 dark:text-red-400/90' : ''}`}>
                                    {log.message}
                                </span>
                            </div>
                        ))}
                        <div ref={logsEndRef} />
                    </div>
                </div>
            </div>
        </div>
    );
};
