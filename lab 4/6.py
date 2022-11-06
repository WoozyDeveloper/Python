import os


def mesaj(e):
    print("EROARE PT ", e)


def my_f(exception: Exception):
    """
    prints exception
    :param exception:
    :return:
    """
    print(exception)


def f(target, to_search, callback):
    if os.path.isfile(target):
        try:
            if to_search in open(target, "r").read():
                return [os.path.abspath(target)]
        except Exception as e:
            print("NU E BN")
            callback(e)
    try:
        if not os.path.isdir(target):
            raise ValueError("nu e path bun")
        res = []
        for root, directories, files in os.walk(target):
            for file_name in files:
                try:
                    if to_search in open(os.path.join(root, file_name), "r").read():
                        res.append(os.path.abspath(
                            os.path.join(root, file_name)))
                except Exception as e:
                    callback(e)
        return res
    except Exception as e:
        callback(e)


print(f("xxxxx", "my_dir", mesaj))
