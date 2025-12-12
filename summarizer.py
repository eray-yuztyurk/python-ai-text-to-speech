"""
Text Summarization
This module provides functionality to summarize text using pre-trained summarization models.
"""

import config.ai_models as ai_models
import gradio as gr
from transformers import pipeline
import torch

# models in cache
summ_loaded_models = {}

# loaders
def load_summarizer_model(model_name):
  """
  Load summarizer model for the specified model name.
  Keyword arguments:
      model_name -- name of the summarization model
      Return: summarization pipeline
  """
  model_name_full = ai_models.summarizer_models[model_name]
  summarizer_pipe = pipeline(
      "summarization",
      model=model_name_full
  )

  return summarizer_pipe

# getting models
def get_summarizer_model(model_name):
  """
  Get summarizer model from cache or load if not present.
  Keyword arguments:
      model_name -- name of the summarization model
      Return: summarization pipeline
  """
  if model_name not in summ_loaded_models:
    summ_loaded_models[model_name] = load_summarizer_model(model_name)

  return summ_loaded_models[model_name]

# summarizer
def summarize_text(text_to_summarize, model_name="BART Large CNN"):
  """
  Summarize the input text using the specified summarization model.
  Keyword arguments:
      text_to_summarize -- input text to be summarized
      model_name -- name of the summarization model
      Return: summarized text
  """
  summarizer = get_summarizer_model(model_name)

  model_output = summarizer(text_to_summarize)

  text_output = model_output[0]["summary_text"]

  return text_output

"""
# Gradio Interface
_ui = gr.Interface(
    fn=summarize_text,
    inputs=[
        gr.Dropdown(
            choices=list(ai_models.summarizer_models.keys()),
            label="Model Type",
            value="BART Large CNN"
        ),
        gr.Audio(label="Audio", sources="upload", type="filepath"),
        gr.Checkbox(label="Return Timestamps", value=True)
        ],
    outputs=[
        gr.Textbox(label="Text", lines=15, max_lines=40),
        gr.Textbox(label="Summary", lines=15, max_lines=40)
    ],
    title="Summarizer",
    description="Create a concise summary using BART models."
)

_ui.launch(server_name="0.0.0.0", server_port=7860, inbrowser=True)

"""