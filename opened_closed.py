def open_closed(s: str) -> bool:
    """
    Returns True if each type of opening char ([, (, ', ") has one closing counterpart
    The opening char MUST be before the closing one within the str
    Solution must have a O(n) complexity in time with n len of str
    """

    stack_parenthesis, stack_brackets = [], []
    count_simple_quote, count_double_quote = 0, 0

    for char in s:
        match char:
            case '(':
                stack_parenthesis.append('(')
            case '[':
                stack_brackets.append('[')
            case ')':
                if stack_parenthesis == []:
                    return False
                else:
                    stack_parenthesis.pop()
            case ']':
                if stack_brackets == []:
                    return False
                else:
                    stack_brackets.pop()
            case '\'':
                count_simple_quote += 1
            case '\"':
                count_double_quote += 1

    return stack_parenthesis == [] and stack_brackets == [] and count_simple_quote % 2 == 0 and count_double_quote % 2 == 0
