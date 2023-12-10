
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    groups_to_check = [group]

    while groups_to_check:
        current_group = groups_to_check.pop()

        # Check if the user is in the current group
        if user in current_group.users:
            return True

        # Add subgroups to the list to check
        groups_to_check.extend(current_group.groups)

    return False


# Test Cases
def test_is_user_in_group():
    # Setup
    parent_group = Group("parent")
    child_group = Group("child")
    sub_child_group = Group("sub_child")

    user1 = "user1"
    user2 = "user2"
    sub_child_user = "sub_child_user"

    parent_group.add_group(child_group)
    child_group.add_group(sub_child_group)

    child_group.add_user(user1)
    sub_child_group.add_user(sub_child_user)

    # Test 1: User in the immediate group
    assert is_user_in_group(user1, child_group) == True, "Test 1 Failed: User should be in the immediate group"

    # Test 2: User in the subgroup
    assert is_user_in_group(sub_child_user, parent_group) == True, "Test 2 Failed: User should be in the subgroup"

    # Test 3: User not in any group
    assert is_user_in_group(user2, parent_group) == False, "Test 3 Failed: User should not be in any group"

    # Test 4: User in the deepest subgroup
    assert is_user_in_group(sub_child_user, sub_child_group) == True, "Test 4 Failed: User should be in the deepest subgroup"

    print("All tests passed.")

# Run tests
test_is_user_in_group()