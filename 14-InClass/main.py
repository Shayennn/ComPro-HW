import keyword
keyword_list = keyword.kwlist
"""
'''
finding identifiers
"""
'''
identifiers = variable_name + function_name
'''
"""
finding identifiers2
"""

def remove_docstring_comments(long_line) :
    new_long_line = ''
    found_single = False
    found_double = False
    lines = long_line.split('\n')
    for i in range(len(lines)):
        if found_double or found_single:
            if(lines[i].find("\"\"\"")!=-1):
                found_double = False
            if(lines[i].find('\'\'\'')!=-1):
                found_single = False
            continue
        if(lines[i].find("\"\"\"")!=-1):
            found_double = True
            newline = lines[i][lines[i].find("\"\"\"")+3::]
            if newline != '':
                new_long_line += newline+'\n'
            continue
        if(lines[i].find('\'\'\'')!=-1):
            found_single = True
            newline = lines[i][lines[i].find('\'\'\'')+3::]
            if newline != '':
                new_long_line += newline+'\n'
            continue
        cm = lines[i].find("#")
        if(cm!=-1 and lines[i][cm-1] != '\'' and lines[i][cm-1] != "\"" and lines[i][cm+1] != '\'' and lines[i][cm+1] != "\""):
            newline = lines[i][0:lines[i].find("#")]
            if newline != '':
                new_long_line += newline+'\n'
            continue
        new_long_line += lines[i]+'\n'

    return new_long_line

filename = "main.py"
# reading file
long_line = open(filename).read()
# print(long_line)
# remove docstrings & manylinescomment
long_line = remove_docstring_comments(long_line)
# print(long_line)
# split lines
lines = long_line.split('\n')
print(long_line)

reversed_dict = {}

for i in range(len(long_line.split('\n'))):
    for key in keyword_list:
        if(lines[i].count(key)!=0):
            if key not in reversed_dict:
                reversed_dict[key]=lines[i].count(key)
            else:
                reversed_dict[key]+=lines[i].count(key)

print(reversed_dict)
