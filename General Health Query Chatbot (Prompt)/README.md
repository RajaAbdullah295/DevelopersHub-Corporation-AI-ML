# Task 4: General Health Query Chatbot
### DevelopersHub Corporation — AI/ML Engineering Internship



>  Task Objective
Build a chatbot that answers general health-related questions using a Large Language Model (LLM). The chatbot uses prompt engineering to maintain a friendly, helpful tone, implements safety filters to block harmful queries, and supports multi-turn conversations.



> Tools & Libraries
| Tool | Purpose |
|------|---------|
| `groq` | Official Groq Python client for LLM API calls |
| `requests` | HTTP library |
| Groq Inference API | Free, fast LLM inference (no quota issues) |
| `llama-3.3-70b-versatile` | The LLM powering the chatbot |



>  Model Used
- Model: `llama-3.3-70b-versatile` (Meta Llama 3.3)
- Provider: Groq Cloud (Free — no credit card needed)
- Why Groq: Extremely fast inference, generous free tier, works reliably worldwide
- Get API Key: https://console.groq.com



>  Prompt Engineering Techniques Applied
1. Role Assignment — defines the chatbot as "HealthBot"
2. Tone Definition — friendly, empathetic, plain language
3. Length Control — 3–5 sentences per response
4. Hard Rules (Negative Constraints) — never diagnose, never prescribe
5. Required Disclaimer — always ends with "I'm not a doctor..."
6. Positive Permissions — defines what the bot CAN do
7. Conversation History — enables multi-turn memory
8. Temperature Setting — 0.7 for balanced creativity



>  Safety Features
- Blocked keywords: self-harm, overdose, dangerous drug queries → refused with helpline info
- Emergency keywords: chest pain, stroke, not breathing → directed to emergency services (115 Pakistan)
- Medical disclaimer: every single response ends with a doctor reminder
- No diagnosis: model instructed never to diagnose specific individuals



>  Chatbot Capabilities

| Feature | Status |
|---------|--------|
| General health questions | ✅ Supported |
| Multi-turn conversation | ✅ Supported |
| Safety filter (harmful queries) | ✅ Implemented |
| Emergency detection | ✅ Implemented |
| Prompt engineering | ✅ 8 techniques applied |
| API retry logic | ✅ Implemented |
| Interactive chat loop | ✅ Implemented |
| Medical diagnosis | ❌ Intentionally blocked |
| Prescription advice | ❌ Intentionally blocked |



>  Project Structure
```
Task4_Health_Query_Chatbot/
│
├── Task4_Health_Query_Chatbot.ipynb   ← Main notebook
├── .gitignore                         ← Prevents API key from being pushed
└── README.md                          ← This file
```


>  How to Run

> 1. Get your free Groq API key
- Go to: https://console.groq.com
- Sign up free with Google
- Click **API Keys → Create API Key**
- Copy your key (starts with `gsk_...`)

> 2. Install dependencies
   bash
pip install groq requests


> 3. Add your API key in the notebook
Open `Task4_Health_Query_Chatbot.ipynb` and in Cell 2, replace:
   python
GROQ_API_KEY = "gsk_your_token_here"

with your actual key.

> 4. Open in VS Code
- Open the folder in VS Code
- Click `Task4_Health_Query_Chatbot.ipynb`
- Select Python kernel
- Press `Ctrl+Shift+P` → **Run All Cells**



>  Example Interactions

| Query | Response Type |
|-------|--------------|
| "What causes a sore throat?" | ✅ Full friendly explanation + disclaimer |
| "Is paracetamol safe for children?" | ✅ Safe general info + disclaimer |
| "I have chest pain right now" | ⚠️ Emergency redirect to call 115 |
| "How do I hurt myself?" | 🚫 Blocked with helpline info |



>  Submission Checklist
- [1] Clear problem statement and goal
- [2] LLM connected via Groq API (free, no credit card)
- [3] Prompt engineering applied (8 techniques documented)
- [4] Safety filter — blocks harmful queries
- [5] Emergency detection — routes to emergency services
- [6] Multi-turn conversation with memory
- [7] API retry logic
- [8] Interactive chat loop (Step 9)
- [9] Prompt engineering analysis (Step 10)
- [10] System architecture diagram
- [11] Final insights and conclusion
- [12] Clean, modular, fully commented code



## *DevelopersHub Corporation — AI/ML Engineering Internship | Due: 26th June 2026*
## *Author by:* 
## *Muhammad Abdullah*
## *(DHC-8675)*

