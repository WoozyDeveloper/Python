import os


def f(dir_path, file_path):
    my_file = open(file_path, "a")
    extension_set = set()
    entries = os.listdir(dir_path)
    for entry in entries:
        # write the entry in the file
        if entry[0] == 'A':
            my_file.write(os.path.abspath(entry) + '\n')


f('my_dir/', 'my_file')
