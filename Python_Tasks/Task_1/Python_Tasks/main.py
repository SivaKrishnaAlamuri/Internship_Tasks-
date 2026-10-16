
from solutions import (
    word_frequency,
    character_frequency,
    first_non_repeating_character,
    are_anagrams,
    first_repeating_character,
    move_zeros_to_end,
    second_highest_distinct,
    remove_duplicates_preserve_order,
    find_missing_number,
    two_sum_first_pair,
    closest_to_zero,
    common_elements,
    rotate_right,
    maximum_consecutive_pair_sum,
    all_unique_pairs,
)


def run_tests():
    print("Q1 - Word frequency")
    print(word_frequency("python is easy and python is powerful"))
    print(word_frequency("hello hello world"))  

    print("\nQ2 - Character frequency")
    print(character_frequency("banana"))
    print(character_frequency("book"))  

    print("\nQ3 - First non-repeating character")
    print(first_non_repeating_character("swiss"))
    print(first_non_repeating_character("aabbc"))  

    print("\nQ4 - Anagrams")
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("hello", "world"))  

    print("\nQ5 - First repeating character")
    print(first_repeating_character("programming"))
    print(first_repeating_character("abcdefa"))  

    print("\nQ6 - Move zeros to the end")
    print(move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
    print(move_zeros_to_end([1, 0, 2]))  

    print("\nQ7 - Second highest distinct number")
    print(second_highest_distinct([10, 20, 40, 30, 40, 20]))
    print(second_highest_distinct([5, 5, 4]))  

    print("\nQ8 - Remove duplicates preserving order")
    print(remove_duplicates_preserve_order([4, 2, 4, 5, 2, 7, 5]))
    print(remove_duplicates_preserve_order([1, 1, 1, 2]))  

    print("\nQ9 - Missing number from 1 to N")
    print(find_missing_number([1, 2, 4, 5, 6], 6))
    print(find_missing_number([1, 3, 4], 4)) 

    print("\nQ10 - First two-sum pair")
    print(two_sum_first_pair([2, 7, 11, 15], 9))
    print(two_sum_first_pair([1, 4, 6, 8], 10))  

    print("\nQ11 - Number closest to zero")
    print(closest_to_zero([-8, -3, 2, 5, -2]))
    print(closest_to_zero([-4, -1, 1]))  

    print("\nQ12 - Common elements")
    print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print(common_elements([2, 2, 3, 4], [4, 2])) 

    print("\nQ13 - Rotate right")
    print(rotate_right([1, 2, 3, 4, 5], 2))
    print(rotate_right([1, 2, 3], 4)) 

    print("\nQ14 - Maximum consecutive pair sum")
    print(maximum_consecutive_pair_sum([4, 7, 2, 9, 5]))
    print(maximum_consecutive_pair_sum([-5, -2, -7]))  

    print("\nQ15 - All unique pairs for target")
    print(all_unique_pairs([2, 4, 3, 5, 7, 8, 1], 9))
    print(all_unique_pairs([1, 2, 3, 4], 20))  


if __name__ == "__main__":
    run_tests()
