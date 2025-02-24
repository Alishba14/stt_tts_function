import logging
from gtts import gTTS
from typing import Optional

logger = logging.getLogger(__name__)

class TTSEngine:
    def __init__(self):
        """Initialize the TTS engine."""
        try:
            logger.info("TTS Engine initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize TTS engine: {str(e)}")
            raise

    def synthesize(self, text: str, output_path: str) -> Optional[str]:
        """
        Synthesize speech from text and save to file.

        Args:
            text: Input text to synthesize
            output_path: Path to save the output audio file

        Returns:
            Path to the output file if successful, None otherwise
        """
        try:
            # Convert text to speech using gTTS
            tts = gTTS(text=text, lang='en', slow=False)

            # Save audio file
            tts.save(output_path)
            logger.info(f"Successfully synthesized speech to {output_path}")

            return output_path

        except Exception as e:
            logger.error(f"Speech synthesis failed: {str(e)}")
            raise