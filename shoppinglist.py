# Einkaufsliste

shoppinglist = ["Shoppinglist"]
print(shoppinglist)

# Funktion zum Hinzufügen von Artikeln!

def add_item():
    item = input("Please enter your item")
    print(f"you want to buy {item}")
    shoppinglist.append(item)
add_item()

#Funktion zum Anzeigen der Einkaufsliste

def show_shoppinglist():
    if shoppinglist:
        print("Deine Einkaufsliste:")
        for item in shoppinglist:
            print(f"{item}")

        else:
            print("Deine Eikaufsliste ist leer")

show_shoppinglist()                
     

#Main function
def main_function():
    while True:
        print("___Einkaufsliste___")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")
        choice = input("Bitte treffen Sie Ihre Auswahl")
        if choice == "1":
            add_item()
        elif choice == "2":
            show_shoppinglist:() 
        elif choice == "3":
            print("Programm wird beendet! AufWiedersehen")
