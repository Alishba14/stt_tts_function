document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('ttsForm');
    const textInput = document.getElementById('textInput');
    const synthesizeBtn = document.getElementById('synthesizeBtn');
    const audioContainer = document.getElementById('audioContainer');
    const audioPlayer = document.getElementById('audioPlayer');
    const downloadBtn = document.getElementById('downloadBtn');
    const errorAlert = document.getElementById('errorAlert');
    
    let audioBlob = null;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const text = textInput.value.trim();
        if (!text) {
            showError('Please enter some text');
            return;
        }

        // Reset UI
        hideError();
        audioContainer.classList.add('d-none');
        synthesizeBtn.disabled = true;
        synthesizeBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Generating...';

        try {
            const formData = new FormData();
            formData.append('text', text);

            const response = await fetch('/synthesize', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.error || 'Failed to generate speech');
            }

            // Get the audio blob
            audioBlob = await response.blob();
            
            // Create object URL and update audio player
            const audioUrl = URL.createObjectURL(audioBlob);
            audioPlayer.src = audioUrl;
            
            // Show audio container
            audioContainer.classList.remove('d-none');

        } catch (error) {
            showError(error.message);
        } finally {
            synthesizeBtn.disabled = false;
            synthesizeBtn.innerHTML = '<i class="bi bi-play-circle"></i> Synthesize Speech';
        }
    });

    downloadBtn.addEventListener('click', function() {
        if (audioBlob) {
            const url = window.URL.createObjectURL(audioBlob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'tts_output.wav';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        }
    });

    function showError(message) {
        errorAlert.textContent = message;
        errorAlert.classList.remove('d-none');
    }

    function hideError() {
        errorAlert.classList.add('d-none');
        errorAlert.textContent = '';
    }
});
