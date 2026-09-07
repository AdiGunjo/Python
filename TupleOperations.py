def create_tuple():
    n = int(input("Enter number of elements for the tuple: "))
    items = []
    for i in range(n):
        value = input(f"Enter element {i + 1}: ")
        items.append(value)
    return tuple(items)
 
 
def create_set(label):
    n = int(input(f"Enter number of elements for set {label}: "))
    items = set()
    for i in range(n):
        value = input(f"Enter element {i + 1}: ")
        items.add(value)
    return items
 
 
def tuple_operations(my_tuple):
    print(f"\nTuple: {my_tuple}")
    print(f"Length: {len(my_tuple)}")
    print(f"Max: {max(my_tuple)}")
    print(f"Min: {min(my_tuple)}")
    value = input("Enter element to count occurrences of: ")
    print(f"Count of '{value}': {my_tuple.count(value)}")
 
 
def set_operations(set_a, set_b):
    print(f"\nSet A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Union: {set_a | set_b}")
    print(f"Intersection: {set_a & set_b}")
    print(f"Difference (A - B): {set_a - set_b}")
    print(f"Symmetric Difference: {set_a ^ set_b}")
    print(f"Is A a subset of B? {set_a.issubset(set_b)}")
 
 
def main():
    my_tuple = create_tuple()
    tuple_operations(my_tuple)
 
    set_a = create_set("A")
    set_b = create_set("B")
    set_operations(set_a, set_b)
 
 
if __name__ == "__main__":
    main()