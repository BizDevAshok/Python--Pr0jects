import requests

def get_country_by_name(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    return fetch_country_data(url)

def get_country_by_code(code):
    url = f"https://restcountries.com/v3.1/alpha/{code}"
    return fetch_country_data(url)

def list_all_countries():
    url = "https://restcountries.com/v3.1/all"
    try:
        response = requests.get(url)
    except Exception as e:
        return f"Connection error: {e}"

    if response.status_code == 200:
        data = response.json()
        country_names = sorted([country.get("name", {}).get("common", "Unknown") for country in data])
        return "\n".join(country_names)
    else:
        return f"Error: {response.status_code}"

def fetch_country_data(url):
    try:
        response = requests.get(url)
    except Exception as e:
        return f"Connection error: {e}"

    if response.status_code == 200:
        data = response.json()[0]

        name = data.get("name", {}).get("common", "N/A")
        capital = data.get("capital", ["N/A"])[0]
        region = data.get("region", "N/A")
        population = data.get("population", "N/A")
        area = data.get("area", "N/A")

        languages = ", ".join(data.get("languages", {}).values()) \
            if data.get("languages") else "N/A"

        currencies = ", ".join(
            [f"{v.get('name')} ({k})" for k, v in data.get("currencies", {}).items()]
        ) if data.get("currencies") else "N/A"

        return f"""
✅ Country: {name}
🏛 Capital: {capital}
🌍 Region: {region}
👥 Population: {population}
📏 Area: {area} sq. km
🗣 Languages: {languages}
💰 Currencies: {currencies}
""".strip()
    else:
        return f"Error: {response.status_code}"

def save_to_file(data, filename="country_info.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)
        return f" Data saved to {filename}"
    except Exception as e:
        return f"Error saving file: {e}"

def main():
    while True:
        print("\n=== Country Info API ===")
        print("1️⃣ Search by country name")
        print("2️⃣ Search by country code")
        print("3️⃣ List all countries")
        print("4️⃣ Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter country name: ").strip()
            result = get_country_by_name(name)
            print("\n" + result)
            ask_save(result)

        elif choice == "2":
            code = input("Enter 2/3 letter country code: ").strip()
            result = get_country_by_code(code)
            print("\n" + result)
            ask_save(result)

        elif choice == "3":
            result = list_all_countries()
            print("\n" + result)
            ask_save(result)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again!")

def ask_save(data):
    save = input("\nDo you want to save this info to a file? (y/n): ").lower()
    if save == "y":
        filename = input("Enter filename (default: country_info.txt): ").strip() or "country_info.txt"
        print(save_to_file(data, filename))

if __name__ == "__main__":
    main()
