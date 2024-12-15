from collections import deque

class Node:
    def __init__(self, data=None):
        # Inicializace uzlu s daty a prázdnými odkazy na levý a pravý podstrom
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        # Vložení nových dat do stromu podle pravidel binárního vyhledávacího stromu
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)# Vložení nového uzlu do levého podstromu
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data) # Vložení nového uzlu do pravého podstromu
                else:
                    self.right.insert(data)# Rekurzivní volání na pravý podstrom
        else:
            self.data = data # Pokud uzel ještě nemá data, vloží se sem


    def print_tree(self, level=0, prefix=""):
        # Tisk binárního stromu s odsazením podle úrovně
        if self.data is not None:
            print(" " * (4 * level) + prefix + str(self.data))
            if self.left:
                self.left.print_tree(level + 1, "L: ")
            if self.right:
                self.right.print_tree(level + 1, "R: ")

    def in_order_traversal(self):
        # In-order průchod binárním stromem
        ordered_elements = []
        if self.left:
            ordered_elements += self.left.in_order_traversal()
        ordered_elements.append(self.data) # Přidání aktuálních dat uzlu
        if self.right:
            ordered_elements += self.right.in_order_traversal()
        return ordered_elements # Vrácení seznamu se seřazenými prvky

    def max_depth(self, depth=0):
        # Funkce pro zjištění maximální hloubky (výšky) stromu
        if self.left:
            left_depth = self.left.max_depth(depth + 1)
        else:
            left_depth = depth
        if self.right:
            right_depth = self.right.max_depth(depth + 1)
        else:
            right_depth = depth
        return max(left_depth, right_depth) # Vrátí maximální hloubku mezi levým a pravým podstromem

    def contains(self, data):
        found, steps = self.breadth_first_search(data)
        return found, steps

    def breadth_first_search(self, data):
        if self is None:
            return False, 0  # Pokud strom je prázdný, vracíme False a 0 kroků

        queue = deque([self])   # Začínáme s kořenem stromu
        visited = set()  # Množina pro sledování navštívených uzlů
        visited.add(self)  # Označení kořenového uzlu jako navštíveného
        steps = 0  # Počet kroků

        while queue:
            current = queue.popleft()  # Vyjmutí prvního uzlu z fronty
            steps += 1  # Zvýšení počtu kroků

            # Tisk aktuálního uzlu a počtu kroků
            #print(f"Prohledávám uzel: {current.data}, krok: {steps}")

            # Zkontrolujeme, zda aktuální uzel odpovídá hledaným datům
            if current.data == data:
                return True, steps  # Pokud jsme našli hledaný uzel, vrátíme True a počet kroků

            # Pokud existuje levý podstrom a ještě nebyl navštíven, přidáme ho do fronty
            if current.left and current.left not in visited:
                queue.append(current.left)
                visited.add(current.left)
            # Pokud existuje pravý podstrom a ještě nebyl navštíven, přidáme ho do fronty
            if current.right and current.right not in visited:
                queue.append(current.right)
                visited.add(current.right)

        return False, steps # Pokud uzel nebyl nalezen, vrátíme False a počet kroků

    def print_tree_centered(self):
        max_depth = self.max_depth() # Zjištění maximální hloubky stromu
        lines = [] # Seznam pro uchování řádků při tisku
        self._print_tree_centered_helper(self, 0, max_depth, lines)
        for line in lines:
            print(line) # Tisk každého řádku

    def _print_tree_centered_helper(self, node, depth, max_depth, lines):
        if node is None:
            return

        value = str(node.data) # Převod hodnoty uzlu na řetězec
        space_before = " " * (2 ** (max_depth - depth) - 1)  # Počet mezer před hodnotou uzlu
        space_between = " " * (2 ** (max_depth - depth + 1) - 1) # Počet mezer mezi hodnotami uzlů
        # Pokud ještě není dostatek řádků pro danou úroveň, přidáme nový řádek
        if len(lines) <= depth:
            lines.append(space_before + value)
        else:
            lines[depth] += space_before + value # Přidáme hodnotu uzlu na správné místo v řádku

        self._print_tree_centered_helper(node.left, depth + 1, max_depth, lines)
        self._print_tree_centered_helper(node.right, depth + 1, max_depth, lines)

# Testing

bin_tree = Node(10)
bin_tree.insert(6)
bin_tree.insert(14)
bin_tree.insert(5)
bin_tree.insert(8)
bin_tree.insert(11)
bin_tree.insert(18)
bin_tree.insert(18)
bin_tree.insert(1)
bin_tree.insert(20)
bin_tree.insert(25)


found, steps = bin_tree.breadth_first_search(10)
assert found == True and steps == 1

found, steps = bin_tree.contains(10)
assert found == True and steps == 1

found, steps = bin_tree.breadth_first_search(18)
assert found == True and steps == 7

found, steps = bin_tree.contains(18)
assert found == True and steps == 7

found, steps = bin_tree.breadth_first_search(11)
assert found == True and steps == 6

found, steps = bin_tree.contains(11)
assert found == True and steps == 6

found, steps = bin_tree.breadth_first_search(55)
assert found == False and steps == 10

print("All tests passed!")

bin_tree.print_tree_centered()
