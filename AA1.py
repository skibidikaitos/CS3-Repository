class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        print(f"{self.name} attacks the Zombie for {self.damage} damage!")
        zombie.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        if self.distance > 0:
            self.distance -= 1
            print(f"{self.name} moves closer! Distance: {self.distance}")

    def attack(self, plant):
        print(f"{self.name} attacks {plant.name} for {self.damage} damage!")
        plant.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

plant1 = Plant("plant1", 50, 15)
plant2 = Plant("plant2", 50, 10)
zombie = Zombie("Zombie", 500, 20, 3)

turn = 1

print("=== PLANTS VS ZOMBIE ===")

while True:
    print(f"\n--- Turn {turn} ---")

    print(f"Plant1 Health: {plant1.health}")
    print(f"Plant2 Health: {plant2.health}")
    print(f"Zombie Health: {zombie.health}")
    print(f"Zombie Distance: {zombie.distance}")

    if plant1.health > 0:
        plant1.attack(zombie)

        if zombie.health <= 0:
            print("\nZombie Health: 0")
            print("Plants win!")
            break

    if plant2.health > 0:
        plant2.attack(zombie)

        if zombie.health <= 0:
            print("\nZombie Health: 0")
            print("Plants win!")
            break

    if zombie.distance > 0:
        zombie.move()
    else:
        if plant1.health > 0:
            zombie.attack(plant1)
        elif plant2.health > 0:
            zombie.attack(plant2)

    print(f"Plant1 Health: {plant1.health}")
    print(f"Plant2 Health: {plant2.health}")
    print(f"Zombie Health: {zombie.health}")
    print(f"Zombie Distance: {zombie.distance}")

    if plant1.health <= 0 and plant2.health <= 0:
        print("\nZombie wins!")
        break

    turn += 1