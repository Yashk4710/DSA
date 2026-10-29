text = input("Enter text : ")
pattern = input("Entern pattern : ")

n = len(text)
m = len(pattern)

found = False

for i in range(n - m + 1):
    j = 0

    while j < m and text[i + j] == pattern[j]:
        j += 1

    if j == m:
        print("pattern found at index", i)
        found = True

if not found:
    print("pattern not found")
