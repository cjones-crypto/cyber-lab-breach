# Christopher Jones
# IT-140 Project Two
# The Cyber Lab Breach


def show_instructions():
    """Display the game instructions, objectives, and available commands."""
    print("The Cyber Lab Breach")
    print("Collect all 7 hardware components before facing Specter. (CPU, Motherboard, RAM, SSD Storage, PSU, GPU, Cooling System)")
    print("Move Commands: go north, go south, go east, go west")
    print("Item Command: get <item name>")
    print("Navigation Aid: map")
    print("-" * 50)


def display_map():
    """Display an ASCII layout of the cyber lab network and room links."""
    print("\n" + "=" * 50)
    print("           [Raspberry Pi Cluster]")
    print("                     |")
    print("[Server Rack] -- [  SOC  ] -- [Wi-Fi Analysis]")
    print("     |               |               |")
    print("[Forensics]     [ Sandbox ]     [Exploit Dev]")
    print("                     |")
    print("                [Hardware]")
    print("                     |")
    print("                [ AI Core ]")
    print("=" * 50)


def show_status(current_room, inventory, rooms):
    """Display player location, current inventory, room item, and available exits."""
    print()
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")

    # Check if an item is located in the current room:
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")

    # Display all valid directional exits for this room
    available_exits = [direction for direction in rooms[current_room] if direction != "item"]
    print(f"Exits: {', '.join(available_exits)}")

    print("-" * 50)


def main():
    # Nested dictionary mapping rooms, paths, items, and the villain
    rooms = {
        'Security Operations Center': {
            'north': 'Raspberry Pi Cluster Room',
            'east': 'Wi-Fi Analysis Lab',
            'west': 'Server Rack Room',
            'south': 'Malware Sandbox'
        },
        'Raspberry Pi Cluster Room': {
            'south': 'Security Operations Center',
            'item': 'Motherboard'
        },
        'Wi-Fi Analysis Lab': {
            'west': 'Security Operations Center',
            'south': 'Exploit Development Chamber',
            'item': 'RAM'
        },
        'Server Rack Room': {
            'east': 'Security Operations Center',
            'south': 'Forensics Workbench',
            'item': 'CPU'
        },
        'Forensics Workbench': {
            'north': 'Server Rack Room',
            'item': 'PSU'
        },
        'Exploit Development Chamber': {
            'north': 'Wi-Fi Analysis Lab',
            'item': 'GPU'
        },
        'Malware Sandbox': {
            'north': 'Security Operations Center',
            'south': 'Hardware Assembly Lab',
            'item': 'SSD Storage'
        },
        'Hardware Assembly Lab': {
            'north': 'Malware Sandbox',
            'south': 'AI Core Chamber',
            'item': 'Cooling System'
        },
        'AI Core Chamber': {
            'north': 'Hardware Assembly Lab',
            'item': 'Specter'
        }
    }

    current_room = 'Security Operations Center'
    inventory = []

    show_instructions()

    # Main gameplay loop
    while True:
        show_status(current_room, inventory, rooms)

        user_input = input("Enter your move:\n").strip()

        # Input check against empty inputs (e.g., no content)
        if not user_input:
            print("No input detected. Enter a command to continue the breach.")
            continue

        command = user_input.split()
        action = command[0].lower()

        # script for movement between rooms
        if action == 'go':
            if len(command) < 2:
                print("Specify a vector: go north, go south, go east, or go west.")
                continue

            direction = command[1].lower()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]

                # Terminal condition check: evaluate immediately upon entering villain chamber
                if current_room == 'AI Core Chamber':
                    if len(inventory) == 7:
                        print()
                        print("Congratulations!")
                        print("You assembled the forensic workstation and defeated Specter.")
                        print("Network security has been restored.")
                    else:
                        print()
                        print("Specter detected an unauthorized breach and wiped the terminal.")
                        print("HA, HA, HA...GAME OVER!")
                        print("Thanks for playing....TRY AGAIN!.")
                    break
            else:
                print("Access denied. No pathway in that direction.")

        # Script for gathering items from rooms
        elif action == 'get':
            if len(command) < 2:
                print("Specify a component to acquire (e.g., get CPU).")
                continue

            # Join remaining tokens to support multi-word item names (e.g., SSD Storage)
            target_item = " ".join(command[1:])
            room_data = rooms[current_room]

            # Check if an item exists and matches the user's input (case-insensitive)
            if "item" in room_data and room_data["item"].lower() == target_item.lower():
                item_name = room_data["item"]
                inventory.append(item_name)
                del room_data["item"]
                print(f"{item_name} collected.")
            else:
                print(f"No {target_item} in this sector.")

        # Script for in-game map navigation command
        elif action == 'map':
            display_map()

        # Script for invalid inputs
        else:
            print("Unknown protocol. Try 'go <direction>', 'get <item>', or 'map'.")


if __name__ == "__main__":
    main()
