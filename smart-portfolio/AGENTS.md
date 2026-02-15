# 🤖 AI Agent System Architecture

The **Smart Portfolio Council** is powered by a multi-agent system where distinct "personalities" work in tandem to optimize your portfolio. Unlike a single AI, this system mimics a real-world hedge fund investment committee.

## 👥 The Agents

### 1. Dr. Sentiment (The Analyst) 📰
*   **Role**: Fundamental Analysis & News Monitoring.
*   **Behavior**: Scans "news feeds" (simulated) for qualitative data. Excited by growth stories and innovation.
*   **Output**: Sentiment signals (Bullish/Bearish).

### 2. Quantos (The Mathematician) 📈
*   **Role**: Quantitative Analysis.
*   **Behavior**: Ignores news suitable for numbers. Looks at momentum, correlation, and standard deviation.
*   **Output**: Hard data metrics and probabilities.

### 3. Guardian (The Risk Manager) 🛡️
*   **Role**: Risk Control.
*   **Behavior**: Pessimistic by design. Always looks for the downside. Enforces Volatility and Drawdown limits.
*   **Output**: "Veto" or "Cap" on exposure.

### 4. The Boss (Portfolio Manager) ⚖️
*   **Role**: Decision Maker.
*   **Behavior**: Listens to all inputs. Weighs the Analyst's optimism against the Risk Manager's caution.
*   **Output**: Final execution triggers (Buy/Sell/Rebalance).

---

## 🔄 How They Work in Tandem (The Workflow)

When you click **"Run Analysis"** (or use Voice Control: *"Start Analysis"*), the following chain reaction occurs:

1.  **News Trigger**: **Dr. Sentiment** picks up a market signal (e.g., "Tech sector beating earnings").
2.  **Data Validation**: **Quantos** cross-references this with price action. *"Is the price actually moving? Yes, 3-sigma deviation."*
3.  **Risk Check**: **Guardian** interrupts. *"Wait, volatility is too high. We need to hedge."*
4.  **Eclectic Consensus**: **The Boss** synthesizes this: *"Okay, we buy, but we keep position size small to satisfy Guardian."*
5.  **Execution**: The **Auto-Pilot** executes the rebalance in your portfolio.

## 🏆 Why This is a Winning Solution

### 1. The "Glass Box" Paradox
*   **The Problem**: Traditional "Robo-Advisors" are black boxes. Users trust them blindly or not at all.
*   **Our Solution**: **Transparency as a Feature**. By visualizing the *debate* between agents, we build trust. The user sees the *Reasoning*, not just the *Result*.

### 2. Antifragile Decision Making
*   **The Innovation**: Most systems optimize for one variable (e.g., Return). Our "Council" optimizes for **Survival**.
*   **How**: The tension between the **Analyst** (Greed) and **Risk Manager** (Fear) creates a balanced, hedge-fund-grade strategy that mimics human institutional checks and balances.

### 3. Event-Driven & Real-Time
*   **The Differentiator**: Unlike static rebalancers that run once a quarter, this system is designed to react to **News Events** in real-time (simulated for MVP). It turns Portfolio Management into an active, engaging experience.

## 🚀 Try the Demo

1.  Click **"Load Demo"** to populate a sample portfolio.
2.  Click **"Run Analysis"** (or say *"Start Analysis"*) in the Agent Council.
3.  Watch the **System Audit Log** as the agents debate the best course of action in real-time!
