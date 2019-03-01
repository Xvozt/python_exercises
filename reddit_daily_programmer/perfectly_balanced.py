"""Given a string containing only the characters x and y,
find whether there are the same number of xs and ys.

balanced("xxxyyy") => true
balanced("yyyxxx") => true
balanced("xxxyyyy") => false
balanced("yyxyxxyxxyyyyxxxyxyx") => true
balanced("xyxxxxyyyxyxxyxxyy") => false
balanced("") => true
balanced("x") => false

Optional bonus
Given a string containing only lowercase letters,
find whether every letter that appears in the string
appears the same number of times.
Don't forget to handle the empty string ("") correctly!

balanced_bonus("xxxyyyzzz") => true
balanced_bonus("abccbaabccba") => true
balanced_bonus("xxxyyyzzzz") => false
balanced_bonus("abcdefghijklmnopqrstuvwxyz") => true
balanced_bonus("pqq") => false
balanced_bonus("fdedfdeffeddefeeeefddf") => false
balanced_bonus("www") => true
balanced_bonus("x") => true
balanced_bonus("") => true
"""


def balanced(example):
    ys = []
    xs = []
    for x in example:
        if x == 'x':
            xs.append(x)
        else:
            ys.append(x)
    if len(xs) == len(ys):
        return True
    else:
        return False

print(balanced("xxxyyy"))
print(balanced("yyyxxx"))
print(balanced("xxxyyyy"))
print(balanced("yyxyxxyxxyyyyxxxyxyx"))
print(balanced("xyxxxxyyyxyxxyxxyy"))
print(balanced(""))
print(balanced("x"))


def balanced_bonus(example):
    chars_split = list(example)
    letter_count = {}
    for c in chars_split:
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1
    return len(set(letter_count.values())) <= 1


print(balanced_bonus("xxxyyyzzz"))
print(balanced_bonus("abccbaabccba"))
print(balanced_bonus("xxxyyyzzzz"))
print(balanced_bonus("abcdefghijklmnopqrstuvwxyz"))
print(balanced_bonus("pqq"))
print(balanced_bonus("fdedfdeffeddefeeeefddf"))
print(balanced_bonus("www"))
print(balanced_bonus("x"))
print(balanced_bonus(""))
