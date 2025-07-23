"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    _ls = []
    _ls_2 = []
    vowels_dict = {
        'a':'@',
        'e':'v',
        'i':'¡',
        'o':'0',
        'u':'v'
    }
    vowels_list = ['a','e','i','o','u']

    for i in result:
        if i == result[0] and i not in vowels_list:
            _ls.append(i.upper())
        elif i == result[-1] and i not in vowels_list:
            _ls.append(i.upper())
        else:
            _ls.append(i)

    result_1 = "".join(_ls)

    for letter in result_1:
        if letter == 'a':
            _ls_2.append(vowels_dict['a'])
        elif letter == 'e':
            _ls_2.append(vowels_dict['e'])
        elif letter == 'i':
            _ls_2.append(vowels_dict['i'])
        elif letter == 'o':
            _ls_2.append(vowels_dict['o'])
        elif letter == 'u':
            _ls_2.append(vowels_dict['u'])
        else:
            _ls_2.append(letter)

    result_2 = "".join(_ls_2)
    return result_2
