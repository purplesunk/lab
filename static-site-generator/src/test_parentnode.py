import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ],
                )

        node2 = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    node,
                    ],
                )

        node3 = ParentNode(
                "p",
                [
                    node,
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ],
                {"style": "text-align: center"}
                )

        node4 = ParentNode(
                "p",
                [
                    node2,
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ],
                {"style": "text-align: center"}
                )



        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        self.assertEqual(node2.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")
        self.assertEqual(node3.to_html(), "<p style=\"text-align: center\"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        self.assertEqual(node4.to_html(), "<p style=\"text-align: center\"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


if __name__ == "__main__":
    unittest.main()
