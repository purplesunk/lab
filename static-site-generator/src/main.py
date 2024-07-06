import re
import os
import shutil

from textnode import TextNode
from htmlnode import HTMLNode 
from leafnode import LeafNode 
from parentnode import ParentNode 

from block import *
from inline import *

public = "public"
static = "static"


def recursive_copy(src, dst):
    if os.path.exists(src):
        if os.path.isdir(src):
            os.mkdir(src.replace(src, dst))
            src_list = list(map(lambda x: os.path.join(src, x), os.listdir(src)))
            dst_list = list(map(lambda x: x.replace(src, dst, 1), src_list))
            for i in range(0, len(src_list)):
                recursive_copy(src_list[i], dst_list[i])
        if os.path.isfile(src):
            print(f"{src} is being copied to {dst}")
            shutil.copy(src, dst)
            
            
def copy_from_static():
    if (os.path.exists(public) 
        and os.path.exists(static)):
        shutil.rmtree(public)
    recursive_copy(static, public)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("All pages should have an h1 heading")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        from_content = file.read()

    with open(template_path, "r") as file:
        template_content = file.read()

    title = extract_title(from_content)
    content = markdown_to_html_node(from_content).to_html()
    html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", content)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    file = open(dest_path, "w")
    file.write(html)
    file.close()


def main():
    copy_from_static()
    generate_page("content/index.md", "template.html", "public/index.html")

main()
