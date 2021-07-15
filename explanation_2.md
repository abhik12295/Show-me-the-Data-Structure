Used recurision  and concatenated new valid file to current path, then return the new files found and 
extended current list of files with them

Time complexity :
Time cmplexy depends on the number of iterations that will be done. 
O(mn) because loop over all files includes number of sub directories, m and number of files per directory, n

Space Complexity:
Directly dependent on the number of returns the function does, hence, the number of found files n, O(n).
