import unittest

from main import *
from textnode import TextNode
from htmlnode import HTMLNode 
from leafnode import LeafNode 
from parentnode import ParentNode 



class TestMain(unittest.TestCase):
    def test_eq(self):

        # Test Split delimiter
        node = TextNode("This is text with a `code block` word", text_type_text)
        node2 = TextNode("`This is text with a code` block `word`", text_type_text)
        node3 = TextNode("`This is text with a code block word`", text_type_text)
        node4 = TextNode("*This is text with a *code block* word*", text_type_text)
        node5 = TextNode("**This is text with a code block*** word*", text_type_text)

        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        split_nodes_delimiter([node4], "*", text_type_italic)
        split_nodes_delimiter([node4], "**", text_type_bold)

        self.assertEqual(new_nodes, [TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text)])

        # Test Images and Links regexs
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text), [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text), [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

        node = TextNode(
                "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                text_type_text,
                )

        self.assertEqual(split_nodes_image([node]), [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                ),
            ])

        # Test text to textnode
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

        self.maxDiff = None
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
            ])

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
