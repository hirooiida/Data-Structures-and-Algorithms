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

    if data == "":
        return "0", Node(None,None)

    for c in data:
        if c not in frequency:
            frequency[c] = 1
        elif c in frequency:
            frequency[c] += 1

    if len(frequency) < 2:
        return "0" * frequency[data[0]], Node(data[0],frequency[data[0]])
    
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
        if code == "":
            translation_dict[node.char] = "0"
        else:
            translation_dict[node.char] = code
        return translation_dict

    translation_dict.update(generate_huffman_code_dict(node.left, code + "0"))
    translation_dict.update(generate_huffman_code_dict(node.right, code + "1"))

    return translation_dict

def huffman_decoding(data,tree):
    decoded_data = ""

    if tree.freq == None:
        return ""

    translation_dict = generate_huffman_code_dict(tree)
    reversed_dict = get_reversed_dict(translation_dict)

    key = ""
    for char in data:
        key += char
        if key in reversed_dict:
            decoded_data += reversed_dict[key]
            key = ""
    
    return decoded_data


def get_reversed_dict(dictionary):
    return {v: k for k, v in dictionary.items()}

if __name__ == "__main__":
    codes = {}

    '''
    print("\n==== TEST ====")
    data = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("--- Encode data ---")
    encoded_data, tree = huffman_encoding(data)
    print(data)
    print(encoded_data)

    print("--- Decode data ---")
    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)
    '''

    print("--- UDACITY sample 1 ---")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    print("--- UDACITY sample 2 ---")
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    print("--- UDACITY sample 3 ---")
    a_great_sentence = "bbb"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))