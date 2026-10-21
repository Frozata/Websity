from enum import Enum
from htmlnode import ParentNode, LeafNode

class TextType(Enum):
	plain = "text"
	bold = "bold"
	italic = "italic"
	code = "code"
	links = "link"
	images = "image"

class TextNode:
	def __init__(self, text, text_type, url = None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
    		return (
        		self.text == other.text
        		and self.text_type == other.text_type
			and self.url == other.url
    		)
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
	if text_node.text_type == TextType.plain:
		return LeafNode(None, text_node.text)
	elif text_node.text_type == TextType.bold:
                return LeafNode("b", text_node.text)
	elif text_node.text_type == TextType.italic:
                return LeafNode("i", text_node.text)
	elif text_node.text_type == TextType.code:
                return LeafNode("code", text_node.text)
	elif text_node.text_type == TextType.links:
                return LeafNode("a", text_node.text, {"href": text_node.url})
	elif text_node.text_type == TextType.images:
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
	else:
		raise Exception(f"invalid text type: {text_node.text_type}")

