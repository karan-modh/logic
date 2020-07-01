def inputfn():
    n, mode = map(int, input().strip().split())
    sentences = []
    for i in range(0, n):
        sentences.append(input())

    result = input()
    return n, mode, sentences, result
