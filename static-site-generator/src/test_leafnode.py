import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "link", {"href": "https://archlinux.org"})
        node2 = LeafNode("p", "this is a paragraph")
        node3 = LeafNode("a", "link", {"href": "https://archlinux.org", "target": "_blank"})

        self.assertEqual(node.to_html(), "<a href=\"https://archlinux.org\">link</a>")
        self.assertEqual(node2.to_html(), "<p>this is a paragraph</p>")
        self.assertEqual(node3.to_html(), "<a href=\"https://archlinux.org\" target=\"_blank\">link</a>")



if __name__ == "__main__":
    unittest.main()
