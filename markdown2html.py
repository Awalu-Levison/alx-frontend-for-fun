#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import os
import re


def convert_markdown_to_html(input1, output1):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    if not (os.path.exists(input1) and os.path.isfile(input1)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_file, encoding="utf-8") as f:
            html_output = []
            for line in f:
                match = re.match(r"^(#+) (.*)$", line)
                if match:
                    heading_level = len(match.group(1))
                    heading_text = match.group(2)
                    html_output.append(
                        f"<h{heading_level}>{heading_text}</h{heading_level}>")
                else:
                    html_output.append(line.rstrip())
    except Exception as e:
        print(f"Error reading {input1}: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(output1, "w", encoding="utf-8") as f:
            f.write("\n".join(html_output))
    except Exception as e:
        print(f"Error writing to {output2}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            f"Error: Expected 2 arguments, but got {len(sys.argv) - 1}.",
            file=sys.stderr)
        print("Usage: ./markdown2html.py <input1> <output1>", file=sys.stderr)
        sys.exit(1)

    input1 = sys.argv[1]
    output1 = sys.argv[2]

    convert_markdown_to_html(input1, output1)
