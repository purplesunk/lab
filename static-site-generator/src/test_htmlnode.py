import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "link", None, {"href": "https://archlinux.org"})
        node2 = HTMLNode("p", "this is a paragraph")
        node3 = HTMLNode("a", "link", None, {"href": "https://archlinux.org", "target": "_blank"})

        self.assertEqual(node.props_to_html(), " href=\"https://archlinux.org\"")
        self.assertEqual(node2.props_to_html(), "")
        self.assertEqual(node3.props_to_html(), " href=\"https://archlinux.org\" target=\"_blank\"")



if __name__ == "__main__":
    unittest.main()
