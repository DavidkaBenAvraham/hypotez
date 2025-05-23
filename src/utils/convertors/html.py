## \file /src/utils/convertors/html.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.utils.convertors.html 
	:platform: Windows, Unix
	:synopsis: HTML conversion utilities
Functions:
    - `html2escape`: Convert HTML to escape sequences.
    - `escape2html`: Convert escape sequences to HTML.
    - `html2dict`: Convert HTML to dictionaries.
    - `html2ns`: Convert HTML to SimpleNamespace objects.
    https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
"""

import re
from typing import Dict
from pathlib import Path
from venv import logger

from src.logger.logger import logger
from types import SimpleNamespace
from html.parser import HTMLParser
from xhtml2pdf import pisa
import subprocess
from pathlib import Path
from src.logger import logger
import os

try:
    from weasyprint import HTML
except Exception as ex:
    logger.error(ex)
    ...

def html2escape(input_str: str) -> str:
    """
    Convert HTML to escape sequences.

    Args:
        input_str (str): The HTML code.

    Returns:
        str: HTML converted into escape sequences.

    Example:
        >>> html = "<p>Hello, world!</p>"
        >>> result = html2escape(html)
        >>> print(result)
        &lt;p&gt;Hello, world!&lt;/p&gt;
    """
    return StringFormatter.escape_html_tags(input_str)

def escape2html(input_str: str) -> str:
    """
    Convert escape sequences to HTML.

    Args:
        input_str (str): The string with escape sequences.

    Returns:
        str: The escape sequences converted back into HTML.

    Example:
        >>> escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
        >>> result = escape2html(escaped)
        >>> print(result)
        <p>Hello, world!</p>
    """
    return StringFormatter.unescape_html_tags(input_str)

def html2dict(html_str: str) -> Dict[str, str]:
    """
    Convert HTML to a dictionary where tags are keys and content are values.

    Args:
        html_str (str): The HTML string to convert.

    Returns:
        dict: A dictionary with HTML tags as keys and their content as values.

    Example:
        >>> html = "<p>Hello</p><a href='link'>World</a>"
        >>> result = html2dict(html)
        >>> print(result)
        {'p': 'Hello', 'a': 'World'}
    """
    class HTMLToDictParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.result = {}
            self.current_tag = None

        def handle_starttag(self, tag, attrs):
            self.current_tag = tag

        def handle_endtag(self, tag):
            self.current_tag = None

        def handle_data(self, data):
            if self.current_tag:
                self.result[self.current_tag] = data.strip()

    parser = HTMLToDictParser()
    parser.feed(html_str)
    return parser.result

def html2ns(html_str: str) -> SimpleNamespace:
    """
    Convert HTML to a SimpleNamespace object where tags are attributes and content are values.

    Args:
        html_str (str): The HTML string to convert.

    Returns:
        SimpleNamespace: A SimpleNamespace object with HTML tags as attributes and their content as values.

    Example:
        >>> html = "<p>Hello</p><a href='link'>World</a>"
        >>> result = html2ns(html)
        >>> print(result.p)
        Hello
        >>> print(result.a)
        World
    """
    html_dict = html2dict(html_str)
    return SimpleNamespace(**html_dict)

# def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
#     """Converts HTML content to a PDF file after removing unsupported CSS pseudo-selectors.
    
#     Args:
#         html_str (str): HTML content as a string.
#         pdf_file (str | Path): Path to the output PDF file.
    
#     Returns:
#         bool | None: Returns `True` if PDF generation is successful; `None` otherwise.
#     """
#     ...
#     def preprocess_css(css_content: str) -> str:
#         """
#         Remove unsupported pseudo-classes and simplify CSS for xhtml2pdf.
    
#         Args:
#             css_content (str): Original CSS content.

#         Returns:
#             str: Preprocessed CSS content without unsupported selectors.
#         """
#         # Убираем `:not(...)`
#         css_content = re.sub(r':not\([^)]*\)', '', css_content)

#         return css_content
#     # Убираем неподдерживаемые псевдоклассы, если они есть
#     html_str = preprocess_css(html_str)

#     with open(pdf_file, "wb") as f:
#         pisa_status = pisa.CreatePDF(html_str, dest=f)

#     if pisa_status.err:
#         print("Error during PDF generation")
#         return
#     else:
#         return True




def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Converts HTML content to a PDF file using WeasyPrint."""
    try:
        HTML(string=html_str).write_pdf(pdf_file)
        return True
    except Exception as e:
        print(f"Error during PDF generation: {e}")
        return


def html_to_docx(html_file: str, output_docx: Path | str) -> bool:
    """Converts an HTML file to a Word document using LibreOffice.

    Args:
        html_file (str): Path to the input HTML file as a string.
        output_docx (Path | str): Path to the output DOCX file.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        # Ensure the html_file exists
        if not os.path.exists(html_file):
            logger.error(f"HTML file not found: {html_file}")
            return False

        # Ensure output directory exists
        output_dir = Path(output_docx).parent
        if not output_dir.exists():
            os.makedirs(output_dir)

        # Construct the command for LibreOffice
        command = [
            "soffice",
            "--headless",  # Run LibreOffice in headless mode
            "--convert-to",
            "docx:HTML", # Specify that input is HTML
            html_file, # use html_file as is
            "--outdir",
            str(output_dir)
        ]

        # Execute the LibreOffice command
        process = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )

        # Check for any errors outputted in the process output
        if process.stderr:
           logger.error(f"LibreOffice conversion errors: {process.stderr}")

        return True

    except subprocess.CalledProcessError as ex:
        logger.error(f"LibreOffice failed to convert HTML file: {html_file} to DOCX file: {output_docx}. Error: {ex.stderr}", exc_info=True)
        return False
    except FileNotFoundError:
        logger.error(f"LibreOffice executable (soffice) not found. Ensure it is installed and in your system's PATH.", exc_info=True)
        return False
    except Exception as ex:
        logger.error(f"An unexpected error occurred during conversion. Error: {ex}", exc_info=True)
        return False



