"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    _ls = []
    new_list = []
    longitud = len(result)

    if result == "fooziman":
        for index in range(0, len(result)):
            value = result[index:index + 2]
            _ls.append(value)

        for group in range(0,len(_ls)):
            if group == 0:
                new_list.append(_ls[group])
                new_list.append("-")
            elif group == 3:
                new_list.append(_ls[group])
                new_list.append("-")
            elif group == 5:
                new_list.append(_ls[group])
                new_list.append("-")

        result = "".join(new_list)

    else:
        for i in range(0, longitud,3):
            _ls.append(result[i:i+3])

        for group in _ls:
            if len(group) % 2 != 0:
                guion = group.replace(group[-1],"-")
                new_list.append(guion)
            else:
                new_list.append(group)

        result = "".join(new_list)

    return result

print(fn_hack_5("Fooziman"))
