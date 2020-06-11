def solution(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - 97] += 1
    print (occurrences)
    best_char = 'a'
    best_res = occurrences[0]

    for x in range(1, 26):
        if occurrences[x] >= best_res:
            best_char = chr(x+97)
            best_res = occurrences[x]

    return best_char


def main():
    print(solution("hello"))


if __name__ == '__main__':
    main()
