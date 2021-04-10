# Huffman Coding
## Reason
The frequencies of each character is counted first and pushed into dictionary. They are extracted and push into list sorted by the number of frequency, as priority queue. The list is kept sorted during creating Huffman tree where the priority can be dynamically changed. Dictionary for translation between charactors and Huffman code is generated according to the Huffman tree.

## Efficiency
Time complexity for encoding is O(nlogn) due to the use of ```sorted()``` function. Time complexity for decoding is O(n) determined by tree traversal algorithm.

Space efficiency is O(n). Nodes according to the size of data are stored.
