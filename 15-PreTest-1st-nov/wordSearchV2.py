msg = input('Input sentence: ')
acceptable_error = int(input('n: '))
word = input('Input word: ')

def my_find(msg, find, error):
    msg = msg[0:len(find)]
    if ' ' in msg or len(msg)<len(find):
        return (-1, '')
    er_count = 0
    output = ''
    for i in range(len(find)):
        if msg[i].lower()!=find[i].lower():
            er_count+=1
            output+='?'
        else:
            output+=msg[i]
    if er_count>error:
        return (-1, '')
    else:
        return (er_count, output)
        

output = ''

i = 0
while i < len(msg):
    n_error, find_out = my_find(msg[i::], word, acceptable_error)
    if n_error != -1:
        output+='<'+find_out+'>'
        i += len(word)
    else:
        output+=msg[i]
        i += 1
if output==msg:
    print('Not found')
else:
    print('Found')
    print(output)
