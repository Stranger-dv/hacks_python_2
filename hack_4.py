"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    _ls = []

    if(len(result) > 3):
        for letter in result:
            if letter == result[0]:
                continue
            elif letter == result[-1]:
                continue
            else:
                _ls.append(letter)

        result = "".join(_ls)
    return result
