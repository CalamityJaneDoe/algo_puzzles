import string


def playset(s: str) -> bool:
    """
    Returns True if there is one or several character(s) duplicate(s) within str
    Solution must have a O(n) complexity in time with n len of str
    """
    alphabet_dict = dict.fromkeys(string.ascii_lowercase, 0)

    for char in s:
        alphabet_dict[char] += 1

    return 2 in alphabet_dict.values()
