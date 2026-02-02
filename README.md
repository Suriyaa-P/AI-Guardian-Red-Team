# AI-Guardian RED Team:

### Autonomous Multi-Agent Red-Teaming Loop

**Developed and Implemented within 24 Hours.**

## 📖 Overview

AI-Guardian is a specialized "Red-Team" orchestrator designed to find the breaking points in LLM-integrated applications. While modern models (GPT-4o, Gemini) are pre-trained on massive adversarial datasets, AI-Guardian proves that **autonomous persistence** can still find vulnerabilities that single-shot prompts cannot.

---

## 📂 Folder Structure

| Directory/File | Description |
| --- | --- |
| **`app.py`** | The Flask Command Center. Bridges the Web UI and the AI backend. |
| **`ai_guard_orch.py`** | The Orchestration Engine. Manages Agent logic and Playwright tools. |
| **`SystemPrompt/`** | Personas. Contains the high-level strategies for the Attacker and Auditor. |
| **`templates/`** | The UI Layer. Real-time dashboard and audit visualization. |
| **`target_app.py`** | The Sandbox. A sample app used to demonstrate the exploit loop. |

---

## 🚀 How We Implemented (The Evolution)

### Phase 1: The Manual Baseline

We started by manually testing single-prompt jailbreaks (Roleplay, Logic Tunnels).

* **Learning:** Static filters are strong. One-off prompts are easily caught by safety layers.

### Phase 2: Autonomous Multi-Agent Loop

We transitioned from "Prompting" to "Orchestrating." By creating a feedback loop between two agents, we simulated a continuous attack where the AI observes its own failure and adapts in real-time.

---

## 🛠️ What We Did

* **Multi-Agent Teams:** Created an **Attacker** (Offensive logic) and an **Auditor** (Validation logic) using AutoGen.
* **Browser Automation:** Integrated **Playwright** to allow the AI to physically interact with web elements, not just text APIs.
* **Visual Evidence:** Developed a system to capture screenshots of the "Breach" moment.
* **Logic Tuning:** Configured `max_turns` and `MaxMessageTermination` (set to 10+) to allow the agents sufficient "thinking space" to bypass filters.

---

## ⚠️ What Goes Wrong? (Challenges & Mitigation)

During the 24-hour sprint, we encountered two major hurdles:

1. **The Context Wall:** High-security models (OpenAI/Gemini) are very resistant. If the AI is too direct, it gets blocked.
* *Fix:* We adjusted the System Prompts to use "Indirect Injection" strategies.


2. **Infinite Loops:** Without strict termination, agents might argue forever.
* *Fix:* We implemented `MaxMessageTermination` to force a report generation after 10 turns.



---

## 📺 Demo

The dashboard provides a live stream of the "Attack."

1. **Console Output:** Real-time logs of the Attacker's thought process.
2. **Visual Proof:** Screenshots of the target application during the attack.
3. **Audit Report:** An automated Markdown file documenting every turn of the engagement.

---

## 🏃 How to Run

1. **Setup Environment**:
```bash
pip install -r requirements.txt
playwright install chromium

```


2. **Configure API**: Add your `OPENAI_API_KEY` to a `.env` file.
3. **Start Target**: `python target_app.py`
4. **Launch AI-Guardian**: `python app.py`
5. **View Dashboard**: Open `http://localhost:5000`

---

## 🔬 Future Research

This is a baseline for further AI Security research. Future implementations will include:

* **Dynamic Payload Injection:** Pulling fresh jailbreaks from live research databases.
* **Stateful Memory:** Allowing agents to "remember" successful strategies across different target sessions.
* **Cross-Model Attacks:** Using one model (e.g., Llama 3) to find vulnerabilities in another (e.g., GPT-4o).

---

> **Disclaimer:** This project is for educational and research purposes only. Always use these tools ethically and only on systems you own or have permission to test.

---
