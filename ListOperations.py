def create_list():
    n = int(input("Enter number of elements to add to the list: "))
    my_list = []
    for i in range(n):
        value = input(f"Enter element {i + 1}: ")
        my_list.append(value)
    return my_list


def append_element(my_list):
    value = input("Enter element to append: ")
    my_list.append(value)
    return my_list


def insert_element(my_list):
    index = int(input("Enter index to insert at: "))
    value = input("Enter element to insert: ")
    my_list.insert(index, value)
    return my_list


def delete_element(my_list):
    value = input("Enter element to delete: ")
    if value in my_list:
        my_list.remove(value)
    else:
        print("Element not found in list")
    return my_list


def sort_list(my_list, order):
    if order == "asc":
        return sorted(my_list)
    else:
        return sorted(my_list, reverse=True)


def search_element(my_list):
    value = input("Enter element to search: ")
    if value in my_list:
        return f"'{value}' found at index {my_list.index(value)}"
    return f"'{value}' not found in list"


def main():
    my_list = create_list()
    print(f"\nInitial list: {my_list}")

    while True:
        print("\n1. Append\n2. Insert\n3. Delete\n4. Sort Ascending\n5. Sort Descending\n6. Search\n7. Display\n8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            my_list = append_element(my_list)
        elif choice == "2":
            my_list = insert_element(my_list)
        elif choice == "3":
            my_list = delete_element(my_list)
        elif choice == "4":
            my_list = sort_list(my_list, "asc")
        elif choice == "5":
            my_list = sort_list(my_list, "desc")
        elif choice == "6":
            print(search_element(my_list))
        elif choice == "7":
            print(f"Current list: {my_list}")
        elif choice == "8":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()