# Balanced Parentheses


pairs = {
    "{":"}",
    "(":")",
    "[":"]"
}
opening_brackets = []
sequance = input()
# {[()]}
balanced = True

for char in sequance:
    if char in "{[(":
        opening_brackets.append(char)
    else:
        closing_brackets = opening_brackets.pop()
        if pairs[closing_brackets] != char:
            balanced = False
            break
if balanced:
    print("YES")
else:
    print("NO")


