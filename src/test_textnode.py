import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)

    def test_Noteq(self):
        node = TextNode("This is a text node", TextType.bold)
        node3 = TextNode("This is not a text node", TextType.bold)
        self.assertNotEqual(node, node3)

    def test_url_none(self):
        mehnode = TextNode("This is a text node", TextType.bold)
        self.assertIsNone(mehnode.url)

    def test_TextType(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.italic)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
