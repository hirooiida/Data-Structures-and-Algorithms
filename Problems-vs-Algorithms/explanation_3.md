# Problem 3: Rearrange Array Digits
## Reason
The required set of numbers can be created by putting largest numbers in the upper digits. Quicksort is used to sort the input list to pop the largest numbers from the input list in order. The quicksort implementation is copied from an Udacity class code.

## Efficiency
The average time complexity is O(nlog n). It can be O(n2) in the worst case due to the use of quicksort. The average space efficiency is O(log n). It can be O(n) in the worst case for quicksort. 
