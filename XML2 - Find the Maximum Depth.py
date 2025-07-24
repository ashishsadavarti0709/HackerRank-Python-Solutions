# Name: Ashish Sadavarti
# Code: XMLMaximumDepthFinder
# Code Description: Recursively calculates the maximum depth of an XML tree
#                   (the longest path from the root to any leaf element).
# Copyright 2025

import xml.etree.ElementTree as ET # Import the ElementTree module for XML parsing

# Global variable to keep track of the maximum depth found so far.
# It's initialized to 0, implying that the root node itself is at level 0
# (or 1 depending on convention, but here the 'level' increments before checking).
maxdepth = 0

def depth(elem, level):
    """
    Recursively traverses an XML tree to find its maximum depth.

    Args:
        elem (xml.etree.ElementTree.Element): The current XML element being processed.
        level (int): The current depth level of 'elem' within the tree.
                    The root element is typically passed with level 0 or -1
                    to correctly calculate depth from 1 onwards.
    """
    global maxdepth # Declare that we are using the global 'maxdepth' variable.
    
    # Increment the level for the current element.
    # If the root is passed with level -1, its children will be level 0, then 1, etc.
    # If the root is passed with level 0, its children will be level 1, then 2, etc.
    level += 1
    
    # If the current level is greater than the recorded maximum depth, update maxdepth.
    # This ensures maxdepth always stores the deepest level reached.
    if level > maxdepth:
        maxdepth = level
        
    # Recursively call the 'depth' function for each child element.
    # The 'level' for the child will be the current 'level'.
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    # This block demonstrates how to use the depth function.
    # In a typical HackerRank problem, input XML lines would be read directly.

    # Read the number of lines of XML input.
    # This value indicates how many lines make up the full XML string.
    n = int(input("Enter number of XML lines: "))
    
    # Read all XML lines and join them into a single string.
    xml_lines = [input() for _ in range(n)]
    xml_string = "\n".join(xml_lines)

    try:
        # Parse the XML string into an ElementTree and get the root element.
        root = ET.fromstring(xml_string)
        
        # Call the depth function, starting with the root element and an initial level.
        # Initial level is typically -1 or 0 to account for root being at depth 0 or 1.
        # If maxdepth should be 0 for a root-only tree, start with -1.
        # If maxdepth should be 1 for a root-only tree, start with 0.
        # The common interpretation of "depth" in these problems implies number of edges from root.
        # If root is level 0, and its children are level 1, the maxdepth will reflect this.
        # Here, `level += 1` inside `depth` means if `depth(root, -1)` is called, root is level 0.
        # If a child of root exists, `depth(child, 0)` is called, child is level 1.
        # So, calling with -1 ensures depth starts counting from 0 for the root level.
        depth(root, -1)
        
        # Print the final maximum depth.
        print(f"Maximum depth of the XML tree: {maxdepth}")

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Example Input (for n=5):
    # <a>
    #     <b>
    #         <c></c>
    #     </b>
    #     <d></d>
    # </a>

    # Tree Structure and Levels (calling depth(root, -1)):
    # a (level 0)
    #   b (level 1)
    #     c (level 2)
    #   d (level 1)

    # Max depth reached is 2 (for element 'c').
    # Expected Output for the example:
    # Maximum depth of the XML tree: 2
