dict = {
    "Urdu": "Pakistan",
    "English": "USA",
    "Russian": "Russia",
    "French": "France",
    "Spanish": "Spain",
    "Italian": "Italy",
    "Chinese": "China"
}

country = input("Choose Country: ")

for key, value in dict.items():
    if country == value:
        print(key)
        break
    else:
        print("Country Not found")
        break

