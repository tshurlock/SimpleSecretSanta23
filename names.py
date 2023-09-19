import random
buyers = "Tony, Emma, Mark, Ryan, James, Anna, Ken, Chole"

buyerlist = ['Tony', 'Emma', 'Mark', 'Ryan', 'James', 'Anna', 'Ken', 'Chole']
receiverlist = ['Tony', 'Emma', 'Mark', 'Ryan', 'James', 'Anna', 'Ken', 'Chole']


couplepairs = {'Tony':'Emma', 'Mark':'Ryan', 'James':'Anna', 'Ken':'Chole', 'Emma':'Tony', 'Ryan': 'Mark', 'Anna':'James', 'Chole':'Ken'}

buyingPairs= {'Tony': None,  'Emma': None, 'Mark': None, 'Ryan': None, 'James': None, 'Anna': None, 'Ken': None, 'Chole': None,}

for name in buyerlist:
    print('recevivers left ', receiverlist)
    while buyingPairs[name] == None:
        buyer = name
        receiver = random.choice(receiverlist)
        print(buyer, ' buys for ', receiver)
        if buyer != receiver and receiver != couplepairs[buyer]:
            print("Valid Selection")
            buyingPairs[buyer] = receiver
            receiverlist.remove(receiver)

print(buyingPairs)

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
for i in buyingPairs:
    print(i,buyingPairs[i])