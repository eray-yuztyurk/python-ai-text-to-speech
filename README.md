<h1 align="center">AI Text-to-Speech & Summarizer</h1>

A compact, multi-language text-to-speech and text summarization toolkit built with state-of-the-art transformer models. This repository demonstrates how modern AI can convert text into natural-sounding speech and generate concise summaries, supporting a wide range of languages and use cases.

<table align="center">
  <tr>
    <td align="left" width="50%" style="vertical-align: top;">
      <h3>📑 Table of Contents</h3>
      <ul>
        <li><a href="#what-this-does">What this does</a></li>
        <li><a href="#key-features">Key features</a></li>
        <li><a href="#how-it-works-high-level">How it works (high level)</a></li>
        <li><a href="#quick-start">Quick start</a></li>
        <li><a href="#example-usage">Example usage</a></li>
        <li><a href="#extending-the-project">Extending the project</a></li>
        <li><a href="#notes-on-data">Notes on data</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
      </ul>
    </td>
    <td align="center" width="50%">
      <img width="400" alt="tts-demo" src="https://user-images.githubusercontent.com/placeholder/tts-demo.png" />
    </td>
  </tr>
</table>

---

## What this does

- Converts input text into speech audio files in multiple languages using pre-trained transformer models.
- Summarizes long texts into concise, readable summaries.
- Provides a simple Gradio web interface for interactive use.

## Key features

- **Multi-language TTS**: Supports 25+ languages with high-quality neural voices.
- **Text Summarization**: Uses advanced transformer models for extractive and abstractive summarization.
- **Easy-to-use UI**: Gradio-powered web interface for both TTS and summarization.
- **Customizable**: Easily extendable with new models or languages.
- **Open Source**: MIT-licensed, ready for research or production.

## How it works (high level)

- **Text-to-Speech**: Utilizes Hugging Face's `transformers` pipelines and Facebook MMS-TTS models. Select a language, enter text, and generate a `.wav` audio file.
- **Summarization**: Uses pre-trained summarization models (e.g., BART, T5) to condense input text. Models are loaded on demand and cached for efficiency.
- **Web UI**: Gradio interfaces wrap both functionalities for easy browser-based access.

## Quick start

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/python-ai-text-to-speech.git
   cd python-ai-text-to-speech
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the TTS app**
   ```bash
   python text_to_audio_converter.py
   ```
   The app will launch at http://localhost:7861

4. *(Optional)* **Run the summarizer**
   ```bash
   python summarizer.py
   ```

## Example usage

- **Text-to-Speech**: Select a language, provide a file name, and paste your text. Download the generated `.wav` file.
- **Summarizer**: Paste your text and get a concise summary instantly.

## Extending the project

- Add new languages by updating `config/languages.py`.
- Integrate new TTS or summarization models in `config/ai_models.py`.
- Customize the Gradio UI for additional features or batch processing.

## Notes on data

- All TTS and summarization models are loaded from Hugging Face Hub.
- Output audio files are saved in the `output_audio_files/` directory.
- No user data is stored or shared.

## Contributing

Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
