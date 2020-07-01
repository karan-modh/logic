from helper.inpTake import inputfn
from helper.convertToCNF import convert_to_cnf
from helper.resolution import resolve, print_sentences

n, mode, sentences, result = inputfn()

if len(result) == 1:
    result = '!'+result
elif len(result) == 2:
    result = result[1:]
else:
    result = '!' + '(' + result + ')'

sentences.append(result)
sentence_trees, modified_sentences = convert_to_cnf(sentences)

sentences = modified_sentences.copy()
for i in range(len(modified_sentences)):
    modified_sentences[i] = modified_sentences[i].split('|')

print("After Converting To CNF")
for x in sentences:
    print(x)
# for x in modified_sentences:
#     print(x)
print("--------------")

ans = resolve(modified_sentences)
# print_sentences(modified_sentences)
print(ans)
