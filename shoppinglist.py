# Einkaufsliste

shoppinglist = ["Shoppinglist"]
print(shoppinglist)

# Wir fordern den Kunden auf, ein Produkt auszuwählen!

def add_item():
    item = input("Please enter your item")
    print(f"you want to buy {item}")
    shoppinglist.append(item)
add_item()

#Der Artikel wird der Liste hinzugefügt

print(shoppinglist)
     