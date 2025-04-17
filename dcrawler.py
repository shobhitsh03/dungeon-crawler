import random

# Player setup
player = {
    "name": "Hero",
    "hp": 100,
    "attack": (10, 20)
}

# Monster setup
monsters = [
    {"name": "Goblin", "hp": 30, "attack": (5, 10)},
    {"name": "Skeleton", "hp": 40, "attack": (7, 12)},
    {"name": "Orc", "hp": 60, "attack": (10, 15)},
    {"name": "Dragon", "hp": 100, "attack": (15, 25)}
]

# Dungeon rooms
rooms = ["empty", "monster", "treasure", "trap"]

def battle(monster):
    print(f"\nA wild {monster['name']} appears!")

    while monster["hp"] > 0 and player["hp"] > 0:
        # Player attack
        dmg = random.randint(*player["attack"])
        monster["hp"] -= dmg
        print(f"You attack the {monster['name']} for {dmg} damage.")

        if monster["hp"] <= 0:
            print(f"You defeated the {monster['name']}!")
            break

        # Monster attacks back
        dmg = random.randint(*monster["attack"])
        player["hp"] -= dmg
        print(f"The {monster['name']} hits you for {dmg} damage.")

        if player["hp"] <= 0:
            print("You died... Game over!")
            return False
    return True

def dungeon_crawler():
    print("Welcome to the Dungeon!")
    room_count = 0

    while player["hp"] > 0:
        input("\nPress Enter to enter the next room...")
        room = random.choice(rooms)
        room_count += 1
        print(f"\n-- Room {room_count}: {room.upper()} --")

        if room == "empty":
            print("The room is eerily quiet. Nothing happens.")
        elif room == "monster":
            monster = random.choice(monsters).copy()
            if not battle(monster):
                break
        elif room == "treasure":
            heal = random.randint(10, 30)
            player["hp"] += heal
            print(f"You found a healing potion! Restored {heal} HP.")
        elif room == "trap":
            dmg = random.randint(5, 25)
            player["hp"] -= dmg
            print(f"A trap! You take {dmg} damage.")

        print(f"Your HP: {player['hp']}")
        if player["hp"] <= 0:
            print("You collapsed in the dungeon. Game over!")
            break

    print(f"\nYou survived {room_count} room(s).")

# Run the game
dungeon_crawler()