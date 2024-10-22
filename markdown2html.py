#!/usr/bin/python3
"""
A python script that converts Markdown to HTML.
"""

import sys
import os
import re


def convert_markdown_to_html(my_input, my_output):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """

    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not (os.path.exists(my_input) and os.path.isfile(my_input)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(my_input, encoding="utf-8") as f:
        html_lines = []
        for line in f:
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(
                        f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                html_lines.append(line.rstrip())

    # Write the HTML output to a file
    with open(my_output, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))


if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print(
                "Usage: ./markdown2html.py <input_file> <output_file>",
                file=sys.stderr)
        sys.exit(1)

    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(my_input, my_output)

    # Exit with a successful status code
    sys.exit(0)
