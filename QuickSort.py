def quick_sort(sequence):
    length = len(sequence)
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop()
        greater=[]
        lower=[]

        for item in sequence:
            if item > pivot:
                greater.append(item)

            else:
                lower.append(item)
        return quick_sort(lower)+[pivot]+quick_sort(greater)
try:
    list=[]
    while True:
        list.append(int(input()))
except:
    print(list)

          
print(quick_sort(list))
