import re

from textnode import TextNode
from htmlnode import HTMLNode 
from leafnode import LeafNode 
from parentnode import ParentNode 

from inline import text_node_to_html_node, text_to_textnodes

block_type_paragraph = "paragraph"
block_type_code = "codeblock"
block_type_heading = "heading"
block_type_quote = "quoteblock"
block_type_ulist = "unordered list"
block_type_olist = "ordered list"

def markdown_to_blocks(markdown):
    lines = list(map(lambda s: s.strip(), markdown.split("\n")))

    block = []
    blocks = []
    for line in lines:
        if not line and block:
            blocks.append("\n".join(block))
            block = []
        if line:
            block.append(line)

    if block:
        blocks.append("\n".join(block))

    return blocks


def block_to_block_type(block):
    if (block.startswith("```")
        and block.endswith("```")):
        return block_type_code

    lines = block.split("\n")
    if (re.search(r"^#{1,6} ", block)
        and len(lines) == 1):
        return block_type_heading

    if all(line.startswith("> ") for line in lines):
        return block_type_quote
    if all(line.startswith(("* ", "- ")) for line in lines):
        return block_type_ulist

    olist = True
    for i in range(0, len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            olist = False
    if olist:
        return block_type_olist
    return block_type_paragraph


def block_to_blockquote(block):
    text = " ".join(list(map(lambda x: x.replace("> ", "", 1), block.split("\n"))))
    children = list(map(text_node_to_html_node, text_to_textnodes(text)))
    return ParentNode("blockquote", children)

def text_to_li(text):
    children = list(map(text_node_to_html_node, text_to_textnodes(text)))
    return ParentNode("li", children)

def block_to_ul(block):
    children = list(map(lambda x: text_to_li(x[2:]), block.split("\n")))
    return ParentNode("ul", children)

def block_to_ol(block):
    children = list(map(lambda x: text_to_li(x[2:]), block.split("\n")))
    return ParentNode("ol", children)

def block_to_code(block):
    return ParentNode("pre", [ParentNode("code", [LeafNode(None, block[4:-3])])])

def block_to_heading(block):
    heading = block.split(" ", 1)
    heading_text = heading[1]
    heading_number = len(heading[0])
    children = list(map(text_node_to_html_node, text_to_textnodes(heading_text)))
    return ParentNode(f"h{heading_number}", children)


def block_to_paragraph(block):
    children = list(map(text_node_to_html_node, text_to_textnodes(block)))
    return ParentNode("p", children)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            html_nodes.append(block_to_paragraph(block))
        elif block_type == block_type_code:
            html_nodes.append(block_to_code(block))
        elif block_type == block_type_heading:
            html_nodes.append(block_to_heading(block))
        elif block_type == block_type_quote:
            html_nodes.append(block_to_blockquote(block))
        elif block_type == block_type_ulist:
            html_nodes.append(block_to_ul(block))
        elif block_type == block_type_olist:
            html_nodes.append(block_to_ol(block))
        else:
            raise Exception(f"Block:\n{block}\n\nwith invalid block_type: {block_type}.")
    return ParentNode("div", html_nodes)
