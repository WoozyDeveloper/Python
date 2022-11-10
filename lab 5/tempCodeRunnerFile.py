def multiply_output(function):
    function_string = '''def new_function(*args, **kwargs):
    return function(*args,**kwargs)'''
    globals()["function"] = multiply_by_two
    exec(function_string, globals())
    return new_function


augmented_multiply_by_three = multiply_output(multiply_by_three)

x = augmented_multiply_by_three(10)