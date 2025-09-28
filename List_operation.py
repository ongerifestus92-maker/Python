def main():
    # Create an empty list called my_list
    my_list = []
    print(f"1. Empty list: {my_list}")

    # Append elements: 10, 20, 30, 40
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print(f"2. After appending 10, 20, 30, 40: {my_list}")

    # Insert value 15 at the second position
    my_list.insert(1, 15)
    print(f"3. After inserting 15 at position 1: {my_list}")

    # Extend with another list: [50, 60, 70]
    my_list.extend([50, 60, 70])
    print(f"4. After extending with [50, 60, 70]: {my_list}")

    # Remove the last element
    my_list.pop()
    print(f"5. After removing last element: {my_list}")

    # Sort in ascending order
    my_list.sort()
    print(f"6. After sorting in ascending order: {my_list}")

    # Find and print the index of value 30
    index_of_30 = my_list.index(30)
    print(f"7. Index of value 30: {index_of_30}")

if __name__ == "__main__":
    main()
