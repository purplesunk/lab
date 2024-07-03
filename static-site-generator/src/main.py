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
        if isinstance(node, TextNode):
            words = node.text.split()
            found_delimiter_start = False
            found_delimiter_end = False
            new_node = []

            for word in words:
                if found_delimiter_start:
                    if word.endswith(delimiter):
                        found_delimiter_end = True
                        new_node.append(word.rstrip(delimiter))
                        continue
                    new_node.append(word)

                if word.startswith(delimiter):
                    found_delimiter_start = True
                    new_node.append(word.lstrip(delimiter))

            if (found_delimiter_start 
                and not found_delimiter_end):
                raise Exception("Could not find matching closing delimiter in {node} with {delimiter}.")
            new_nodes.append(TextNode(" ".join(new_node), text_type))
        else:
            new_nodes.append(node)


def main():
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    print(new_nodes)

    tn = TextNode("This is a text node", "bold", "https://www.boot.dev") 
    print(tn)


main()
