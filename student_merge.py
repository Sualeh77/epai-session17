from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts:list)->dict:
    result = defaultdict(int)
    for d in dicts:
        for key in d.keys():
            result[key] += d[key]
    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))


def merge_with_counter(*dicts):
    result = Counter()
    for d in dicts:
        for key in d.keys():
            result[key] += d[key]
    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))