"List is a collection which is ordered and changeable. Allows duplicate members. \
Tuple is a collection which is ordered and unchangeable. Allows duplicate members. \
Set is a collection which is unordered and unindexed. No duplicate members. \
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members."

# -----------------------------------List------------------------------------------------------------------
lista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(lista)
print("--------------------------------------------------------")

# Acces items
print(lista[1])
print("--------------------------------------------------------")

# Negative indexing
print(lista[-1])
print("--------------------------------------------------------")

# Range of indexes
print(lista[2:5]) # Note: The search will start at index 2 (included) and end at index 5 (not included).
print("--------------------------------------------------------")

# Change item value
print(lista[3])
lista[3] = "peach"
print(lista[3])
print("--------------------------------------------------------")

# Loop through using for
for x in lista:
    print(x)
print("--------------------------------------------------------")

# CHeck if item exists
if "peach" in lista or "pear" in lista:
    print("Peach or pear are in list")
print("--------------------------------------------------------")

# List Length
print("El tamaño de la lista es {}".format(len(lista)))
print("--------------------------------------------------------")

# Add items with append() method
print(lista)
lista.append("pear")
print(lista)
print("--------------------------------------------------------")

# Insert item at specified index using insert()
print(lista)
lista.insert(0, "cocoa")
print(lista)
print("--------------------------------------------------------")

# Remove item using remove()
print(lista)
lista.remove("cocoa")
print(lista)
print("--------------------------------------------------------")

## The pop() method removes the specified index, (or the last item if index is not specified):
x = lista
print(x)
x.pop(3)
print(x)
# del also removes the specified index
del x[2]
print(x)
print("--------------------------------------------------------")

# clear() empties the list
x = lista
print(x)
x.clear()
print(x)
print(lista)
# Note: You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.
print("--------------------------------------------------------")

# COPY A LIST

# Make a copy of a list with the copy() method:
lista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
