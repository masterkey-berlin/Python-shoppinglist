import sqlite3

# Verbindung zu sqlite-DB (falls nicht vorhanden ist, dann wird die erstellt.)
conn = sqlite3.connect('croceries.db')

# Erstellung von Cursor um sql-Befehl durchzuführen. 
cursor = conn.cursor()

# Erstellung von Tabellen in croceries.db
cursor.execute('''
CREATE TABLE  IF NOT EXISTS croceries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    amount INTEGER NOT NULL, 
    price FLOAT NOT NULL
    );
''')
# Erste Funktion hinzufügen (CREATE)
def add_item(name, amount, price):
    cursor.execute('''
    INSERT INTO croceries (name, amount, price) VALUES (?, ?, ?)
    ''', (name, amount, price))
    conn.commit()
    print(f"{name} wurde hinzugefügt")

# Erstellung von READ funktion
def show_items():
    cursor.execute('SELECT id, name FROM croceries')
    items = cursor.fetchall()
    for name in items:
        print(name)

# Update function to update items data
def update_item(id, name, amount, price):
    cursor.execute('''
    UPDATE croceries SET name = ?, amount = ?, price = ?
    WHERE id = ?               
    ''',(name, amount, price, id))
    conn.commit()
    print(f"updated items with id {id}")

# Adding a delete function to delete a student

def delete_item(id):
    cursor.execute('''
    DELETE FROM croceries WHERE id = ?                
    ''',(id,))
    conn.commit()
    print(f"Item has been deleted with id {id}")

# define main function to get the user input
# user can choose from create, read, update and delete function
def main():
    while True:
        print("\n----- Shoppingliste -----")
        print("1. Item  hinzufügen")
        print("2. Shoppingliste anzeigen")
        print("3. Item aktualisieren")
        print("4. Item löschen")       
        print("5. Programm beenden")

        choice = input("Bitte wähle eine Option (1,2,3,4 oder 5): ")

        if choice == "1":
            print("Bitte gib die Daten des neuen Items ein: ")
            name = input("name: ")
            amount = input("amount: ")
            price = input("price: ")
            add_item(name, amount, price)
        elif choice == "2":
            show_items()
        elif choice == "3":
            print("Bitte gib die aktualisierten Daten mit id ein: ")
            id = input("id: ")
            name = input("name: ")
            amount = input("amount: ")
            price = input("price: ")
            update_item(id, name, amount, price)
        elif choice == "4":
            print("Bitte gib die ID des zu löschenden Items ein: ")
            id = input("id: ")
            delete_item(id)
        elif choice == "5":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe! Bitte wähle 1,2,3,4 oder 5")

if __name__ == "__main__":
    main()