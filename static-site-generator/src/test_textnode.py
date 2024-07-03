import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is an img", "bold", "img.jpg")
        node4 = TextNode("This is an img", "bold", "img.jpg")
        node5 = TextNode("This is some link", "bold", "https://hello.com")
        node6 = TextNode("This is a text...", "bold")
        node7 = TextNode("This is a text node", "italic")

        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node3, node5)
        self.assertNotEqual(node, node6)
        self.assertNotEqual(node, node7)


if __name__ == "__main__":
    unittest.main()
