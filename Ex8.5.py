sentence='to be or not to be is a question'
tokens=sentence.split()
token=[word for word in tokens if word.startswith('b')]
print(token)