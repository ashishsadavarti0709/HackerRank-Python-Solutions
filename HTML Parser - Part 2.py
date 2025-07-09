# Name: Ashish Sadavarti
# Code: HTML Parser - Part 2: Comments and Data
# Code Description: Parses HTML input to detect and print HTML comments (single/multi-line)
#                   and non-empty data (text content) within the HTML structure.
# Copyright 2025

# This script continues the demonstration of Python's `html.parser.HTMLParser`.
# In this part, it focuses on handling two other common HTML components:
# - `handle_comment`: For HTML comments (`<!-- ... -->`). It distinguishes between
#   single-line and multi-line comments.
# - `handle_data`: For the actual text content (data) found between tags.
#   It specifically filters out newlines that might be treated as data by the parser.

from html.parser import HTMLParser # Import the HTMLParser class.

class MyHTMLParser(HTMLParser):
    """
    A custom HTML parser that inherits from HTMLParser.
    It overrides methods to print specific messages when HTML comments and data are encountered.
    """
    
    def handle_comment(self, comment):
        """
        Called when the parser encounters an HTML comment (`<!-- ... -->`).
        
        Parameters:
        comment (str): The content of the comment (excluding `<!--` and `-->`).
        """
        # Check if the comment string contains a newline character.
        # This is a simple way to differentiate between single-line and multi-line comments.
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        
        # Print the actual content of the comment.
        print(comment)

    def handle_data(self, data):
        """
        Called when the parser encounters plain text data within HTML tags.
        
        Parameters:
        data (str): The text content found.
        """
        # HTMLParser might sometimes report pure newline characters as data.
        # This check filters out such cases to focus on meaningful text data.
        if data.strip() == '': # More robust check for empty/whitespace-only data
             return
        
        print('>>> Data') # Print that data was found.
        # Print the actual text data.
        print(data)
    
    # It's good practice to also include other handlers from Part 1 if needed for full parsing.
    # For this specific problem, only comments and data are the focus.
    # def handle_starttag(self, tag, attrs): pass
    # def handle_endtag(self, tag): pass
    # def handle_startendtag(self, tag, attrs): pass

if __name__ == '__main__':
    print("--- HTML Parser - Part 2: Comments and Data ---")
    print("This program parses HTML input to detect comments and text data.")
    
    html_content = "" # Initialize an empty string to accumulate all HTML input.
    
    try:
        # Read the number of lines of HTML input.
        num_lines = int(input("Enter the number of HTML lines to parse: "))

        if num_lines < 0:
            print("Number of lines cannot be negative.")
            exit()

        print(f"\nEnter {num_lines} lines of HTML content:")
        # Loop 'num_lines' times to read each line of HTML.
        for i in range(num_lines):
            # Read a line, remove trailing whitespace (rstrip()), and append it to `html_content`.
            # A newline character is added after each line to maintain structure,
            # which is important for multi-line comments and data separation by the parser.
            html_content += input().rstrip()
            html_content += '\n'
        
        # Create an instance of our custom HTML parser.
        parser = MyHTMLParser()
        
        # Feed the entire accumulated HTML content to the parser.
        parser.feed(html_content)
        
        # Call close() to ensure all buffered data is processed.
        parser.close()

    except ValueError:
        print("Invalid input. Please enter an integer for the number of HTML lines.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

