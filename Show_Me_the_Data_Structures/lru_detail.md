
Explanation of LRU Cache Implementation
Requirement:
The LRU (Least Recently Used) Cache should offer fast access for get() and put()/set() operations, ideally in O(1) time complexity.

Summary:
To achieve efficient operations, the implementation combines two data structures:

Hashtable: Provides constant-time O(1) lookup.
Doubly Linked List (DLL): Enables constant-time O(1) addition and removal of nodes when the node's address is known.
Detailed Approach:
Hashtable: Each key in the hashtable maps to the corresponding node in the Doubly Linked List, storing the node's address. This allows direct access to any node in the list, facilitating quick movements and updates.
Doubly Linked List: The list keeps track of the usage order of cache items. The most recently used item is moved or added to the head of the list, and the least recently used item is found at the tail.
Time Complexity:
The combination of a Hashtable and a Doubly Linked List ensures that all critical operations - lookup, addition, and removal of nodes - are performed in constant time, O(1).
Lookup: The hashtable provides immediate access to the list node.
Add/Remove Nodes: Given the node's address from the hashtable, adding to or removing from the head/tail of the DLL is a constant-time operation.
Space Complexity:
Space complexity is evaluated as the sum of the input size and auxiliary space:

Input Space:
Dictionary space: O(n)
Doubly Linked List space: O(n)
Total Input space: O(n + n) ≈ O(n)
Auxiliary Space:
This refers to the temporary space used by the algorithm (excluding input size), such as loop initialization, function calls, etc. Assuming a constant auxiliary space of 4 bytes, it's O(1).
Total Space Complexity: O(n) (input size) + O(1) (auxiliary space) ≈ O(n)

Conclusion:
This LRU Cache implementation effectively balances the quick access of a hashtable with the ordered structure of a doubly linked list, ensuring all operations are performed in O(1) time, with an overall space complexity of O(n). This makes it highly efficient for caching applications where the speed of access and update is crucial.