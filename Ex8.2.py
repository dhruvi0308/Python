import random
for i in range(20):
    article=['the','a','one','some','any']
    noun=['boy','girl','dog','town','car']
    verb=['drove','jumped','ran','walked','skipped']
    preposition=['to','from','over','under','on']

    words=[article[random.randrange(5)],
           noun[random.randrange(5)],
           verb[random.randrange(5)],
           preposition[random.randrange(5)],
           article[random.randrange(5)],
           noun[random.randrange(5)]]
    ' '.join(words)+'.'
    print(words)
