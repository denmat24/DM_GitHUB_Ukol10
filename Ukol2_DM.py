#Definice funkce
def create_usernames(data):
    usernames = {}
    students = data["students"]
    active = data["active"]
    transformed_data = {"students": [], "active": [], "usernames": []}

    for i, student in enumerate(students): # využití indexu pro přístup k seznamu active a jeho hodnotě
        if not active[i]:
            continue         # přeskočí neaktivního studenta

        name, surname = student.split() # rozdělení jmen na jméno a příjmení dle mezery

        # 5 písmen příjmení + 3 písmena jména)
        username = (surname[:5] + name[:3]).lower()#vytvoření uživatelského jména a převod na malá písmena

        #kontrola existence username
        exist_user = username
        count = 2 #pro indexaci za jménem od 2
        while username in usernames: #pokud username již existuje
                username = exist_user[:-1] + str(count)#tvorba nového username
                count += 1

            # username, zapsání do mapy

        usernames[username] = True
        transformed_data["usernames"].append(username)
        transformed_data["students"].append(student)
        transformed_data["active"].append(active[i])


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