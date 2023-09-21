
def fileCreator(buyer, receiver):
    location = "C://Users//Tim//Desktop//SecretSanta23"
    name = buyer
    pathy=str(location + '//' + name  + '.txt')

    f = open(pathy, 'a')
    f.write('Secret Santa 2023 \n')
    f.write('\n')
    f.write('Ho, ho ,ho, Merry Christmas ' + name + '\n' )
    f.write('\n')
    f.write('You are buying a present for ' + receiver)
    f.write('\n\n')
    f.write('p.s. this message was written by a computer, no one has read it and no one else knows who your \n')
    f.write('randomly selected secret santa is')
    f.close()


