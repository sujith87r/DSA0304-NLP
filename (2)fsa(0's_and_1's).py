
def is_equal_01(string):
    count_0 = 0
    count_1 = 0

    for char in string:
        if char == '0':
            count_0 += 1
        elif char == '1':
            count_1 += 1
        else:
            return False

    return count_0 == count_1

# Example usage
test_strings = ["0101", "0010", "000111", "1100", "010101"]

for test_string in test_strings:
    result = is_equal_01(test_string)
    print(f"{test_string}: {'Valid' if result else 'Invalid'}")