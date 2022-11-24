import os
import re


def f(my_path, reg):
    if os.path.isdir(my_path):
        # lista tuple (extensie, count)
        # sortata descrescator duap count
        # extensie si nr de fisiere cu extensia respectiva
        for root, subdirs, files in os.walk(my_path):
            for file in files:
                split_text = file.split(".")
                res = re.findall(reg, split_text[0])

                my_file = open(file, "r")
                content = my_file.read()
                res2 = re.findall(reg, content)

                if res and res2:
                    print('>>', split_text[0])
                else:
                    print(split_text[0])


f("D:\PYTHONLAB\Python\lab 6", "\d+")
