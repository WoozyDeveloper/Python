import os


def f(target, to_search):

    if os.path.isfile(target):
        if to_search in open(target, "r").read():
            return [os.path.abspath(target)]
    elif os.path.isdir(target):
        res = []
        for root, directories, files in os.walk(target):
            res += [os.path.abspath(os.path.join(root, file_name))
                    for file_name in files if os.access(os.path.join(root, file_name), os.R_OK) and to_search in
                    open(os.path.join(root, file_name), "r").read()]
            return res
    else:
        raise ValueError("Error!!!")


print(f(".", "my_dir"))
