# 🚀 Multi‑Send‑Question‑NGL

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows%20%7C%20macOS-0ea5e9)
![License](https://img.shields.io/badge/License-MIT-22c55e)

> Send multiple questions to **NGL** from a list — fast and simple.  
> This repo contains `bot.py`, `question.txt`, and `requirements.txt`. Just install the deps, fill your questions, and run.

---

## ✨ What it does
- Reads questions from **`question.txt`** (one question per line).
- Uses **`bot.py`** to send them to your NGL link/username.
- Designed to run from terminal (no extra setup).

> ⚠️ **Use responsibly.** NGL has its own Terms of Service. Spamming or abusing the platform may result in rate‑limits or account actions. This tool is for learning/automation demos only.

---

## 📦 Requirements
- **Python 3.10+** (3.12 works)
- Packages listed in **`requirements.txt`**

---

## 🛠️ Setup

### Option A — Linux / macOS / Windows (PowerShell)
```bash
# 1) Clone
git clone https://github.com/Nadir-N3/Multi-Send-Question-NGL.git
cd Multi-Send-Question-NGL

# 2) (Optional) Create a virtual environment
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# 3) Install dependencies
pip install -r requirements.txt
```

### Option B — Termux (Android)
```bash
pkg update -y && pkg upgrade -y
pkg install python git -y

git clone https://github.com/Nadir-N3/Multi-Send-Question-NGL.git
cd Multi-Send-Question-NGL

pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📝 Prepare your questions
Open **`question.txt`** and put each question on a new line, e.g.:
```
Apa kabar?
Kapan main bareng lagi?
Tips belajar ngoding bang?
```

You can add as many lines as you want. Empty lines are ignored.

---

## ▶️ Run the bot
```bash
python bot.py
```
Then follow the on‑screen prompts (the script will ask for your **NGL link/username** and how many times to send each question).

If your Python has multiple versions, use `python3` instead of `python`.

---

## ✅ Example session
```
$ python bot.py
Enter your NGL link/username: __naadiir.fx
How many times to send each question? 3
Sending...
✔ Sent (1/3): "Apa kabar?"
✔ Sent (2/3): "Apa kabar?"
...
Done!
```

> Output may vary depending on your connection and NGL’s response.

---

## 🧯 Troubleshooting
- **`pip install` fails** → upgrade pip: `python -m pip install --upgrade pip`
- **`ModuleNotFoundError`** → re‑run `pip install -r requirements.txt` in the *same* environment/venv
- **Connection/429** → you are being rate‑limited; reduce the send count, add pauses between runs
- **Termux storage** → if you need to read files from shared storage: `termux-setup-storage`

---

## 📜 License
MIT — see the LICENSE file in this repository.

---

## 🙌 Credits
Created by **Nadir‑N3**.  
Follow me on [X](https://x.com/Naadiir_08) and [Instagram](https://instagram.com/__naadiir.fx).
