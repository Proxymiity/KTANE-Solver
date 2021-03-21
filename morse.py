import sys
arg = sys.argv

words = {
    "english": {"shell": "3.505", "halls": "3.515", "slick": "3.522", "trick": "3.532", "boxes": "3.535",
                "leaks": "3.542", "strobe": "3.545", "bistro": "3.552", "flick": "3.555", "bombs": "3.565",
                "break": "3.572", "brick": "3.575", "steak": "3.582", "sting": "3.592", "vector": "3.595",
                "beats": "3.600"}
}

morse = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h",
    "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q",
    ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z"
}

search_language = arg[1]
values = [x for x in words[search_language]]

query = ""
for encoded_char in arg[2:]:
    try:
        char = morse[encoded_char]
        query += char
    except KeyError:
        print(f"{encoded_char} is not a morse character.")

print(f"Searching for {query}.")

p = 0
for x in values:
    p += len(x)

t = 1
for search in values:
    tries = []
    for x in search:
        search = search[1:] + search[0]
        tries.append(search)
    for y in tries:
        found = False
        if query in y:
            print(f"FOUND: {search} {words[search_language][search]} MHz - {t}/{p}")
            found = True
        if found:
            break
    t += 1

print("Search complete!")
