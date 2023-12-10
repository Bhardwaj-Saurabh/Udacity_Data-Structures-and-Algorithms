import sys
import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    if not data:
        return "", None

    frequency = Counter(data)
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    codes = {}
    root = priority_queue[0]

    def generate_codes(node, current_code):
        if node is not None:
            if node.char is not None:
                codes[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")

    generate_codes(root, "")

    encoded_data = ''.join([codes[char] for char in data])
    return encoded_data, root

def huffman_decoding(data, tree):
    decoded = ""
    node = tree
    for bit in data:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.char:
            decoded += node.char
            node = tree
    return decoded

if __name__ == "__main__":
    codes = {}
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    ## Add your own test cases: include at least three test cases
    ## and two of them must include edge cases, such as null, empty or very large values

    # test case 1
    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}".format(decoded_data))

    # test case 2
    a_great_sentence = "aabbccd"
    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}".format(decoded_data))

    # test case 3
    a_great_sentence = "xxyyz"
    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))
    
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}".format(decoded_data))