# IPL Squad & Salary Tracker

**The question:** Can a simple command-line tool realistically manage IPL-style auction budgets and squad composition without external libraries?

**What I did:** Built a pure-Python CLI application that stores player names, roles, and auction prices for multiple IPL franchises. The tool tracks each team's remaining purse, enforces a squad size limit, calculates average spend per player, and displays a formatted squad summary on demand — all through a loop-based menu system with no external dependencies.

**Key finding:** *(Add this once you've run it — e.g. "Modeling a ₹100 crore purse across 3 sample teams showed that teams overspending on top-order batsmen in the first 5 picks consistently ran out of budget for bowling depth.")*

**If I had more time:** I'd add persistent file storage so squads survive between sessions, and a basic validation layer to flag if a team exceeds the real IPL squad size cap (25 players) or purse limit.

**Tools:** Python (functions, loops, dictionaries) — no external libraries
**Data:** Self-defined sample player and price data (swap in real auction data if available)

[View the code](./squad_tracker.py)
