# Write a Python program with builtin function that returns True if all elements of the tuple are true.
tpl = (True, True, True, True)

def all_true(tpl):
    return True if all(tpl) else False

print(all_true(tpl))