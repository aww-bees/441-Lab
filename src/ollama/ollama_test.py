import ollama
from numpy import dot 
from numpy.linalg import norm

paragraph = "She never liked cleaning the sink. It was beyond her comprehension how it got so dirty so quickly. It seemed that she was forced to clean it every other day. Even when she was extra careful to keep things clean and orderly, it still ended up looking like a mess in a couple of days. What she didn't know was there was a tiny creature living in it that didn't like things neat."
list = []
list = paragraph.split('. ')
inp = input('Ask a question\n')

sentence_map = [
    {"sentence": sentence.strip(), "embed": ollama.embeddings(model='llama2', prompt=sentence)["embedding"], "sim": 0} for sentence in list
]

inp_embed=ollama.embeddings(model='llama2', prompt=inp)["embedding"]


for this_sentence in sentence_map:
    this_sentence["sim"]=dot(this_sentence["embed"], inp_embed)/(norm(this_sentence["embed"])*norm(inp_embed))

sentence_map.sort(key=lambda x: ["sim"])

last_three = sentence_map[-3:]

best_sentences=last_three[0]["sentence"]+"\n"+ last_three[1]["sentence"]+ "\n"+last_three[2]["sentence"]

total = "CONTEXT:\n"+best_sentences+"\n QUERY: "+inp

text = ollama.generate(model='llama2', prompt=total)

print(total, "\n", text["response"])