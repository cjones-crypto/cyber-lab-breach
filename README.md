# The Cyber Lab Breach

A text-based adventure game written in Python for SNHU IT-140 Project Two.

You start in the Security Operations Center of a breached cyber lab. A rogue AI known as **Specter** has taken over the AI Core Chamber. To stop it, you must explore the lab, collect all seven hardware components needed to assemble a forensic workstation, and then face Specter.

## How to run

```bash
python3 cyber_lab_breach.py
```

Requires Python 3. No external dependencies.

## How to play

| Command | What it does |
| ------- | ------------ |
| `go north`, `go south`, `go east`, `go west` | Move between rooms |
| `get <item>` | Pick up the component in the current room |
| `map` | Show the lab layout |

Collect all 7 components before entering the AI Core Chamber:

- CPU — Server Rack Room
- Motherboard — Raspberry Pi Cluster Room
- RAM — Wi-Fi Analysis Lab
- SSD Storage — Malware Sandbox
- PSU — Forensics Workbench
- GPU — Exploit Development Chamber
- Cooling System — Hardware Assembly Lab

## Win / lose

- **Win:** Enter the AI Core Chamber with all 7 components and defeat Specter.
- **Lose:** Enter the AI Core Chamber without all 7 components — Specter wipes the terminal.

## Concepts demonstrated

- Functions and modular structure
- Nested dictionaries for rooms, exits, and items
- Lists for inventory management
- Gameplay loop with branching logic
- Input validation and case-insensitive commands

## Project structure

- `cyber_lab_breach.py` — the complete game in a single file
