#!/usr/bin/python3
"""
A python script that converts Markdown to HTML.
"""

import sys
import os
import re


def convert_markdown_to_html(a, b):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    a: input file
    b: output file
    """

    # Get the input and output file names from the command-line arguments
    a = sys.argv[1]
    b = sys.argv[2]

    if not (os.path.exists(a) and os.path.isfile(a)):
        print(f"Missing {a}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(a, encoding="utf-8") as f:
        my_html = []
        for line in f:
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                my_html.append(
                        f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                my_html.append(line.rstrip())

    # Write the HTML output to a file
    with open(b, "w", encoding="utf-8") as f:
        f.write("\n".join(my_html))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <a> <b>", file=sys.stderr)
        sys.exit(1)

    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(a, b)

    # Exit with a successful status code
    sys.exit(0)
