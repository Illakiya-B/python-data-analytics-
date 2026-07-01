"""
IPL Squad & Salary Tracker
---------------------------
A command-line tool to manage IPL-style auction squads:
tracks player picks, enforces purse limits, and reports squad summaries.

No external libraries — pure Python only.
"""

PURSE_LIMIT_CR = 100.0      # Total purse per team, in crores
MAX_SQUAD_SIZE = 25          # Real IPL squad size cap

teams = {}  # team_name -> {"purse": float, "players": [ {"name", "role", "price"} ]}


def create_team(team_name):
    if team_name in teams:
        print(f"Team '{team_name}' already exists.\n")
        return
    teams[team_name] = {"purse": PURSE_LIMIT_CR, "players": []}
    print(f"Team '{team_name}' created with a purse of ₹{PURSE_LIMIT_CR:.2f} Cr.\n")


def add_player(team_name, player_name, role, price):
    if team_name not in teams:
        print(f"No such team: '{team_name}'. Create it first.\n")
        return

    team = teams[team_name]

    if len(team["players"]) >= MAX_SQUAD_SIZE:
        print(f"'{team_name}' has reached the maximum squad size of {MAX_SQUAD_SIZE}.\n")
        return

    if price > team["purse"]:
        print(f"Not enough purse remaining. '{team_name}' has ₹{team['purse']:.2f} Cr left, "
              f"but {player_name} costs ₹{price:.2f} Cr.\n")
        return

    team["players"].append({"name": player_name, "role": role, "price": price})
    team["purse"] -= price
    print(f"Added {player_name} ({role}) to '{team_name}' for ₹{price:.2f} Cr. "
          f"Remaining purse: ₹{team['purse']:.2f} Cr.\n")


def view_squad(team_name):
    if team_name not in teams:
        print(f"No such team: '{team_name}'.\n")
        return

    team = teams[team_name]
    print(f"\n--- {team_name} Squad ---")
    print(f"{'Player':<20}{'Role':<15}{'Price (Cr)':>10}")
    print("-" * 45)

    total_spent = 0.0
    for player in team["players"]:
        print(f"{player['name']:<20}{player['role']:<15}{player['price']:>10.2f}")
        total_spent += player["price"]

    avg_spend = total_spent / len(team["players"]) if team["players"] else 0.0

    print("-" * 45)
    print(f"Players picked   : {len(team['players'])}/{MAX_SQUAD_SIZE}")
    print(f"Total spent      : ₹{total_spent:.2f} Cr")
    print(f"Average per pick : ₹{avg_spend:.2f} Cr")
    print(f"Purse remaining  : ₹{team['purse']:.2f} Cr\n")


def list_teams():
    if not teams:
        print("No teams created yet.\n")
        return
    print("\nTeams:")
    for name, data in teams.items():
        print(f"  - {name} | Players: {len(data['players'])} | Purse left: ₹{data['purse']:.2f} Cr")
    print()


def print_menu():
    print("=" * 40)
    print("  IPL SQUAD & SALARY TRACKER")
    print("=" * 40)
    print("1. Create a new team")
    print("2. Add a player to a team")
    print("3. View a team's squad")
    print("4. List all teams")
    print("5. Exit")
    print("=" * 40)


def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            team_name = input("Enter team name: ").strip()
            create_team(team_name)

        elif choice == "2":
            team_name = input("Enter team name: ").strip()
            player_name = input("Enter player name: ").strip()
            role = input("Enter role (Batsman/Bowler/All-rounder/Wicketkeeper): ").strip()
            try:
                price = float(input("Enter price (in Cr): ").strip())
                add_player(team_name, player_name, role, price)
            except ValueError:
                print("Invalid price. Please enter a number.\n")

        elif choice == "3":
            team_name = input("Enter team name: ").strip()
            view_squad(team_name)

        elif choice == "4":
            list_teams()

        elif choice == "5":
            print("Exiting. Good luck with the auction!")
            break

        else:
            print("Invalid choice. Please select 1-5.\n")


if __name__ == "__main__":
    main()
