def create_dictionary():
    n = int(input("Enter number of key-value pairs to add: "))
    my_dict = {}
    for i in range(n):
        key = input(f"Enter key {i + 1}: ")
        value = input(f"Enter value for '{key}': ")
        my_dict[key] = value
    return my_dict


def add_or_update(my_dict):
    key = input("Enter key to add/update: ")
    value = input("Enter value: ")
    my_dict[key] = value
    return my_dict


def delete_key(my_dict):
    key = input("Enter key to delete: ")
    if key in my_dict:
        del my_dict[key]
    else:
        print("Key not found")
    return my_dict


def search_key(my_dict):
    key = input("Enter key to search: ")
    if key in my_dict:
        return f"'{key}' found with value '{my_dict[key]}'"
    return f"'{key}' not found in dictionary"


def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def main():
    my_dict = create_dictionary()
    print(f"\nInitial dictionary: {my_dict}")

    while True:
        print("\n1. Add/Update\n2. Delete\n3. Search\n4. Display Keys\n5. Display Values\n6. Merge with another dictionary\n7. Display\n8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            my_dict = add_or_update(my_dict)
        elif choice == "2":
            my_dict = delete_key(my_dict)
        elif choice == "3":
            print(search_key(my_dict))
        elif choice == "4":
            print(f"Keys: {list(my_dict.keys())}")
        elif choice == "5":
            print(f"Values: {list(my_dict.values())}")
        elif choice == "6":
            other = create_dictionary()
            my_dict = merge_dictionaries(my_dict, other)
        elif choice == "7":
            print(f"Current dictionary: {my_dict}")
        elif choice == "8":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()