import re

from functools import reduce

from textnode import TextNode
from htmlnode import HTMLNode 
from leafnode import LeafNode 
from parentnode import ParentNode 

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

block_type_paragraph = "paragraph"
block_type_code = "codeblock"
block_type_heading = "heading"
block_type_quote = "quoteblock"
block_type_ulist = "unordered list"
block_type_olist = "ordered list"

def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    if text_type == text_type_text:
        return LeafNode(None, text) 
    if text_type == text_type_bold:
        return LeafNode(b, text) 
    if text_type == text_type_italic:
        return LeafNode(i, text) 
    if text_type == text_type_code:
        return LeafNode(code, text) 
    if text_type == text_type_link:
        return LeafNode(a, text, {"href": text_node.url}) 
    if text_type == text_type_image:
        return LeafNode(img, "", {"alt": text_node.text, "src": text_node.url})

    raise Exception(f"Invalid text type in {text_node}.")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            splited_node = node.text.split(delimiter)

            if len(splited_node) % 2 == 0:
                raise Exception(f"Invalid Markdown Syntax: Could not find matching closing delimiter in {node} with {delimiter}.")

            for i in range(0, len(splited_node)):
                if splited_node[i] and i % 2 != 0: 
                    new_nodes.append(TextNode(splited_node[i], text_type))
                elif splited_node[i]:
                    new_nodes.append(TextNode(splited_node[i], text_type_text))
        else:
            new_nodes.append(node)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)

        if not images:
            new_nodes.append(node)
            continue

        new_node_list = []
        original_text = node.text
        for image_tup in images:
            splited_text = original_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if splited_text[0]:
                new_node_list.append(TextNode(splited_text[0], node.text_type))
            new_node_list.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
            original_text = splited_text[1];

        new_nodes.extend(new_node_list)
        if original_text:
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue

        new_node_list = []
        original_text = node.text
        for link_tup in links:
            splited_text = original_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if splited_text[0]:
                new_node_list.append(TextNode(splited_text[0], node.text_type))
            new_node_list.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
            original_text = splited_text[1];

        new_nodes.extend(new_node_list)
        if original_text:
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def text_to_textnodes(text):
    text_node = [TextNode(text, text_type_text)]
    nodes_code = split_nodes_delimiter(text_node, "`", text_type_code)
    nodes_bold = split_nodes_delimiter(nodes_code, "**", text_type_bold)
    nodes_italic = split_nodes_delimiter(nodes_bold, "*", text_type_italic)
    return split_nodes_link(split_nodes_image(nodes_italic))


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


def main():
    print("hola")

main()
