# Name: Ashish Sadavarti
# Code: Detect HTML Tags and Attributes
# Code Description: Parses HTML input to extract and print information about
#                   start tags and their attributes using Python's HTMLParser.
# Copyright 2025

# This script demonstrates how to use Python's built-in `html.parser.HTMLParser`
# to process HTML content. It defines a custom parser class that overrides
# the `handle_starttag` method. This method is automatically called by the parser
# whenever it encounters an opening HTML tag, allowing us to extract the tag name
# and its associated attributes.

from html.parser import HTMLParser # Import the HTMLParser class.

class MyHTMLParser(HTMLParser):
    """
    A custom HTML parser that inherits from HTMLParser.
    It overrides the handle_starttag method to print tag names and their attributes.
    """
    def handle_starttag(self, tag, attrs):
        """
        This method is called by the HTMLParser when an opening tag is encountered.

        Parameters:
        tag (str): The name of the HTML tag (e.g., 'div', 'a', 'p').
        attrs (list of tuples): A list of (attribute_name, attribute_value) tuples
                                found in the tag.
                                Example: [('href', 'example.com'), ('id', 'link1')]
        """
        # Print the name of the encountered HTML tag.
        print(tag)
        
        # Iterate through the list of attributes for the current tag.
        # Each 'attr' is a tuple like ('attribute_name', 'attribute_value').
        # Using a list comprehension for concise printing.
        # `*attr` unpacks the tuple into two arguments for `format`.
        for attr in attrs:
            print('-> {} > {}'.format(*attr))

if __name__ == '__main__':
    print("--- HTML Tag and Attribute Detector ---")
    print("Enter HTML lines. Press Enter twice to finish input.")

    try:
        # Read the number of lines of HTML input.
        # This is common in HackerRank problems.
        num_lines = int(input("Enter the number of HTML lines: "))
        
        # Read 'num_lines' lines of HTML input and join them into a single string.
        # .strip() is used to clean up potential whitespace on each line.
        html_lines = []
        print(f"Enter {num_lines} lines of HTML content:")
        for i in range(num_lines):
            html_lines.append(input())
        html_input = '\n'.join(html_lines)

        # Create an instance of our custom HTML parser.
        parser = MyHTMLParser()
        
        # Feed the HTML content to the parser.
        # The parser will process the HTML string and call appropriate handler methods
        # (like handle_starttag) as it encounters different HTML constructs.
        parser.feed(html_input)
        
        # Call close() to ensure all buffered data is processed and to release resources.
        parser.close()

    except ValueError:
        print("Invalid input. Please enter an integer for the number of HTML lines.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

