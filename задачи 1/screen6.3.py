from collections import Counter

def count_it(sequence):
    counts = Counter(map(int, sequence))
    return dict(counts.most_common(3))
sequence = "3847219346927493648736458274745757587858754785757848"
result_dict = count_it(sequence)
print(result_dict)