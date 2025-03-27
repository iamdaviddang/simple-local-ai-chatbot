# Simple Local AI Chatbot

🚀 **Simple Local AI Chatbot** is a lightweight chatbot running locally on your PC. It uses the **llama.cpp** model to generate responses based on user input without requiring an internet connection.

## 📌 Features

- Runs locally without cloud services.
- Supports **llama.cpp** for efficient inference.
- Simple deployment and configuration.

---

## 🛠 Installation

### 1. Clone the repository

```sh
git clone https://github.com/iamdaviddang/simple-local-ai-chatbot.git
cd simple-local-ai-chatbot
```

### 2. Install dependencies

Make sure you have **Python 3.10+** installed and run:

```sh
pip install -r requirements.txt
```

### 3. Download the model

You need to download an AI model compatible with **llama.cpp** in `ggml` or `gguf` format. For example:

```sh
wget -O models/llama.gguf https://example.com/path-to-model.gguf
```

---

## 🚀 Usage

Run the chatbot with:

```sh
python main.py --model models/llama.gguf
```

Or specify a custom model:

```sh
python main.py --model /path/to/your/model.gguf
```

You can then start entering questions, and the chatbot will respond based on the trained model.

---

## ⚙️ Configuration

The `config.yaml` file allows you to adjust parameters like:

```yaml
model_path: "models/llama.gguf"
max_tokens: 200
temperature: 0.7
top_p: 0.9
```

Modify it according to your needs.

---

## 🏗 Project Structure

```
├── models/              # Folder for AI models
├── src/                 # Source code
│   ├── chatbot.py       # Main chatbot logic
│   ├── utils.py         # Helper functions
│   ├── config.yaml      # Configuration file
├── requirements.txt     # Dependencies list
├── main.py              # Main script
└── README.md            # This file
```

---

## 📜 License

This project is licensed under the **MIT License** – you are free to modify and use it.

---

🔹 **Author:** [David Dang](https://github.com/iamdaviddang)  
💬 **Feedback:** Open an issue or create a pull request! 😊
