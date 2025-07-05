def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    count = 0
    words = text.lower()
    for char in words:
        if char not in chars:
            chars[char] = count
            chars[char] += 1
        else:
            chars[char] += 1
    return chars

def sort_on(items):
    return items["num"]

def sorted_dict(dict):
    new_list = []
    for entry in dict:
        if entry.isalpha():
            new_list.append({"char" : entry, "num" : dict[entry]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list