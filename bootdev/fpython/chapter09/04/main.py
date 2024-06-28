from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# don't touch above this line


def convert_format(content, from_format, to_format):
    match(from_format, to_format):
        case (DocFormat.TXT, DocFormat.PDF):
            return f"[PDF] {content} [PDF]"
        case (DocFormat.MD, DocFormat.HTML):
            return f"<h1>{content.lstrip("# ")}</h1>"
        case (DocFormat.HTML, DocFormat.MD):
            return f"# {content.replace("<h1>", "").replace("</h1>", "")}"
        case _:
            raise Exception("Invalid type")
