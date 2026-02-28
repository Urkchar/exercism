"""SGF Parsing"""


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    """Parses and SGF string and returns a tree structure of properties"""

    # Input cannot be empty
    if input_string == "":
        raise ValueError("Input cannot be the empty string")

    # File must have nodes
    if input_string == "()":
        raise ValueError("Input must contain nodes")

    # Nodes belong to a tree
    if "(" not in input_string or ")" not in input_string:
        raise ValueError("Node found with no tree")

    # Get the tree
    # Strip off the parentheses
    input_string = input_string[1:-1]

    # Check if the parent has children
    if "(" in input_string:
        # This parent has children

        # Split the parent from the children
        parent_stop = input_string.index("(")
        parent = input_string[0:parent_stop]
        print(parent)
        input_string = input_string.replace(parent, "")
        print(input_string)

        # Sanitize the parent
        parent = parent.replace(";", "")

        # Get the properties of the parent
        parent_properties = get_properties(parent)
        print(parent_properties)

        # Separate the children
        children = input_string.split(";")
        print(children)

        # Sanitize the children
        children = [child.replace("(", "").replace(")", "") for child in children]
        children = [child for child in children if child != ""]
        print(children)

        # Get the properties of the children
        child_properties = []
        for child in children:
            child_properties.append(get_properties(child))
        print(child_properties)

        # Get the child trees
        child_trees = []
        for child in child_properties:
            child_trees.append(SgfTree(properties=child))
        print(child_trees)

        # Return the parent with its children
        return SgfTree(properties=parent_properties, children=child_trees)
    else:
        # This parent does not have children

        # Remove the node separator from the node
        input_string = input_string.replace(";", "")
        print(input_string)
        return SgfTree(properties=get_properties(input_string))


def get_properties(node: str) -> dict:
    print(f"Node is {node}")

    # Split the node into its properties
    properties = dict()
    while len(node) > 0:

        # Get the key
        key_stop = node.index("[")
        key = node[0: key_stop]

        # Key must be uppercase
        if not key.isupper():
            raise ValueError("Key must be uppercase")

        # Get the value
        value_stop = node.index("]")
        value = node[key_stop + 1: value_stop]

        # Add the pairs to the properties dict
        properties[key] = [value]

        # Remove the first property from the node
        node = node[len(key) + len(value) + 2:]

    return properties

# Two nodes
tree = parse("(;A[B];B[C])")
print(tree.properties)