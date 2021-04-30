# Problem 5: Autocomplete with Tries
## Reason
Each TrieNode contains following word as child nodes in dictionary type which enable O(1) efficiency to access nodes. If the word is completed at the node, the node won't have child nodes and its attribute ```is_word``` gets ```True```. The recursive implementations are deployed for ```insert``` and ```find``` functions for the code simplicity.

## Efficiency
The time complexity for both ```find``` and ```insert``` is O(n). It needs to iterate the for loops with n times in the worst case when the input word exists. The space complexity is O(n). The worst case is to insert new word which starts with a new alphabet.
