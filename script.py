import pymorphy2
import json
morph = pymorphy2.MorphAnalyzer()
data = morph.parse('стали')[0].lexeme
i = 0

# for d in data:
# 	i = i + 1
# 	print(d.word)

# print(i)
# print(data.inflect({'gent'}))