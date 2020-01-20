# coding=utf-8
# Taken from the internet. Credits to the owner
import os
import sys
import inspect

# Append the script location to the import path
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

def describe_builtin(obj):
    """ Describe a builtin function """
    # Built-in functions cannot be inspected by
    # inspect.getargspec. We have to try and parse
    # the __doc__ attribute of the function.
    docstr = obj.__doc__
    args = ''
    if docstr:
        items = docstr.split('\n')
        if items:
            func_descr = items[0]
            s = func_descr.replace(obj.__name__,'')
            idx1 = s.find('(')
            idx2 = s.find(')',idx1)
            if idx1 != -1 and idx2 != -1 and (idx2>idx1+1):
                args = s[idx1+1:idx2]
    return args

if __name__ == '__main__':
    package_name = sys.argv[1].strip()
    mymodule = __import__(package_name, fromlist=['foo'])

    for element_name in dir(mymodule):
        element = getattr(mymodule, element_name)

        if inspect.isclass(element):
            print("class %s" % element_name)

        elif hasattr(element, '__call__'):
            if inspect.isbuiltin(element):
                sys.stdout.write("builtin_function %s" % element_name)
                data = describe_builtin(element)
                data = data.replace("[", " [")
                data = data.replace("  [", " [")
                data = data.replace(" [, ", " [")
                sys.stdout.write(data.replace(", ", " "))
                print("")

            else:
                try:
                    data = inspect.getargspec(element)
                    sys.stdout.write("function %s" % element_name)
                    for a in data.args:
                        sys.stdout.write(" ")
                        sys.stdout.write(a)
                    if data.varargs:
                        sys.stdout.write(" *")
                        sys.stdout.write(data.varargs)
                    print("")
                except:
                    pass

        elif inspect.ismodule(element):
            print("module %s" % element_name)

        else:
            print("value %s" % element_name)
