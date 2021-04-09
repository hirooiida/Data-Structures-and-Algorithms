import sys

class Node:

    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None    # 0
        self.right = None   # 1

    def __repr__(self):
        return f"Node({self.char},{self.freq})"

def huffman_encoding(data):
    encoded_data = ""
    frequency = {}

    for c in data:
        if c not in frequency:
            frequency[c] = 1
        elif c in frequency:
            frequency[c] += 1
    
    sorted_frequency = sorted(frequency.items(), key=lambda x:x[1])
    node_list = build_node_list(sorted_frequency)
    tree_root = build_tree(node_list)
    translation_dict = generate_huffman_code_dict(tree_root)

    for char in data:
        encoded_data += translation_dict[char]

    return encoded_data, tree_root

def build_node_list(data):
    node_list = list()
    for item in data:
        node_list.append(Node(item[0], item[1]))
    return node_list

def build_tree(node_list: list):

    if len(node_list) == 1:
        return node_list[0]

    parent = Node()
    parent.left = node_list.pop(0)
    parent.right = node_list.pop(0)
    parent.freq = parent.left.freq + parent.right.freq
    insert_node(parent, node_list)
    build_tree(node_list)

    return node_list[0]

def insert_node(node: Node, node_list: list):
    index = 0
    while index < len(node_list):
        if node.freq < node_list[index].freq:
            node_list.insert(index, node)
            return node_list
        index += 1
    node_list.append(node)
    return node_list

def generate_huffman_code_dict(node: Node, code=""):
    translation_dict = {}
    if not (node.left or node.right):
        translation_dict[node.char] = code
        return translation_dict

    translation_dict.update(generate_huffman_code_dict(node.left, code + "0"))
    translation_dict.update(generate_huffman_code_dict(node.right, code + "1"))

    return translation_dict


def huffman_decoding(data,tree):
    pass


if __name__ == "__main__":
    codes = {}

    print("\n==== TEST ====")
    data = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("--- Encoded data ---")
    print(huffman_encoding(data))
    
    sorted_list = [('D', 2), ('C', 3), ('B', 7), ('A', 10)]
    sorted_nodes = build_node_list(sorted_list)
    print("\n--- Sorted nodes ---")
    print(sorted_nodes)
    print("\n--- Insert node ---")
    print(insert_node(Node('E',5), sorted_nodes))

    
    print("\n--- Build tree ---")
    sample_ls = [Node("D",2), Node("B",3), Node("E",6), Node("A",7), Node("C",7)]
    root = build_tree(sample_ls)
    print("root: {}".format(root))
    print("root.left: {}".format(root.left))
    print("root.left.right: {}".format(root.left.right))
    print("root.left.left.right: {}".format(root.left.left.right))
    print("root.right: {}".format(root.right))
    print("root.right.right: {}".format(root.right.right))
    print("root.right.right.right: {}".format(root.right.right.right))
    print("root.right.right.left: {}".format(root.right.right.left))

    print("\n--- Generate table ---")
    table = generate_huffman_code_dict(root)
    print(table)

