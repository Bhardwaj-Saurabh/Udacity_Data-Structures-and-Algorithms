
Explanation of Active Directory User Lookup
Requirement:
Develop a function for efficiently checking whether a user exists in a group or its subgroups in an Active Directory structure.

Summary:
The implementation uses a Group class to handle group-related operations like adding users and groups, and retrieving their details. The key function, is_user_in_group, checks for user membership in a specified group and its subgroups.

Functionality:
Immediate Group Check: Initially, the function checks if the user is directly a member of the provided group.
Recursive Subgroup Check: If the user is not found in the immediate group, the function recursively searches through all subgroups.
Return Value: It returns True if the user is found either in the group or any of its subgroups, and False otherwise.

Time Complexity:
User List Check: O(l), where l is the length of the user list in a group. This linear search checks if the user is in the group's user list.
Group List Iteration: O(g), where g is the number of immediate subgroups in a group. Iterating through these subgroups is also a linear operation.
Recursive Complexity: O(n * (l + g)), where n is the total number of groups (including all levels of subgroups, calculated as branches^depth).
Overall: The time complexity combines the cost of checking each group's user list and iterating through each group's subgroup list, giving O(n * (l + g)).

Space Complexity:
Input Space:
Users: O(l)
Group List: O(g)
Per-Iteration Input Space: O(g + l)
Depth Iterations Input Space: O(depth * (g + l))

Auxiliary Space:
O(depth), accounting for the recursive call stack, which grows with the depth of the group structure.
Total Space Complexity: O(depth * (g + l)), combining the input space and auxiliary space complexities.

Conclusion:
This approach provides an effective method to determine user membership in a complex Active Directory structure. The recursive strategy ensures thorough coverage of all potential group memberships, while its linear time complexity per group makes it suitable for directories with a reasonable number of users and groups.