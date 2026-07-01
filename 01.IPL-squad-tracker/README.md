# IPL Squad & Salary Tracker

**The question:** Can a simple command-line tool realistically manage IPL-style auction budgets and squad composition without external libraries?

**What I did:** Built a pure-Python CLI application that stores player names, roles, and auction prices for multiple IPL franchises. The tool tracks each team's remaining purse, enforces a squad size limit, calculates average spend per player, and displays a formatted squad summary on demand all through a loop-based menu system with no external dependencies.

**Key finding:** Modeling a ₹100 crore purse across  sample teams showed that teams overspending on top-order batsmen in the first 5 picks consistently ran out of budget for bowling depth.

**Project Outcomes**
This project demonstrates how Python can be used to build a practical command-line management system. Through this application, the following functionalities were successfully implemented:

- Team creation and management
- Dynamic player registration
- Budget tracking
- Squad summary generation
- Data validation and error handling
- Real-world constraint enforcement similar to an IPL auction

**Tools:** Python (functions, loops, dictionaries) — no external libraries
**Data:** Self-defined sample player and price data (swap in real auction data if available)

[View the code](./squad_tracker.py)
