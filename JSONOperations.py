import json


def create_data():
    n = int(input("Enter number of records to add: "))
    records = []
    for i in range(n):
        print(f"\nRecord {i + 1}")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        city = input("Enter city: ")
        records.append({"name": name, "age": age, "city": city})
    return records


def write_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data written to {filename}")


def read_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def display_json(data):
    print("\nRecords:")
    for record in data:
        print(record)


def update_record(data):
    name = input("\nEnter name of record to update: ")
    for record in data:
        if record["name"].lower() == name.lower():
            new_city = input(f"Enter new city for {name}: ")
            record["city"] = new_city
            print(f"Updated {name}'s city to {new_city}")
            return data
    print(f"No record found for {name}")
    return data


def filter_by_age(data, min_age):
    return [record for record in data if record["age"] >= min_age]


def main():
    filename = "records.json"
    data = create_data()
    write_json(filename, data)

    loaded_data = read_json(filename)
    display_json(loaded_data)

    updated_data = update_record(loaded_data)
    write_json(filename, updated_data)
    display_json(read_json(filename))

    min_age = int(input("\nEnter minimum age to filter records: "))
    filtered = filter_by_age(updated_data, min_age)
    print(f"\nRecords with age >= {min_age}:")
    display_json(filtered)


if __name__ == "__main__":
    main()