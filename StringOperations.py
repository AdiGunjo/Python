def get_substring(text):
    start = int(input(f"Enter start index for substring of '{text}': "))
    end = int(input(f"Enter end index for substring of '{text}': "))
    return text[start:end]


def reverse_string(text):
    return text[::-1]


def compare_strings(str1, str2):
    if str1 == str2:
        return "Both strings are equal"
    elif str1.lower() == str2.lower():
        return "Strings are equal (ignoring case)"
    else:
        return "Strings are not equal"


def concatenate_strings(str1, str2):
    return str1 + str2


def string_length(text):
    return len(text)


def char_at_position(text):
    pos = int(input(f"Enter position to find character in '{text}': "))
    if 0 <= pos < len(text):
        return text[pos]
    return "Invalid position"


def main():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    print(f"\nSubstring of string 1: {get_substring(str1)}")
    print(f"Reverse of string 1: {reverse_string(str1)}")
    print(f"Reverse of string 2: {reverse_string(str2)}")
    print(f"Comparison result: {compare_strings(str1, str2)}")
    print(f"Concatenated string: {concatenate_strings(str1, str2)}")
    print(f"Length of string 1: {string_length(str1)}")
    print(f"Length of string 2: {string_length(str2)}")
    print(f"Character at given position in string 1: {char_at_position(str1)}")


if __name__ == "__main__":
    main()