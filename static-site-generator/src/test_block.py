import unittest

from block import *
from textnode import TextNode
from htmlnode import HTMLNode 
from leafnode import LeafNode 
from parentnode import ParentNode 

class TestMain(unittest.TestCase):
    def test_eq(self):
        codeblock = "```\nint hola() {\n\tint a = 2;\n int b = 43;\n return a + b;\n}\n```"
        self.assertEqual(block_to_block_type(codeblock), block_type_code)
        quoteblock = "> Something\n> Instant\n> Uaa\n> Think"
        self.assertEqual(block_to_block_type(quoteblock), block_type_quote)
        ulistblock = "* Something\n* Instant\n* Uaa\n* Think"
        self.assertEqual(block_to_block_type(ulistblock), block_type_ulist)
        olistblock = "1. Something\n2. Instant\n3. Uaa\n4. Think"
        self.assertEqual(block_to_block_type(olistblock), block_type_olist)
        heading = "## An insane heading"
        self.assertEqual(block_to_block_type(heading), block_type_heading)
        heading = "# An insane heading"
        self.assertEqual(block_to_block_type(heading), block_type_heading)
        bad = "1. Something\n* Instant\n* Uaa\n2. Think"
        self.assertEqual(block_to_block_type(bad), block_type_paragraph)

        markdown = """# This is a heading

This is a paragraph of text.

* This is a list item
* This is another list item"""

        #insane = ParentNode("div", [ParentNode("h1", [LeafNode(None, "This is a heading")]), ParentNode("p", [LeafNode(None, "This is a paragraph of text.")]), ParentNode("ul", [ParentNode("li", [LeafNode(None, "This is a list item")]), ParentNode("li", [LeafNode(None, "This is another list item")])])])


        #self.assertEqual(markdown_to_html_node(markdown), insane)


if __name__ == "__main__":
    unittest.main()
