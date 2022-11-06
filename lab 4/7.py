import os
import pprint


def f(file_path):
    return {
        "full_path": os.path.abspath(file_path),
        "file_size": os.path.getsize(file_path),
        "file_extension": os.path.splitext(file_path)[-1][1:],
        "can_read": os.access(file_path, os.R_OK),
        "can_write": os.access(file_path, os.W_OK),
    }


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(f('D:\PYTHONLAB\Python\lab 4\my_file'))
