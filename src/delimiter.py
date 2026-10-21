from textnode import TextNode, TextType



def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
	result = []
	for stuff in old_nodes:
		if stuff.text_type != TextType.plain:
			result.append(stuff)
			continue
		splits = stuff.text.split(delimiter)

		if len(splits) % 2 == 0:
			raise Exception(f"something went wrong with {delimiter}")

		for i, meme in enumerate(splits):
			if not meme:
				continue
			if i % 2 != 0:
				get_him = text_type
			else:
				get_him = TextType.plain
			result.append(TextNode(meme, get_him))
	return result

