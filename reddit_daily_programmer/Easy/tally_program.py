# https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/

"""5 Friends (let's call them a, b, c, d and e) are playing a game
and need to keep track of the scores.
Each time someone scores a point,
the letter of his name is typed in lowercase.
If someone loses a point, the letter of his name is typed in uppercase.
Give the resulting score from highest to lowest.

Input Description
A series of characters indicating who scored a point. Examples:
abcde
dbbaCEDbdAacCEAadcB
Output Description

The score of every player, sorted from highest to lowest. Examples:
a:1, b:1, c:1, d:1, e:1
b:2, d:2, a:1, c:0, e:-2

Challenge Input:
EbAAdbBEaBaaBBdAccbeebaec
"""


def scoring(series) -> str:
    result = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    for x in series:
        if x == x.lower():
            result[x] += 1
        else:
            result[x.lower()] -= 1
    return sort_result(result)


def sort_result(result):
    sorted_result = []
    for w in sorted(result, key=result.get, reverse=True):
        sorted_result.append(w + ':' + str(result[w]))
    return ', '.join(sorted_result)


print(scoring('EbAAdbBEaBaaBBdAccbeebaec'))
