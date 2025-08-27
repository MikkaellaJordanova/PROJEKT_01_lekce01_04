"""
main.py: první projekt do Engeto Online Python Akademie

author: Michaela Jordánová
email: m.jordanova@post.cz
"""
# Texty k analýze:
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#  user |   password  |
# +------+-------------+
# | bob  |     123     |
# | ann  |   pass123   |
# | mike | password123 |
# | liz  |   pass123 

# Registrovaní uživatelé
USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# login
print("=== Přihlášení uživatele ===")
username = input("Zadejte uživatelské jméno: ")
password = input("Zadejte heslo: ")

# 1. Ověření přihlášení dvojice jméno ~ heslo
# 2. zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
# 3. pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
#    Welcome to the app, bob
# 4. pokud není registrovaný, upozorni jej a ukonči program.

# Kontrola přihlášení:
if username in USERS and USERS[username] == password:
    print("-" * 40)
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("-" * 40)

# výběr textu
    selection = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

    if not selection.isdigit():
        print("Invalid input (Neplatný vstup - očekávám číslo!), terminating the program..")
        exit()

    selection = int(selection)
    if selection < 1 or selection > len(TEXTS):
        print("Invalid number (Neplatné číslo - musí být v rozsahu!), terminating the program..")
        exit()

    text = TEXTS[selection - 1]     # sníží hodnotu o 1 kvůli indexování
                                    # tady si vytvoříš list s číslem
# analýza textu
    words = text.split()
    count_words = len(words)                                    # počet slov
    count_titlecase = sum(1 for w in words if w.istitle())      # first_upper,  pocet_titlecase
    count_uppercase = sum(1 for w in words if w.isupper())      # all_upper
    count_lowercase = sum(1 for w in words if w.islower())      # all_lower

 # Číselné řetězce
    numbers = [int(w.strip(".,!?")) for w in words if w.strip(".,!?").isdigit()] # w.strip(".,!?") – odstraní interpunkci
    count_numbers = len(numbers)                                # pocet_cisel
    sum_numbers = sum(numbers)                                  # součet čísel

 # Výpis analýzy textu:
    print("-" * 40)
    print(f"There are {count_words} words in the selected text.")
    print(f"There are {count_titlecase} titlecase words.")
    print(f"There are {count_uppercase} uppercase words.")
    print(f"There are {count_lowercase} lowercase words.")
    print(f"There are {count_numbers} numeric strings.")
    print(f"The sum of all the numbers {sum_numbers}")

# Sloupcový graf podle délky a četnosti slov:
    cetnost = {}                                # slovník, kde klíč = délka slova, hodnota = počet slov té délky.
    for w in words:                             # w.strip(".,!?") – odstraní interpunkci
        l = len(w.strip(".,!?"))                # l = len(...) – zjistí délku očistěného slova.
        if l > 0:                               # if l > 0: – ignoruje prázdná slova
            cetnost[l] = cetnost.get(l, 0) + 1  # zvýší počet slov dané délky o 1,
                                                    # vrátí aktuální počet slov délky l nebo 0, pokud tato délka ještě není ve slovníku.
    print("-" * 40)
    print("LEN|  OCCURRENCES  |NR.")
    print("-" * 40)
    for l in sorted(cetnost):                   # sorted(cetnost) – seřadí délky slov vzestupně
        print(f"{l:>3}|{'*' * cetnost[l]:<18}|{cetnost[l]}")
        
# Ukončení programu při neplatném uživateli nebo vstupu:
else:
    print("unregistered user, terminating the program..")
    exit()