import { useState, useEffect, useCallback } from 'react';

interface VoiceCommand {
    phrase: string;
    action: () => void;
}

export const useVoiceCommands = (commands: VoiceCommand[]) => {
    const [isListening, setIsListening] = useState(false);
    const [transcript, setTranscript] = useState('');
    const [support, setSupport] = useState(true);

    useEffect(() => {
        if (!('webkitSpeechRecognition' in window)) {
            setSupport(false);
            return;
        }

        // @ts-ignore
        const recognition = new window.webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;
        recognition.lang = 'en-US';

        recognition.onstart = () => setIsListening(true);
        recognition.onend = () => setIsListening(false);

        recognition.onresult = (event: any) => {
            const current = event.resultIndex;
            const transcriptText = event.results[current][0].transcript.toLowerCase();
            setTranscript(transcriptText);

            // Check for commands
            commands.forEach(cmd => {
                if (transcriptText.includes(cmd.phrase.toLowerCase())) {
                    cmd.action();
                    setTranscript(''); // Reset after match
                }
            });
        };

        if (isListening) {
            recognition.start();
        } else {
            recognition.stop();
        }

        return () => {
            recognition.stop();
        };
    }, [isListening, commands]);

    const toggleListening = useCallback(() => setIsListening(prev => !prev), []);

    return { isListening, toggleListening, transcript, support };
};
