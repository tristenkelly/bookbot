import string


def get_num_words(filepath):
    with open(filepath) as f:
        words = f.read().split()
    return len(words)


def get_num_appearances(filepath):
    with open(filepath) as f:
        text = f.read().lower()
        counts = {}
        for char in text:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        return counts
    
def sort_on(item):
    return item["num"]



