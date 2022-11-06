import os


def f(dir_path):
    extension_set = set()
    entries = os.listdir(dir_path)
    for entry in entries:
        extension = entry.split('.')
        extension_set.add(extension[-1])
    return extension_set


print(f('my_dir/'))
