def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict:
    char_counts = {}
    for char in text.lower():
        if char in char_counts.keys():
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars: dict):
    sorted_list = []
    for ch in num_chars:
        sorted_list.append({
            "char": ch,
            "num": num_chars[ch]
        })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
