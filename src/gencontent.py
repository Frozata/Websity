import os
from markdown_blocks import markdown_to_html_node
from pathlib import Path

def extract_title(markdown):
	lines = markdown.split("\n")

	for line in lines:

		if line.startswith("# "):
			clean = line.lstrip("#").strip()
			return clean

	raise Exception("no h1")


def generate_page(from_path, template_path, dest_path):
	print(f"Generating page {from_path} to {dest_path} using {template_path}.")
	with open(from_path) as f:
		markdown_content = f.read()

	with open(template_path) as v:
		markdown_template = v.read()
	htmlnode = markdown_to_html_node(markdown_content)
	html = htmlnode.to_html()
	title = extract_title(markdown_content)
	markdown_template = markdown_template.replace("{{ Title }}", title)
	markdown_template = markdown_template.replace("{{ Content }}", html)
	dir_path = os.path.dirname(dest_path)
	os.makedirs(dir_path, exist_ok=True)
	with open(dest_path, "w") as f:
		f.write(markdown_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	content = os.listdir(dir_path_content);
	for i in content:
		source_path = os.path.join(dir_path_content, i)
		dest_path = os.path.join(dest_dir_path, i)
		path_html = Path(dest_path).with_suffix(".html")
		if os.path.isfile(source_path):
			generate_page(source_path, template_path, path_html)
		else:
			generate_pages_recursive(source_path, template_path, dest_path)
