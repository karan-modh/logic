

def print_sentences(sentences):
    for sentence in sentences:
        if len(sentence) == 0:
            print("")
            continue
        pr_str = sentence[0]
        for i in range(1, len(sentence)):
            pr_str += "|" + sentence[i]
        print(pr_str)
    print("###############")


def resolve(sentences):
    changed = True
    while changed:
        changed = False
        for i in range(len(sentences)):
            if len(sentences[i]) == 1:
                temp = sentences[i][0]
                if len(temp) == 2:
                    var = temp[1]
                else:
                    var = "!" + temp
                for j in range(len(sentences)):
                    if var in sentences[j]:
                        sentences[j].remove(var)
                        print("performed r", i+1, " and r", j+1)
                        changed = True
                        if len(sentences[j]) == 0:
                            return 1
                        print_sentences(sentences)
                    else:
                        continue
    return 0
