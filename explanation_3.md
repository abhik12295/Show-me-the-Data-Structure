For every encoded symbol, traverse the tree in order to decode that symbol. 

Time Complexity:

The tree contains k nodes and, on average, it takes O(log k) node visits to decode a symbol. 
So the time complexity would be O(n logk).

Space complexity: 
Space complexity for the creation of tree is O(k) and 
as since we, storing it in dictinary and extracting , thus O(n) for the decoded text.
