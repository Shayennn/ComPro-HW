msg = input('Input sentence: ')
word = input('Input word: ')

output = ''

i = 0
while i < len(msg):
    found = msg.lower().find(word.lower(), i)
    if found == i:
        output+='<'+msg[i:i+len(word)]+'>'
        i += len(word)
    else:
        output+=msg[i]
        i += 1
if output==msg:
    print('Not found')
else:
    print('Found')
    print(output)
