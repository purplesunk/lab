from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode with no tag.")

        if not self.children:
            raise ValueError("ParentNode with no children.")

        print(self.children)

        html = f"<{self.tag}{self.props_to_html()}>"
        for child_node in self.children:
            html = html + child_node.to_html()
        
        html = html + f"</{self.tag}>"

        return html
