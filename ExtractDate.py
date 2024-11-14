text='We have two meetings scheduled on 05/10/2024 and the second on 12/10/2024. Please mark these in your calendar.'
tokens=text.replace(".","").split()
list=[]
for word in tokens:
    if len(word)==10:
        if word[2]=='/' and word[5]=='/':
            list+=[word]
            print(list)
print(tokens)