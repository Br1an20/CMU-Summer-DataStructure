# Please put this file and input files in the same dictionary

def myKey(e):
  return e[0]

# Whice file to run. If run 1.in, thrn indexOfFile = 1
# Change the value of indexOfFile to run different files
indexOfFile = 10

if indexOfFile > 10 or indexOfFile < 1:
    print("Wrong input file")
else:
    timeInterval = []
    initialTimeInterval = []
    with open(str(indexOfFile) + '.in') as f:
        for line in f:
            numbers = [int(n) for n in line.split()]
            if len(numbers) == 1:
                numberOfFires = numbers
            else:
                timeInterval.append(numbers)

    #print timeInterval
    #print numberOfFires

    timeInterval.sort(key=myKey)
    allCoverTime = []


    for all in range(len(timeInterval)):
        coverTime = []
        fireOne = timeInterval.pop(all)
        #print timeInterval
        startCoverTime = int(timeInterval[0][0])
        for t in range(len(timeInterval)):
            if t < len(timeInterval)-1:
                if timeInterval[t+1][0] < timeInterval[t][1]:
                    endCoverTime = int(timeInterval[t+1][1])
                else:
                    coverTime.append(int(timeInterval[t][1]) - startCoverTime)
                    startCoverTime = int(timeInterval[t+1][0])

            if t == len(timeInterval)-1:
                coverTime.append(int(timeInterval[t][1])-startCoverTime)

        #print(coverTime)
        timeInterval.insert(all,fireOne)
        timeSlot = sum(coverTime)
        allCoverTime.append(timeSlot)

    fireOneIndex = allCoverTime.index(max(allCoverTime))
    print('It is optimal to hire the life guard with the index: ' + str(fireOneIndex+1))
    fireOneGaurds = timeInterval[fireOneIndex]
    print('His shift is: ' + str(fireOneGaurds))
    print('The maximum coverage time is: ' + str(max(allCoverTime)))
    String = 'It is optimal to hire the life guard with the index: ' + str(fireOneIndex+1) + '. The maximum coverage time is: ' + str(max(allCoverTime))
    f = open(str(indexOfFile) + '.out', "w")
    f.write(String)
    f.close()
