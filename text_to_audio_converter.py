"""
TTS - Text to Speech Conversion
This module provides functionality to convert text into speech audio using pre-trained TTS models.
"""

from utils import add_pauses, normalize_numbers
from config.languages import languages_mappping
import gradio as gr
from transformers import pipeline
import torch
import numpy as np
import soundfile as sf
import re

# models in cache
tts_models = {}

# loader
def load_tts_model(lang_code):
    """
    Load TTS model for the specified language code.
    Keyword arguments:
        lang_code -- language code for the TTS model
        Return: TTS pipeline
    """
    
    tts_pipe = pipeline(
        "text-to-speech",
        model=f"facebook/mms-tts-{lang_code}",
    
    )
    
    return tts_pipe

# getting model
def get_tts_model(lang_code):
    """
    Get TTS model from cache or load if not present.
    Keyword arguments:
        lang_code -- language code for the TTS model
        Return: TTS pipeline
    """
    
    if lang_code not in tts_models:
        tts_models[lang_code] = load_tts_model(lang_code)

    return tts_models[lang_code]

# conversion to gradio audio format
def convert_TTS_output(audio, sample_rate=16000):
    """
    Convert TTS model output to Gradio audio format.

    Keyword arguments:
        audio -- audio data from TTS model
        sample_rate -- sampling rate of the audio
        Return: tuple of (sample_rate, audio in int16 format)
    """
    
    audio = np.squeeze(audio)
    audio = np.clip(audio, -1, 1)
    audio = (audio * 32767).astype(np.int16)

    return sample_rate, audio

# conversion to audio
def tts_converter(lang, file_name, text_to_convert):
    """
    Convert text to speech audio and save to a file.
    
    Keyword arguments:
        lang -- language of the text
        file_name -- name of the output audio file
        text_to_convert -- text to be converted to speech
        Return: status message and audio data tuple (sample_rate, audio)
    """
    
    if not file_name:
        status = f"Please provide a valid file name."
        return status, None
    
    # get 3 letter language code
    lang_code = languages_mappping[lang]["iso3"]

    text_to_convert = add_pauses(normalize_numbers(text_to_convert, lang_code))

    full_save_path = f"output_audio_files/{file_name}.wav"

    tts_pipe = get_tts_model(lang_code)

    model_output = tts_pipe(text_to_convert)

    sample_rate, final_audio = convert_TTS_output(model_output["audio"], model_output["sampling_rate"])

    print(type(sample_rate), len(final_audio))

    sf.write(full_save_path,final_audio, sample_rate)

    status = f"Conversion completed! File saved under: '{full_save_path}'"

    return status, (sample_rate, final_audio)

# Gradio UI
_ui = gr.Interface(
    fn=tts_converter,
    inputs=[
        gr.Dropdown(
            list(languages_mappping.keys()),
            label="Please select the language of the text...",
            value="English"
        ),
        gr.Textbox(label="Please provide a file name..."),
        gr.Textbox(label="Please paste your text here...", lines=10, max_lines=40)
    ],
    outputs=[
        gr.Textbox(label=f"Status", lines=2),
        gr.Audio(label="Converted Speech", type="numpy")
    ],
    title="""
        <div style='text-align:center; font-size:28px; font-weight:600;'>
        🎧 Speech from Text Generator
        </div>
        """,
    description="""
        <p>This application converts the provided text into speech audio using pre-trained TTS models from Hugging Face Transformers.</p>
        <p>Select the language, provide a file name, and paste your text to generate the audio.</p>
        """
)

_ui.launch(server_name="0.0.0.0", server_port=7861, inbrowser=True)