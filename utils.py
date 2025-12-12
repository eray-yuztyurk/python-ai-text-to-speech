# adding pauses for better pronunciation
import re
from num2words import num2words

def add_pauses(text):
    """
    Add pauses in the text for better TTS pronunciation.
    Keyword arguments:
        text -- input text
        Return: modified text with pauses
    """
    PAUSE_LINE = "\u200B" * 12
    PAUSE_STRONG = "\u200B" * 8
    PAUSE_SOFT = "\u200B" * 4

    text = re.sub(r'\n+', PAUSE_LINE, text)
    text = re.sub(r'([.!?])', r'\1' + PAUSE_STRONG, text)
    text = re.sub(r'([,;:])', r'\1' + PAUSE_SOFT, text)

    return text

def normalize_numbers(text, lang_code):
    """
    Convert numbers in the text to words.
    Keyword arguments:
        text -- input text
        Return: modified text with numbers converted to words
    """

    def replace_number(match):
        """
        Replace a number with its word representation.
        Keyword arguments:
            match -- regex match object
            Return: number in words
        """

        number = match.group()
        try:
            return num2words(int(number), lang=lang_code) + ", "
        except:
            return number
    
    normalized_text = re.sub(r'\d+', replace_number, text)

    return normalized_text
