from helper.inpTake import inputfn
from helper.convertToCNF import convert_to_cnf
from helper.parser import parse
from helper.resolution import resolution

n, mode, sentences, result = inputfn()

if not len(sentences):
    print(1)
    exit(1)

if len(result) == 1:
    result = '!' + result
elif len(result) == 2:
    result = result[1:]
else:
    result = '!' + '(' + result + ')'

sentences.append(result)
expressions = []
for sentence in sentences:
    expr = parse(sentence)
    expressions.append(expr)

modified_sentences = convert_to_cnf(expressions)

sentences = modified_sentences.copy()
for i in range(len(modified_sentences)):
    modified_sentences[i] = modified_sentences[i].split('|')

if mode:
    print("After Converting To CNF")
    for x in sentences:
        print(x)
    print("--------------")

# for x in modified_sentences:
#     print(x)

ans = resolution(modified_sentences, mode)
# print_sentences(modified_sentences)
print(ans)