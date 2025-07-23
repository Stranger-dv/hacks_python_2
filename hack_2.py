"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    _ls = []
    vocales = ["a","e","i","o",'u']

    for i in result:
        if i not in vocales:
            _ls.append(i)

    result = "".join(_ls)
    return result

