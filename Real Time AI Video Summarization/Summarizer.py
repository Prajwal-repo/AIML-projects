from transformers import pipeline
from keybert import KeyBERT

summarizer_abs = pipeline("summarization", model="t5-small")
summarizer_ext = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, mode="abstractive"):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    
    summaries = []
    for chunk in chunks:
        summary = (summarizer_abs if mode == "abstractive" else summarizer_ext)(
            chunk, max_length=120, min_length=40, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    
    return " ".join(summaries)

kw_model = KeyBERT(model='all-MiniLM-L6-v2')

def extract_keywords(text, top_n=5):
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=top_n)
    return [kw[0] for kw in keywords]
