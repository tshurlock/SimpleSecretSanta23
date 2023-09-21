import random
import filecreation as fc
buyers = "Tony, Emma, Mark, Ruth, James, Anna, Ken, Chole"

buyerlist = ['Tony', 'Emma', 'Mark', 'Ruth', 'James', 'Anna', 'Ken', 'Chole']
receiverlist = ['Tony', 'Emma', 'Mark', 'Ruth', 'James', 'Anna', 'Ken', 'Chole']


couplepairs = {'Tony':'Emma', 'Mark':'Ruth', 'James':'Anna', 'Ken':'Chole', 'Emma':'Tony', 'Ruth': 'Mark', 'Anna':'James', 'Chole':'Ken'}

buyingPairs= {'Tony': None,  'Emma': None, 'Mark': None, 'Ruth': None, 'James': None, 'Anna': None, 'Ken': None, 'Chole': None,}

confirmedBuyer= []
confirmedReceiver= []

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
            confirmedBuyer.append(buyer)
            confirmedReceiver.append(receiver)



print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

for i in buyingPairs:
    fc.fileCreator(i,buyingPairs[i])

print('all done')
print(confirmedReceiver)
print('Confirmed buyers', sorted(confirmedBuyer))
print('Confirmed receiver', sorted(confirmedReceiver))