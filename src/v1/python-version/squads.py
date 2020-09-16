swimmerList = {}
squad1 = []
squad2 = []
squad3 = []
noSquad = []
version = '1.0.0'
def addSwimmer():
    global swimmerList
    swimmerName = input("Please enter the name of the swimmer:\n")
    if swimmerName in swimmerList:
        choice = input('A swimmer with this name already exists. Do you want to overwrite them? [y/n] ').lower()
        while True:
            if choice != 'y' and choice != 'n':
                choice = input('Do you want to overwrite them? [y/n] ').lower()
            else: break
        if choice == 'n': return False
    while True:
        try:
            minSessions = int(input('Please enter the minimum number of sessions the swimmer is willing to do:\n'))
            break
        except ValueError:
            print('A valid number is required')
    while True:
        try:
            averageTime = float(input('Please enter the average time it takes the swimmer to swim 50m in seconds:\n'))
            break
        except ValueError:
            print('A valid number is required')
    swimmerList[swimmerName] = {'minSessions':minSessions, 'averageTime':averageTime}
    return True
print('Squad chooser Version: {} \nCopyright (c) 2020 Matthew Nickson, All rights reserved\nLicensed under MIT'.format(version))
while True:
        print("[1] Add swimmer\n[2] Generate squads\n[3] Quit")
        try:
            choice = int(input('Please choose an option: '))
        except ValueError:
            choice = False
        if choice == 1:
            state = addSwimmer()
            if state:
                print('Successfully added swimmer')
            else:
                print('Failed to add swimmer')
        elif choice == 2:
            for key in swimmerList:
                if swimmerList[key]['minSessions'] >=5 and swimmerList[key]['averageTime'] < 30:
                    squad3.append(key)
                    continue
                elif swimmerList[key]['minSessions'] >=4 and swimmerList[key]['averageTime'] < 33:
                    squad2.append(key)
                    continue
                elif swimmerList[key]['minSessions'] >=3 and swimmerList[key]['averageTime'] < 36:
                    squad1.append(key)
                    continue
                else:
                    noSquad.append(key)
                    continue
            print('Squad 1:')
            print(*squad1, sep = ", ")
            print('Squad 2:')
            print(*squad2, sep = ", ")
            print('Squad 3:')
            print(*squad3, sep = ", ")
            print('Unfortunately these swimmers did not make it into the squads:')
            print(*noSquad, sep = ", ")
            squad1 = []
            squad2 = []
            squad3 = []
            noSquad = []

        elif choice == 3: break
        else:
            print('Invalid option')
