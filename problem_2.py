import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.Note that a path may
    contain further subdirectories and those subdirectories may also contain
    further subdirectories.There are no limit to the depth of the subdirectories
    can be.
    Args:
        suffix(str): suffix if the file name to be found
        path(str): path of the file system
    Returns:
        list: a list of paths
    """
    files = []
    if os.path.isdir(path):
        # iterating items
        for item in os.listdir(path):
            # Recursion and appending to list
            for file in find_files(suffix, os.path.join(path, item)):
                files.append(file)
    # suffix end with .c, add it to the list
    if path.endswith(suffix):
        files.append(path)
    return files

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))  #return False

# Does the file end with .py?
print ("./ex.py".endswith(".py")) #True

'''
['.ipynb_checkpoints', 'explanation_1.md.txt', 'problem_1.ipynb', 'problem_2.ipynb', 'Workbook(1).ipynb']
False
True

'''

print("Pass" if find_files(".c","./testdir") == ["./testdir/subdir3/subsubdir1/b.c", "./testdir/t1.c",
                                                  "./testdir/subdir5/a.c", "./testdir/subdir1/a.c"] else "Fail")
print("Pass" if find_files(".c","./testdir/t1.c") == ["./testdir/t1.c"] else "Fail")
print("Pass" if find_files(".c","./testdir/subdir3/subsubdir1/b.c") == ["./testdir/subdir3/subsubdir1/b.c"] else "Fail")
print("Pass" if find_files(".c","") == [] else "Fail") #edge case when path is not provided
print("Pass" if find_files(".c","./testdir/subdir2") == [] else "Fail")