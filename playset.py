def playset(s: str) -> bool:
    """
    Returns True if there is one or several character(s) duplicate(s) within str
    Solution must have a O(n) complexity in time with n len of str
    """
    str_set = set(s)

    return len(s) != len(str_set)
