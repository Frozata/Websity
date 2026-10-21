import textnode
from copystatic import website_generation
from gencontent import generate_pages_recursive
import os
import shutil
import sys


def main():
	basepath = "/"
	if len(sys.argv) > 1:
		basepath = sys.argv[1]
	dir_path_docs = "./docs"

	if os.path.exists(dir_path_docs):
		shutil.rmtree(dir_path_docs)

	website_generation("./static", "./docs")

	generate_pages_recursive("content", "./template.html", "docs", basepath)





main()


