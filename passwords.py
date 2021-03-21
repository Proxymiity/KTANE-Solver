import sys
arg = sys.argv

words = {
    "english": ["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large",
                "learn", "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still",
                "study", "their", "there", "these", "thing", "think", "three", "water", "where", "which", "world",
                "would", "write"]
}

search_language = arg[1]

search = {
    1: [arg[2][x:x+1] for x in range(0, len(arg[2]), 1)],
    2: [arg[3][x:x+1] for x in range(0, len(arg[3]), 1)],
    3: [arg[4][x:x+1] for x in range(0, len(arg[4]), 1)],
    4: [arg[5][x:x+1] for x in range(0, len(arg[5]), 1)],
    5: [arg[6][x:x+1] for x in range(0, len(arg[6]), 1)]
}

total = len(search[1])*len(search[2])*len(search[3])*len(search[4])*len(search[5])
print(f"Searching passwords. There are {total} combinations possible.")
for c in search:
    print(f"Column {c}: {search[c]}")

t = 1
for query_1 in search[1]:
    for query_2 in search[2]:
        for query_3 in search[3]:
            for query_4 in search[4]:
                for query_5 in search[5]:
                    query = query_1 + query_2 + query_3 + query_4 + query_5
                    query = query.lower()
                    if query in words[search_language]:
                        print(f"FOUND: {query} - {t}/{total}")
                    t += 1

print("Search complete!")
