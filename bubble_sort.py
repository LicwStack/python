def bubble_sort(collection):
    length = len(collection)
    for i in range(length-1, -1, -1):
        print i
        for j in range(i):
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
            print collection
    return collection

print bubble_sort([-1, -11, 11, 1, 111])
