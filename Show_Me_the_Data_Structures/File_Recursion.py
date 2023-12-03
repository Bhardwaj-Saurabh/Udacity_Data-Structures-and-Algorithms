
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # check if dir exists
    if not os.path.isdir(path):
        return "Invalid directory path"

    file_list = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) and item_path.endswith(suffix): # check conditions
            file_list.append(item_path) # add to the list
        elif os.path.isdir(item_path):
            file_list.extend(find_files(suffix, item_path)) # add list to the list

    return file_list

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: 
# Normal case with ".c" suffix

print("Test Case 1:", find_files(".c", "./testdir"))

# Test Case 2: 
# Edge Case - Non-existent directory

print("Test Case 2:", find_files(".c", "./testdir/subdir3/subsubdir5"))

# Test Case 3: 
# Edge Case - Directory with no ".c" files

print("Test Case 3:", find_files(".c", "./testdir/subdir2")) 