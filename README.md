## 🧠 StrategIQ — Conversational Multi-Agent System

**StrategIQ** is an intelligent multi-agent conversational framework powered by **Gemini**, built to simulate how different experts collaborate to solve complex problems.

It features an **Orchestrator (Team Leader)** that coordinates specialized agents — each representing a distinct role — to deliver well-reasoned, well-rounded responses.

---

### 🚀 Core Idea

Instead of relying on one prompt or persona, **StrategIQ** distributes thinking across five distinct “expert” roles:

| Role                   | Description                                                     |
| ---------------------- | --------------------------------------------------------------- |
| 🧭 **Strategist**      | Provides vision, high-level direction, and long-term thinking.  |
| 🧩 **Product Manager** | Focuses on usability, value, and execution feasibility.         |
| ⚙️ **Engineer**        | Analyzes technical feasibility and implementation details.      |
| 📣 **Marketer**        | Crafts messaging, audience fit, and go-to-market approach.      |
| 🕵️ **Critic**         | Challenges assumptions, identifies risks, and improves quality. |

All are coordinated by the **🗣️ Team Leader / Moderator**, who reviews their insights, identifies conflicts, and synthesizes the final, balanced answer.

---

### 🧬 How It Works

1. The user sends a message.
2. The **Team Leader** receives it, along with stored context.
3. It calls specialized agents as needed via Gemini’s function-calling interface.
4. Each agent returns a structured response.
5. The **Team Leader** merges them into a coherent, actionable answer.
6. Memory is updated for future context.

---

### 🧰 Tech Stack

* **Language:** Python 3.10+
* **Framework:** [Streamlit](https://streamlit.io/)
* **LLM:** [Gemini 2.5 Flash](https://ai.google.dev/)
* **Memory:** Custom `AgentMemory` class for contextual recall
* **Schema:** Structured agent definitions (`schemas/` folder)
* **Orchestration:** Gemini function-calling via `call_gemini()` utility

---

### 🧩 Project Structure

```
strategiq/
├── app.py                  # Streamlit UI
├── main.py                 # Entrypoint logic
├── utils/
│   ├── llm.py              # Handles Gemini API calls
│   ├── memory.py           # Stores/retrieves conversation context
├── functions/
│   ├── agent.py            # Agent function call routing
├── schemas/
│   ├── strategist.py
│   ├── product_manager.py
│   ├── marketer.py
│   ├── engineer.py
│   ├── critic.py
├── .env                    # GEMINI_API_KEY stored here
└── README.md
```

---

### ⚙️ Setup Instructions

#### 1. Clone the repo

```bash
git clone https://github.com/yourusername/strategiq.git
cd strategiq
```

#### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Add your Gemini API key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

#### 5. Run the Streamlit app

```bash
streamlit run app.py
```

---

### 💬 Usage

Once launched, StrategIQ opens a chat interface where you can ask questions like:

> “How can we launch a productivity app for remote teams?”
> “What would be a good strategy for reducing customer churn?”
> “If our budget is limited, how should we prioritize features?”

Behind the scenes, the **Team Leader**:

* Routes your query to the most relevant experts.
* Collects their opinions.
* Resolves conflicts and synthesizes insights into a unified response.

---

### ⚠️ Common Issues

#### 1. `peer closed connection without sending complete message body`

This usually means Gemini’s API closed the connection prematurely due to:

* A long or heavy response
* Recursive calls
* Large message history

✅ Fix: Reset `messages` each call, limit context size, and catch retry exceptions.


### 🧠 Example Conversation Flow

```text
👤 User: How should we improve user retention for our app?

🧭 Strategist: Focus on long-term loyalty through engagement loops.
🧩 Product Manager: Simplify onboarding and reduce friction.
⚙️ Engineer: Implement behavioral analytics and push notifications.
📣 Marketer: Leverage community challenges to drive daily use.
🕵️ Critic: Beware of over-notification fatigue and burnout.

🗣️ Team Leader: Synthesizing…
✅ Final Plan: Streamline onboarding, introduce community-driven retention features, and monitor notification impact with analytics.
```

---

### 🧑‍💻 Future Plans

* [ ] Add **memory persistence** via SQLite or Redis
* [ ] Enable **agent-specific fine-tuning**
* [ ] Support **voice-based conversations**
* [ ] Allow **custom agent creation** via UI
