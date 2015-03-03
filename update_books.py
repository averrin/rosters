#!env python

import json
import os, sys
import io

books = os.listdir('books')
present = json.load(io.open("data/books.json", 'r', encoding='utf8'), encoding='utf8')
for b in books:
	b = b.encode("utf8")
	ishere = b in [p['filename'] for p in present]
	if not ishere:
		present.append({"filename": b, "name": b})

for b in present[:]:
	if b['filename'] not in books:
		present.remove(b)
		pass

print(present)
with io.open("data/books.json", 'w', encoding='utf8') as f:
	dump = json.dumps(present, indent=4, ensure_ascii=False, encoding="utf-8") #.decode("utf8")
	f.write(dump)