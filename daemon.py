def daemon(numbers: list[int], k: int) -> bool:
    """
    Determine if numbers is partitioned array and if item at k index is a pivot :
    1. All items before k index or stricly inferior to item at k index
    2. All items after k index or superior or equal to item at k index
    Solution must have a O(n) complexity in time with n len of numbers and O(1) in space
    """
    for number in numbers[0:k]:
        if number >= numbers[k]:
            return False
    for number in numbers[k:]:
        if number < numbers[k]:
            return False
    
    return True
