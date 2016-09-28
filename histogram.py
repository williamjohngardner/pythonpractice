import string
import operator

with open("sample.txt") as opened_file:
    text = opened_file.read().lower()

for i in string.punctuation:
    text = text.replace(i, "")
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")

histogram = {}

for word in text.split(" "):
    if word in histogram.keys():
        histogram[word] += 1
    else:
        histogram[word] = 1


#histogram.items() is converting histogram {} into a list of tuples
"""sorted(iterable[, key][, reverse]), Return a new sorted list from the items in iterable. Has two optional arguments which must be specified as keyword arguments.
key specifies a function of one argument that is used to extract a comparison key from each list element: key=str.lower. The default value is None (compare the elements directly)."""

sorted_hist = sorted(histogram.items(), key=operator.itemgetter(1), reverse=True)
#key = .itemgetter(1) is telling the sorted method which index to sort by.

for idx, item in enumerate(sorted_hist[:20:], start=1):
    word, count = item
    print('{:<3} {:<6} {:>4}'.format(idx, word, count))
