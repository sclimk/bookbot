#separating the counting words function and counting characters function 
#from the main.py, for it to be imported

def count_words(text):
    return len(text.split())

def count_characters(text):
    counts = {}

    for char in text.lower():
        counts[char] = counts.get(char,0) + 1
    return counts

def sort_characters(counts):
    items_list = []
    for ch, n in counts.items():
        items_list.append({"char":ch, "num":n})

    def sort_on(entry):
        return entry["num"]

    items_list.sort(reverse=True, key=sort_on)
    return items_list



'''
using a conditional, which makes more sense to me...
def counts_characters(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
'''


