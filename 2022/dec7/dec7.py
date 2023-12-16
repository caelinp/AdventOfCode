filesystem = {} # keys are directory names, values are [parent directory, size]
output = open('input.txt').read().split('\n')
cwd = '/' # Current working directory
filesystem['/'] = [None, 0] # Root directory

for line in output:
    if line.startswith('$ cd '):
        path = line.replace('$ cd ', '')
        if path == "..":
            cwd = '/'.join(cwd.split('/')[:-1])  # Go up one directory
        elif path == "/":
            cwd = '/'  # Go to root directory
        else:
            cwd = cwd + '/' * (not cwd or cwd[-1] != '/') + path  # Navigate to a subdirectory
    elif line.startswith('dir '):
        dir_path = cwd + '/' * (cwd[-1] != '/') + line.replace('dir ', '')
        filesystem[dir_path] = [cwd, 0]  # Add new directory
    elif line.split()[0].isnumeric():
        size = int(line.split()[0])
        parent = cwd
        while parent:
            filesystem[parent][1] += size
            parent = filesystem[parent][0]  # Move to parent directory

# Calculate total size of directories with size at most 100000
p1 = sum(size for _, (_, size) in filesystem.items() if size <= 100000)
p2 = min(size for _, (_, size) in filesystem.items() if size >= (30000000 - (70000000 - filesystem['/'][1])))
print('part 1: {}\npart 2: {}'.format(p1, p2))
