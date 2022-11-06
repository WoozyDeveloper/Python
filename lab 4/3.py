import os


def f(my_path):
    if os.path.isfile(my_path):  # return ultimele 20 de char
        my_file = open(my_path, "r")
        content = my_file.read()
        return content[-20:]
    elif os.path.isdir(my_path):
        # lista tuple (extensie, count)
        # sortata descrescator duap count
        # extensie si nr de fisiere cu extensia respectiva

        dict = {}
        for root, subdirs, files in os.walk(my_path):
            for file in files:
                split_text = file.split(".")
                if len(split_text) == 2:
                    if split_text[1] not in dict:
                        dict[split_text[1]] = 1
                    else:
                        dict[split_text[1]] += 1
        dict = {k: v for k, v in sorted(
            dict.items(), key=lambda item: item[1], reverse=True)}
        return dict
        # res = []
        # extensions = []
        # extensions_set = set()
        # entries = os.popen("dir " + my_path).readline()
        # print("EEEEEEE!!!!" + entries)
        # for entry in entries:
        #     print("entry = = = " + entry)
        #     extension = entry.split('.')
        #     extensions.append(extension[-1])
        #     extensions_set.add(extension[-1])
        # pass

        # for extension in extensions_set:
        #     res.append((extension, extensions.count(extension)))
    print("Not a valid path")
    return -1


print(f('my_dir'))
