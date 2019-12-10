q1 = "flipped class room is important"
q2 = "junyiacademy"

def str_reverse(sentence):
    words = sentence.split(" ")
    result = []
    for word in words:
        p1 = 0
        p2 = len(word)-1
        word = list(word)
        while p1 < p2:
            word[p1], word[p2] = word[p2], word[p1]
            p1 += 1
            p2 -= 1
        result.append("".join(word))
    return " ".join(result)

print(str_reverse(q1))
print(str_reverse(q2))