Time Complexity:

The hash map makes the time of get() to be O(1). 
HashMap provide O(1) insertion and lookup. 
Reason for choosing doubly LinkList is O(1) deletion ,updation and insertion if we have the address of Node on which this operation has to perform.

Space Complexity:
An LRU cache tracking n items requires a linked list of length n, and a hash map holding n items.
That's O(n) space, but it's still two data structures (as opposed to one). 
