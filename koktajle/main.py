import json


with open("data/cocktail_dataset.json", "r", encoding="utf-8") as f:
    cocktails = json.load(f)


cocktail_db = {c['name']: c for c in cocktails}


def find_cocktails_by_ingredient(ingredient):
    results = []
    for name, c in cocktail_db.items():
        ingredients = [ing['name'] for ing in c['ingredients']]
        if ingredient.lower() in [ing.lower() for ing in ingredients]:
            results.append(name)
    return results


def recommend_by_ingredients(user_ingredients):
    results = []
    for name, c in cocktail_db.items():
        ingredients = [ing['name'] for ing in c['ingredients']]
        if all(ui.lower() in [ing.lower() for ing in ingredients] for ui in user_ingredients):
            results.append(name)
    return results


def show_cocktail_details(name):
    c = cocktail_db[name]
    print(f"\n--- {name} ---")
    print("Instrukcje:", c.get('instructions', 'Brak instrukcji'))
    print("Składniki:")
    for ing in c['ingredients']:
        desc = ing.get('description') or 'Brak opisu'
        print(f" - {ing['name']}: {desc}")


while True:
    print("\nOpcje: ")
    print("1 - Szukaj koktajli po składniku")
    print("2 - Szukaj koktajli po podanych składnikach")
    print("q - wyjście")
    choice = input("Wybierz opcję: ")

    if choice == "1":
        ing = input("Podaj składnik: ")
        res = find_cocktails_by_ingredient(ing)
        if res:
            print("Znalezione koktajle:")
            for i, name in enumerate(res, 1):
                print(f"{i}. {name}")
            sel = input("Wybierz numer koktajlu, żeby zobaczyć szczegóły: ")
            if sel.isdigit() and 1 <= int(sel) <= len(res):
                show_cocktail_details(res[int(sel)-1])
            else:
                print("Nieprawidłowy numer")
        else:
            print("Nie znaleziono koktajli z tym składnikiem")

    elif choice == "2":
        ings = input("Podaj składniki oddzielone przecinkiem: ").split(",")
        ings = [i.strip() for i in ings]
        res = recommend_by_ingredients(ings)
        if res:
            print("Znalezione koktajle:")
            for i, name in enumerate(res, 1):
                print(f"{i}. {name}")
            sel = input("Wybierz numer koktajlu, żeby zobaczyć szczegóły: ")
            if sel.isdigit() and 1 <= int(sel) <= len(res):
                show_cocktail_details(res[int(sel)-1])
            else:
                print("Nieprawidłowy numer")
        else:
            print("Nie znaleziono koktajli z podanymi składnikami")

    elif choice.lower() == "q":
        break
    else:
        print("Nieprawidłowa opcja")