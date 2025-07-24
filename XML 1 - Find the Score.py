# Name: Ashish Sadavarti
# Code: XMLAttributeCounter
# Code Description: Recursively counts the total number of attributes across
#                   all elements in an XML tree.
# Copyright 2025

import xml.etree.ElementTree as ET # Import the ElementTree module for XML parsing

def get_attr_number(node):
    """
    Recursively calculates the total number of attributes for a given XML node
    and all its descendants.

    Args:
        node (xml.etree.ElementTree.Element): The current XML element (node) to process.

    Returns:
        int: The total count of attributes from this node and its entire subtree.
    """
    # Initialize the score with the number of attributes in the current node.
    # node.attrib is a dictionary-like object containing the attributes of the current element.
    # len(node.attrib) gives the number of key-value pairs (attributes) for this specific node.
    score = len(node.attrib)
    
    # Iterate over each child element of the current node.
    # This is where the recursion happens.
    for child in node:
        # For each child, recursively call get_attr_number to get the attribute count
        # for that child and its entire subtree.
        # Add the result of the recursive call to the current score.
        score += get_attr_number(child)
        
    # Return the accumulated score, which includes attributes from the current node
    # and all its descendants.
    return score

if __name__ == '__main__':
    # This block demonstrates how to use the get_attr_number function.
    # In a typical HackerRank problem, input XML lines would be read directly.

    # Read the number of lines of XML input.
    # This value indicates how many lines make up the full XML string.
    n = int(input("Enter number of XML lines: "))
    
    # Read all XML lines and join them into a single string.
    xml_lines = [input() for _ in range(n)]
    xml_string = "\n".join(xml_lines)

    try:
        # Parse the XML string into an ElementTree.
        # ET.ElementTree(ET.fromstring(xml_string)) creates a tree object.
        # ET.fromstring(xml_string) parses the string directly into the root element.
        tree = ET.ElementTree(ET.fromstring(xml_string))
        
        # Get the root element of the XML tree.
        root = tree.getroot()
        
        # Call the function to calculate the total number of attributes.
        total_attributes = get_attr_number(root)
        
        # Print the final score.
        print(f"Total number of attributes: {total_attributes}")

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Example Input (for n=6):
    # <a attribute1="value1" attribute2="value2">
    #     <b>
    #         <c attribute3="value3"></c>
    #     </b>
    #     <d attribute4="value4" attribute5="value5">
    #         <e></e>
    #     </d>
    # </a>

    # Explanation of Attributes:
    # Node 'a': 2 attributes (attribute1, attribute2)
    # Node 'b': 0 attributes
    # Node 'c': 1 attribute (attribute3)
    # Node 'd': 2 attributes (attribute4, attribute5)
    # Node 'e': 0 attributes
    # Total = 2 + 0 + 1 + 2 + 0 = 5

    # Expected Output for the example:
    # Total number of attributes: 5
