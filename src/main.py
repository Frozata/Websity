import textnode
from copystatic import website_generation
from gencontent import generate_pages_recursive
import os
import shutil

def main():
	dir_path_public = "./public"

	if os.path.exists(dir_path_public):
		shutil.rmtree(dir_path_public)

	website_generation("./static", "./public")

	generate_pages_recursive("content", "./template.html", "public")


main()
