# Create a Dictionary
cats = {"Tabby" : "Susie2.0","Ginger" : "Susie","Black" : "Bob", "White" : "Joe"}
print(cats)

# Accessing values from a dictionary
my_cat = cats["Ginger"]
print(f"My favourite cat is {my_cat}!")

# Get the list of Keys
list_keys = list(cats.keys())
print(list_keys)

# Get the list of Values
list_values = list(cats.values())
print(list_values)

# Accessing the keys from a dictionary
for key in cats:
    print(key)

# Accesing the values from a dictionary
for key in cats:
    print(cats[key])

# Check whether a key is present in a dictionary
if "Tabby" in cats:
    print(cats["Tabby"])
else:
    print("This key does not exist")

# Adding a key value in a dictionary
cats["tiger"] = "BigSusie"
print(cats)

# Deleting a key value from a dictionary
del(cats["White"])
print(cats)

# Changing a value from a dictionary
cats["Black"] = "BlackSusie"
print(cats)
