#!env python

import json
import os, sys

books = os.listdir('books')
present = json.load(file("data/books.json", 'r'))
for b in books:
	ishere = b in [p['filename'] for p in present]
	if not ishere:
		present.append({"filename": b, "name": b})

for b in present[:]:
	if b['filename'] not in books:
		present.remove(b)

with file("data/books.json", 'w') as f:
	json.dump(present, f, indent=4, ensure_ascii=False, encoding="utf-8")