#!env python

import json
import os, sys

books = os.listdir('books')
books = [{"filename": b, "name": b} for b in books]
with file("data/books.json", 'w') as f:
	json.dump(books, f, indent=4)