def get_combinations(text=''):
    # First dealing with edge-cases
    if len(text) == 0:
        return []
    if len(text) == 1:
        return [text]
    if len(text) == 2:
        return [text, text[::-1]]

    # Convert string to array for manipulation further down i.e. len(text) > 2
    text = [elem for index, elem in enumerate(text)]

    combinations = []

    for k in range(len(text)):
        text.insert(0, text.pop())
        for sub_comb in get_combinations(text[1:]):
            tail_text = ''.join(str(char) for char in sub_comb)
            combinations.append('{}{}'.format(text[0], tail_text))
    return combinations


def find_anagram_sub_strings(str1, str2):
    if len(str1) > len(str2):
        combinations = get_combinations(str2)
        return [combination for combination in combinations if combination in str1]

# print find_anagram_sub_strings('cbadcabc', 'abc')
# print find_anagram_sub_strings('cbadcabcd', 'abcd')
