# Name: Ashish Sadavarti
# Code: HTML Parser - Part 1: Tag Detection
# Code Description: Parses HTML input to detect and print start tags, end tags,
#                   and empty (self-closing) tags along with their attributes.
# Copyright 2025

# This script introduces the basic usage of Python's `html.parser.HTMLParser`
# by subclassing it and overriding key handler methods.
# It demonstrates how to capture and report on:
# - `handle_starttag`: For opening tags like `<div>` or `<a href="...">`
# - `handle_endtag`: For closing tags like `</div>` or `</a>`
# - `handle_startendtag`: For self-closing (empty) tags like `<img src="..." />` or `<br>`

from html.parser import HTMLParser # Import the HTMLParser class.

class MyHTMLParser(HTMLParser):
    """
    A custom HTML parser that inherits from HTMLParser.
    It overrides methods to print specific messages when different types of HTML tags are encountered.
    """
    
    def handle_starttag(self, tag, attrs):
        """
        Called when the parser encounters an opening tag (e.g., `<div>`, `<a href="...">`).
        
        Parameters:
        tag (str): The name of the HTML tag (e.g., 'div', 'a').
        attrs (list of tuples): A list of (attribute_name, attribute_value) tuples.
        """
        print('Start :', tag) # Print that a start tag was found, along with its name.
        # Iterate through the attributes of the start tag.
        # Each 'ele' is a tuple (attribute_name, attribute_value).
        for ele in attrs:
            # Print the attribute name and its value.
            print('->', ele[0], '>', ele[1])

    def handle_endtag(self, tag):
        """
        Called when the parser encounters a closing tag (e.g., `</div>`, `</a>`).
        
        Parameters:
        tag (str): The name of the HTML tag.
        """
        print('End   :', tag) # Print that an end tag was found, along with its name.

    def handle_startendtag(self, tag, attrs):
        """
        Called when the parser encounters an empty (self-closing) tag (e.g., `<img />`, `<br>`).
        
        Parameters:
        tag (str): The name of the HTML tag.
        attrs (list of tuples): A list of (attribute_name, attribute_value) tuples.
        """
        print('Empty :', tag) # Print that an empty tag was found, along with its name.
        # Iterate through the attributes of the empty tag, similar to handle_starttag.
        for ele in attrs:
            print('->', ele[0], '>', ele[1])

if __name__ == '__main__':
    print("--- HTML Parser - Part 1 ---")
    print("This program parses HTML input to report on various tag types and their attributes.")
    
    # Create an instance of our custom HTML parser.
    parser = MyHTMLParser()
    
    try:
        # Read the number of lines of HTML input.
        num_lines = int(input("Enter the number of HTML lines to parse: "))

        if num_lines < 0:
            print("Number of lines cannot be negative.")
            exit()

        print(f"\nEnter {num_lines} lines of HTML content:")
        # Loop 'num_lines' times to read and feed each line of HTML to the parser.
        for i in range(num_lines):
            html_line = input() # Read a single line of HTML.
            # Feed the HTML line to the parser.
            # The parser processes the string and calls the appropriate handler methods.
            parser.feed(html_line)
        
        # After all lines are fed, call close() to ensure any buffered data is processed.
        parser.close()

    except ValueError:
        print("Invalid input. Please enter an integer for the number of HTML lines.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

