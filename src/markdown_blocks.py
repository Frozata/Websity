from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode, LeafNode
from enum import Enum
from extract_markdown import text_to_textnodes

def markdown_to_blocks(markdown):
        cleaned = []
        blocks = markdown.strip().split("\n\n")
        for e in blocks:
                e = e.strip()
                if e != "":
                        cleaned.append(e)
        return cleaned

class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE =	"quote"
	UNORDERED_LIST = "unordered_list"
	ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
	if markdown.startswith(("# ","## ","### ", "#### ", "##### ", "###### ")):
		return BlockType.HEADING
	lines = markdown.split("\n")
	if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
		return BlockType.CODE
	all_good = True
	for i in lines:
		if not i.startswith(">"):
			all_good = False
			break
	if all_good == True:
		return BlockType.QUOTE
	chaos = True
	for j in lines:
		if not j.startswith("- "):
			chaos = False
			break
	if chaos == True:
		return BlockType.UNORDERED_LIST
	orders = 0
	court = True
	for k in lines:
		orders += 1
		if not k.startswith(f"{orders}. "):
			court = False
			break
	if court == True:
		return BlockType.ORDERED_LIST
	return BlockType.PARAGRAPH

def text_to_children(text):
	children = []
	text_nodes = text_to_textnodes(text)
	for i in text_nodes:
		convert = text_node_to_html_node(i)
		children.append(convert)
	return children

def markdown_to_html_node(markdown):
	blocks = markdown_to_blocks(markdown)
	HTMLN = []
	for i in blocks:
		blocktype = block_to_block_type(i)
		if blocktype.value == "paragraph":
			children = text_to_children(i)
			dis = ParentNode("p", children)
			HTMLN.append(dis)
		elif blocktype.value == "heading":
			count = 0
			clean = i.lstrip("#").strip()
			children = text_to_children(clean)
			for b in i:
				if b == "#":
					count += 1
				else:
					break
			dis = ParentNode(f"h{count}", children)
			HTMLN.append(dis)
		elif blocktype.value == "code":
			cole = i[3:]
			cole = cole.lstrip("\n")
			cole = cole [:-3]
			text_node = TextNode(cole, TextType.code)
			HTMLNode = text_node_to_html_node(text_node)
			wut = ParentNode("code", [HTMLNode])
			meh = ParentNode("pre", [HTMLNode])
			HTMLN.append(meh)
		elif blocktype.value == "quote":
			quote = i.split("\n")
			new_lines = []
			for b in quote:
				if b.startswith(">"):
					b = b[2:]
					new_lines.append(b)
			quote_text = " ".join(new_lines)
			children = text_to_children(quote_text)
			dis = ParentNode("blockquote", children)
			HTMLN.append(dis)

		elif blocktype.value == "unordered_list":
			lines = i.split("\n")
			stuff = []
			for line in lines:
				line = line[2:]
				line_children = text_to_children(line)
				lest = ParentNode("li", line_children)
				stuff.append(lest)
			unordered = ParentNode("ul", stuff)
			HTMLN.append(unordered)
		elif blocktype.value == "ordered_list":
			lines = i.split("\n")
			staff = []
			for line in lines:
				line = line.split(". ")
				line = line[1:]
				joined = ". ".join(line)
				line_children = text_to_children(joined)
				last = ParentNode("li", line_children)
				staff.append(last)
			ordered = ParentNode("ol", staff)
			HTMLN.append(ordered)
	html = ParentNode("div", HTMLN)
	return html
