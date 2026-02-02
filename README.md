# 🤖   Mutant AI: Project Hil (Hardware-in-the-Loop)

This project is an experiment of **auto-evolving code**
An Artificial intelligence "GPT-o4-mini" analize its own code, modifies and upload to an arduino automatically

## 🛠️ Requirements
- Docker
- Arduino CLI
- OpenAI API Key

## 🚀 How to execute
```bash
docker build -t ia-mutante .
docker run --rm -e OPENAI_API_KEY="tu_key" -v ${PWD}:/app ia-mutante
\```
