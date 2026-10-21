import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

	def test_tag(self):
		default = HTMLNode()
		self.assertEqual(default.tag, None)

	def test_value(self):
                default = HTMLNode()
                self.assertEqual(default.value, None)

	def test_children(self):
                default = HTMLNode()
                self.assertEqual(default.children, None)

	def test_props(self):
                default = HTMLNode()
                self.assertEqual(default.props, None)

	def test_leaf_to_html_p(self):
    		node = LeafNode("p", "Hello, world!")
    		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)
