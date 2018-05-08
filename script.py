#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pymorphy2
import json
import sys

word = sys.argv[1]
morph = pymorphy2.MorphAnalyzer()
data = morph.parse(word)[0].lexeme
i = 0
data_list = []
# data1 = { 'hello': 'foo' }
# json.dumps(data1)
for d in data:
	i = i + 1
	data_list.append(d.word)

print(i)

result = { 'hello': data_list }
with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(result, outfile, ensure_ascii=False)
# print(data.inflect({'gent'}))