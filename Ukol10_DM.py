def create_usernames(data):
    usernames = set()  # Použití množiny pro kontrolu unikátnosti
    transformed_data = {"students": [], "active": [], "usernames": []}

    for student, is_active in zip(data["students"], data["active"]):
        if not is_active:
            continue  # Přeskočení neaktivního studenta

        name, surname = student.split()  # Rozdělení na jméno a příjmení
        username_base = (surname[:5] + name[:3]).lower()  # Vytvoření základního uživatelského jména

        # Generování unikátního uživatelského jména
        username = username_base
        count = 2
        while username in usernames:
            username = f"{username_base[:-1]}{count}"
            count += 1

        usernames.add(username)
        transformed_data["usernames"].append(username)
        transformed_data["students"].append(student)
        transformed_data["active"].append(is_active)

    return transformed_data

# Testovací data
data = {
    "students": ["Adam Levine", "Monica Muller", "John Deere", "John Deere"],
    "active": [True, False, True, True]
}

# Testování
assert create_usernames(data) == {
    "students": ["Adam Levine", "John Deere", "John Deere"],
    "active": [True, True, True],
    "usernames": ["levinada", "deerejoh", "deerejo2"]
}

print("Test OK")



