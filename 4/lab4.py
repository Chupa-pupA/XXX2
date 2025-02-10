class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}

    def add_child_folder(self, name):
        if name not in self.children:
            self.children[name] = Folder(name, parent=self)

    def add_file(self, name, size):
        self.files[name] = size

    def compute_size(self):
        total = sum(self.files.values())
        for child in self.children.values():
            total += child.compute_size()
        return total

def process_commands(command_lines):
    root = Folder('/')
    current = root

    for line in command_lines:
        line = line.strip()
        if line.startswith('$ cd'):
            target = line.split(' ')[-1]
            if target == '/':
                current = root
            elif target == '..':
                current = current.parent
            else:
                if target not in current.children:
                    current.add_child_folder(target)
                current = current.children[target]
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            dir_name = line.split(' ')[-1]
            current.add_child_folder(dir_name)
        else:
            size, file_name = line.split(' ')
            current.add_file(file_name, int(size))

    return root

def find_small_folders(root, limit=100000):
    small_folders = []

    def traverse(folder):
        size = folder.compute_size()
        if size <= limit:
            small_folders.append(size)
        for child in folder.children.values():
            traverse(child)

    traverse(root)
    return small_folders


with open('input_4.txt', 'r') as file:
    commands = file.readlines()

root_folder = process_commands(commands)

small_folders = find_small_folders(root_folder)
result = sum(small_folders)

print("Сума розмірів директорій, які не перевищують 100000:", result)