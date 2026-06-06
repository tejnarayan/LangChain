import gradio as gr
import re
import requests

# Try to use Hugging Face transformers if available, otherwise fall back to a simple excerpt
try:
    from transformers import pipeline
    _has_transformers = True
except Exception:
    _has_transformers = False


def _extract_text_from_html(html: str) -> str:
    # crude HTML -> text stripping
    text = re.sub(r"<script.*?>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style.*?>.*?</style>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    # collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def get_summary(url: str) -> str:
    if not url:
        return "Please provide a URL."

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        text = _extract_text_from_html(resp.text)
    except Exception as e:
        return f"Error fetching URL: {e}"

    if not text:
        return "No textual content found at the URL."

    if _has_transformers:
        try:
            summarizer = pipeline("summarization")
            # transformers models have input size limits; summarize first ~2000 chars
            chunk = text[:2000]
            out = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
            return out[0]["summary_text"]
        except Exception:
            pass

    # Fallback: return the first 500 characters as a simple "summary"
    return text[:500] + ("..." if len(text) > 500 else "")

with gr.Blocks() as demo:
    gr.Markdown("## Summarize a URL")
    url_input = gr.Textbox(label="Enter URL")
    summary_output = gr.Textbox(label="Summary")
    summarize_button = gr.Button("Summarize")
    
    summarize_button.click(fn=get_summary, inputs=[url_input], outputs=[summary_output])

if __name__ == "__main__":
    demo.launch()