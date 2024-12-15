from  typing import Tuple

"""
    vvvv      YOUR SOLUTION      vvvv
"""


class Entity:

    def __init__(self, name: str, coords: Tuple[int, int], hit_points: int) -> None:
        # "constructor", more precisely "initializer"
        # initialize Entity here
        # name is string such as "Rob"
        # coords is tuple to represent x and y coordinates in the field: (1, 2) menas x = 1 and y = 2; expect also negative values
        # hitpoints represents count of remaining hitpoints as int, 0 or less hitpoints means death
        self.name=name
        self.coords=coords
        self.hit_points=hit_points
        pass

    def take_damage(self, damage_amount: int) -> None:
        # m# method to apply damage on this entity, it takes damage_amount and applies it by own rules to the entity
        # this is abstract method, just keep it as it is
        raise NotImplementedError("This method is abstract. Please implement it")  # in the child, not here :-)

    def is_alive(self) -> bool:
        # method to check if entity is alive
        # return True if it has hit points above 0
        # return False if it has hit points equal to 0 or less
        return self.hit_points>0
        pass

    def get_distance(self, other_coords: Tuple[int, int]) -> int:
        # method to count distance to other object
        # for calculation of distance use Taxicab/Manhattan metric: https://en.wikipedia.org/wiki/Taxicab_geometry
        # returns the distance
        return abs(self.coords[0]-other_coords[0])+abs(self.coords[1]-other_coords[1])
        pass


class Rock(Entity):

    def take_damage(self, damage_amount: int) -> None:
        # method to apply damage on this entity
        # rock takes damage only when it is hit with damage_amount of at least 10,
        # each such hit takes him 1 hitpoint, smaller hits don't cause any damage to him
        if damage_amount >=10:
            self.hit_points-=1
        pass


class Furniture(Entity):
    def take_damage(self, damage_amount: int) -> None:
        self.hit_points-=damage_amount
    # add take_damage method as for the Rock
    # Furniture takes as damage the whole amount of damage_amount incoming
    pass


class LivingEntity(Entity):

    def __init__(self, name: str, coords: Tuple[int, int], hit_points: int, level: int, damage: int, attack_range: int) -> None:
        # "constructor", more precisely "initializer"
        # use parent constructor
        # initialize level, damage and attack_range after both are ints
        super().__init__(name, coords, hit_points)
        self.level=level
        self.damage=damage
        self.attack_range=attack_range
        pass

    def level_up(self) -> None:
        # this method should increase the level of this entity by 1
        self.level+=1
        pass

    def take_damage(self, damage_amount: int) -> None:
        # method to apply damage on this entity
        # the whole damage_amount is applied to hitpoints
        self.hit_points-=damage_amount
        pass

    def hit(self, other_entity: Entity) -> None:
        # method to hit other entity to cause them to take damage
        # this is abstract method, just keep it as it is
        raise NotImplementedError("This method is abstract. Please implement it")  # in the child, not here :-)

    def move(self, vector: Tuple[int, int]) -> None:
        # method to make entity move on the board
        # it expects vector of steps in x and y directions, the vector is represented as tuple (x, y)
        # the move is executed by editing coordinates by the vector elements
        # x is editing x axis and y is editing y axis
        # +x, -x, +y, -y define also direction of move
        self.coords=(self.coords[0]+vector[0], self.coords[1]+vector[1])
        pass

    def in_range(self, other_entity: Entity) -> bool:
        # method to check if other entity is in range
        # return True if get_distance to other entity <= self.range
        # return False if get_distance to other entity > self.range
        return self.get_distance(other_entity.coords)<=self.attack_range
        pass


class Warrior(LivingEntity):

    def hit(self, other_entity: Entity) -> None:
        # implement hit to another entity
        #   if other entity is in range make it to take damage with it's own method take_damage
        #       damage_amount applied to other entity is equal to damage of attacking entity
        if self.in_range(other_entity):
            other_entity.take_damage(self.damage)
        pass

    def take_damage(self, damage_amount: int) -> None:
        # method to apply damage on this entity
        # Warrior is taking damage only when the damage_amount is bigger then his level
        #   If damage is bigger than level Warrior takes the difference as a damage_amount
        #   Else Warrior takes no damage
        if damage_amount > self.level:
            self.hit_points -= (damage_amount - self.level)
        pass

    def level_up(self) -> None:
        # this method should increase the level according to parent; use call to parent's method
        # also increase damage by 1 and hit_points by 2
        super().level_up()
        self.damage += 1
        self.hit_points += 2
        pass


class Archer(LivingEntity):

    def hit(self, other_entity: Entity) -> None:
        # implement hit to another entity
        #   if other entity is in range make it to take damage with it's own method take_damage
        #       damage_amount applied to other entity is equal to damage of attacking entity
        if self.in_range(other_entity):
            other_entity.take_damage(self.damage)
        pass

    def level_up(self) -> None:
        # this method should increase the level according to parent; use call to parent's method
        # also increase damage by 2 and hit_points by 1
        super().level_up()
        self.damage += 2
        self.hit_points += 1
        pass


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


# Simple Entity tests
print("Testing Entity class...")
entity = Entity("E", (0, 0), 10)
print(f"Created Entity: Name={entity.name}, Coords={entity.coords}, Hit Points={entity.hit_points}")
# constructor
assert entity.name == "E"
assert entity.coords == (0, 0)
assert entity.hit_points == 10
# is alive check
assert entity.is_alive()
# get distance check
assert entity.get_distance((0, 0)) == 0
print(f"Entity distance check passed: Distance to (0,0) = {entity.get_distance((0, 0))}")

print("Entity tests passed.\n")

# Rock tests
print("Testing Rock class...")
rocky = Rock("Rocky", (0, 1), 5)
print(f"Created Rock: Name={rocky.name}, Coords={rocky.coords}, Hit Points={rocky.hit_points}")
# constructor
assert rocky.name == "Rocky"
assert rocky.coords == (0, 1)
assert rocky.hit_points == 5
# is alive check
assert rocky.is_alive()
# get distance check
assert rocky.get_distance((0, 0)) == 1
# damage taking
rocky.take_damage(7)
assert rocky.hit_points == 5
print(f"Rock take_damage check (7 damage) passed: {rocky.hit_points}")
rocky.take_damage(100)
assert rocky.hit_points == 4
print(f"Rock take_damage check (100 damage) passed: {rocky.hit_points}")
print("Rock tests passed.\n")

# Table tests
print("Testing Furniture class...")
table = Furniture("Table", (1, 0), 3)
print(f"Created Furniture: Name={table.name}, Coords={table.coords}, Hit Points={table.hit_points}")
# constructor
# constructor
assert table.name == "Table"
assert table.coords == (1, 0)
assert table.hit_points == 3
# is alive check
assert table.is_alive()
# get distance check
assert table.get_distance((0, 0)) == 1
# damage taking
table.take_damage(2)
assert table.hit_points == 1
(f"Furniture take_damage check (2 damage) passed: {table.hit_points}")
table.take_damage(2)
assert table.hit_points == -1
print(f"Furniture take_damage check (2 damage) passed: {table.hit_points}")
assert not table.is_alive()
print(f"Furniture is_alive check after taking damage passed: {table.is_alive()}")

print("Furniture tests passed.\n")

# LivingEntity tests
print("Testing LivingEntity class...")
tim = LivingEntity("Tim", (-1, 0), 3, 1, 1, 1)
print(f"Created LivingEntity: Name={tim.name}, Coords={tim.coords}, Hit Points={tim.hit_points}, Level={tim.level}, Damage={tim.damage}, Attack Range={tim.attack_range}")
# constructor
assert tim.name == "Tim"
assert tim.coords == (-1, 0)
assert tim.hit_points == 3
assert tim.level == 1
assert tim.damage == 1
assert tim.attack_range == 1
# is alive check
assert tim.is_alive()
# get distance check
tim.level_up()
assert tim.level == 2
# damage taking
tim.take_damage(1)
assert tim.hit_points == 2
print(f"LivingEntity take_damage check (1 damage) passed: {tim.hit_points}")
assert tim.is_alive()
print(f"LivingEntity is_alive check after taking damage passed: {tim.is_alive()}")
# move check
assert tim.in_range(entity)
tim.move((0, -1))
assert not tim.in_range(entity)
print("LivingEntity tests passed.\n")

# Warrior tests
print("Testing Warrior class...")
willy = Warrior("William Wallace", (1, 1), 3, 5, 8, 2)
print(f"Created Warrior: Name={willy.name}, Coords={willy.coords}, Hit Points={willy.hit_points}, Level={willy.level}, Damage={willy.damage}, Attack Range={willy.attack_range}")
# constructor
assert willy.name == "William Wallace"
assert willy.coords == (1, 1)
assert willy.hit_points == 3
assert willy.level == 5
assert willy.damage == 8
assert willy.attack_range == 2
# is alive check
assert willy.is_alive()
# get distance check
assert willy.get_distance((0, 0)) == 2
# level up check
willy.level_up()
assert willy.hit_points == 5
assert willy.level == 6
assert willy.damage == 9
# damage taking
willy.take_damage(1)
assert willy.hit_points == 5
print(f"Warrior take_damage check (1 damage) passed: {willy.hit_points}")
willy.take_damage(7)
assert willy.hit_points == 4
print(f"Warrior take_damage check (7 damage) passed: {willy.hit_points}")
# fight checks
rocky = Rock("Rocky", (0, 1), 5)
willy.hit(rocky)
assert rocky.hit_points == 5
table = Furniture("Table", (1, 0), 3)
willy.hit(table)
assert table.hit_points == -6
print(f"Warrior hits Furniture: Table's hit points reduced to {table.hit_points}")
tim = LivingEntity("Tim", (-1, 0), 3, 1, 1, 1)
willy.hit(tim)
assert tim.hit_points == 3
print(f"Warrior hits Life Entity: Tim's hit points reduced to {tim.hit_points}")

willy.move((-1, -1))
assert willy.get_distance((0, 0)) == 0
willy.hit(tim)
assert tim.hit_points == -6
print("Warrior tests passed.\n")

# Archer tests
print("Testing Archer class...")
rob = Archer("Robin Hood", (5, 8), 3, 1, 7, 10)
print(f"Created Archer: Name={rob.name}, Coords={rob.coords}, Hit Points={rob.hit_points}, Level={rob.level}, Damage={rob.damage}, Attack Range={rob.attack_range}")
# constructor
assert rob.name == "Robin Hood"
assert rob.coords == (5, 8)
assert rob.hit_points == 3
assert rob.level == 1
assert rob.damage == 7
assert rob.attack_range == 10
# is alive check
assert rob.is_alive()
# get distance check
assert rob.get_distance((0, 0)) == 13
# level up check
rob.level_up()
assert rob.hit_points == 4
assert rob.level == 2
assert rob.damage == 9
print(f"Archer level_up check passed: Level={rob.level}, Hit Points={rob.hit_points}, Damage={rob.damage}")
# damage taking
rob.take_damage(1)
assert rob.hit_points == 3
print(f"Archer take_damage check (1 damage) passed: {rob.hit_points}")
# fight checks
willy = Warrior("William Wallace", (1, 1), 3, 5, 8, 2)
rob.hit(willy)
assert willy.hit_points == 3
print(f"Archer hits Warrior: Willy's hit points reduced to {willy.hit_points}")
rob.move((0, -1))
rob.hit(willy)
assert willy.hit_points == -1
assert not willy.is_alive()
print("Archer tests passed.\n")

print("All tests completed successfully.")