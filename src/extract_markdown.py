import re
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def extract_markdown_images(text):
	matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
	return matches

def extract_markdown_links(text):
	matchups = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
	return matchups


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
	result = []
	for img in old_nodes:
		if img.text_type != TextType.plain:
			result.append(img)
			continue

		images = extract_markdown_images(img.text)
		if images == []:
			result.append(img)
			continue

		remaining_text = img.text

		for alt, url in images:
			marker = f"![{alt}]({url})"
			sections = remaining_text.split(marker, 1)
			remaining_text = sections[1]
			if sections[0] != "":
				result.append(TextNode(sections[0], TextType.plain))
			alturl = TextNode(alt, TextType.images, url)
			result.append(alturl)
		if remaining_text != "":
			result.append(TextNode(remaining_text, TextType.plain))

	return result

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:

	result = []
	for link in old_nodes:
		if link.text_type != TextType.plain:
			result.append(link)
			continue

		links = extract_markdown_links(link.text)

		if links == []:
			result.append(link)
			continue

		remaining_text = link.text
		for anchor, url in links:
			marker = f"[{anchor}]({url})"
			sections = remaining_text.split(marker, 1)
			remaining_text = sections[1]
			if sections[0] != "":
				result.append(TextNode(sections[0], TextType.plain))
			alturl = TextNode(anchor, TextType.links, url)
			result.append(alturl)
		if remaining_text != "":
			result.append(TextNode(remaining_text, TextType.plain))
	return result

def text_to_textnodes(text):
	listings = [TextNode(text, TextType.plain)]
	listings = split_nodes_delimiter(listings, "**", TextType.bold)
	listings = split_nodes_delimiter(listings, "_", TextType.italic)
	listings = split_nodes_delimiter(listings, "`", TextType.code)
	listings = split_nodes_image(listings)
	listings = split_nodes_link(listings)
	return listings

