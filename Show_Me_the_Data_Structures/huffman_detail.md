Explanation of Huffman Coding

Requirement:
Develop encoding and decoding algorithms using Huffman coding, a lossless data compression schema.

Summary:
Huffman Coding works on the principle of assigning shorter bit sequences to more frequently occurring characters and longer sequences for less frequent ones.

Huffman Encoding:
Frequency Calculation: For a given string, compute the frequency of each character and store it in a dictionary.
Heap Construction: Utilize Python's heapq module to construct a heap based on these frequencies.
Building Huffman Tree: Form a Huffman Tree from the heap by repeatedly merging the two nodes with the lowest values until only the root node remains.
Encoding: Assign '0' to left branches and '1' to right branches. Encode the text based on these assignments and send the encoded text along with the heap tree to the huffman_decoding function.
Huffman Decoding:
Reconstruction: Utilize the provided tree and encoded text to decode and retrieve the original string.
Time and Space Complexity:
Time Complexity:

O(n) to iterate through the string, storing character frequencies.
O(n) for list comprehension and heapify operations.
O(n) for the while loop, including constant time operations for heappop and appending bits to branches.
Total for encoding: O(4n) ≈ O(n).

Decoding also has a time complexity of O(n).
Space Complexity:

Utilizes O(distinct_characters) space to store the encoded or decoded data.
Huffman Encoding Steps in Detail:
Iterate through the string, storing each character's frequency in a dictionary.
Create a heap with [frequency, [symbol, '']] for each symbol, and apply heapq.heapify.
In the while loop:
Perform heapq.heappop twice to get the two lowest nodes.
Add '0' to the binary code of the left node and '1' to the right node.
Use heapq.heappush to push the combined node back into the heap.
Outside the while loop:
Compile a dictionary mapping each character to its Huffman code.
Encode the original text using this dictionary.
Huffman Decoding Steps in Detail:
Traverse the Huffman Tree using the encoded binary string, switching to the left node for '0' and right for '1'. Append the character found at leaf nodes to the decoded string.
This approach ensures efficient compression and decompression of data, leveraging the frequency of character occurrence for optimal encoding.