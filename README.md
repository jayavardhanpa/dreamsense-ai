# DreamSense AI 🧠💭

## AI-Driven Dream Text Analysis (Phase-1)

DreamSense AI is an experimental, research-oriented project that explores how Artificial Intelligence can analyze human dreams using modern NLP architectures and clean, extensible system design.

This repository currently implements Phase-1:
👉 Dream text ingestion, processing, testing, and end-to-end execution
with a strong focus on architecture, testability, and future extensibility.

## 🚀 Project Vision

Humans often experience dreams that feel as real as physical reality.
DreamSense AI aims to study this phenomenon by:

- Analyzing dream narratives using NLP
- Extracting emotional and semantic signals from dream text
- Laying the foundation to later correlate dream content with physiological signals (EEG, HRV, motion)

This repository currently focuses on building a robust, production-ready backbone before adding complex biosignal data.

## ✅ Current Status (Phase-1: COMPLETED)

What is implemented so far:

✔ Clean, modular project architecture
✔ Config-driven design (multi-environment ready)
✔ HuggingFace client abstraction (local, mockable)
✔ NLP processing pipeline
✔ CSV-based batch processing
✔ CLI entrypoint
✔ Structured logging
✔ Unit tests & pipeline validation
✔ End-to-end execution producing output files

⚠️ Note:
Emotion detection and embeddings are currently placeholder implementations.
This is intentional to validate system design before introducing real models.