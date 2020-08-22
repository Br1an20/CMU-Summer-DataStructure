# Please put this file and input files in the same dictionary

def myKey(e):
  return e[0]

# Whice file to run. If run 1.in, thrn IndexOfFile = 1
# Change the value of IndexOfFile to run different files
IndexOfFile = 3

if IndexOfFile > 10 or IndexOfFile < 1:
    print("Wrong input file")
else:
    TimeInterval = []
    InitialTimeInterval = []
    with open(str(IndexOfFile) + '.in') as f:
        for line in f:
            numbers = [int(n) for n in line.split()]
            if len(numbers) == 1:
                NumberOfFires = numbers
            else:
                TimeInterval.append(numbers)

    #print TimeInterval
    #print NumberOfFires

    TimeInterval.sort(key=myKey)
    AllCoverTime = []


    for all in range(len(TimeInterval)):
        CoverTime = []
        FireOne = TimeInterval.pop(all)
        #print TimeInterval
        StartCoverTime = int(TimeInterval[0][0])
        for t in range(len(TimeInterval)):
            if t < len(TimeInterval)-1:
                if TimeInterval[t+1][0] < TimeInterval[t][1]:
                    EndCoverTime = int(TimeInterval[t+1][1])
                else:
                    CoverTime.append(int(TimeInterval[t][1]) - StartCoverTime)
                    StartCoverTime = int(TimeInterval[t+1][0])

            if t == len(TimeInterval)-1:
                CoverTime.append(int(TimeInterval[t][1])-StartCoverTime)

        #print(CoverTime)
        TimeInterval.insert(all,FireOne)
        TimeSlot = sum(CoverTime)
        AllCoverTime.append(TimeSlot)

    FireOneIndex = AllCoverTime.index(max(AllCoverTime))
    print('It is optimal to hire the life guard with the index: ' + str(FireOneIndex+1))
    FireOneGaurds = TimeInterval[FireOneIndex]
    print('His shift is: ' + str(FireOneGaurds))
    print('The maximum coverage time is: ' + str(max(AllCoverTime)))
