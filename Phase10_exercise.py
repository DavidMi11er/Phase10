import random
def FindPhases(Hand):
    """Determine which phases a given hand can fulfill"""
    if len(Hand) < 10:
        return "This is not a full hand"
    elif len(Hand) > 11:
        return "No fair - you have extra cards in your hand"
    elif len(Hand) == 11:
        print("You have one card to discard")
    PhasesPassed = []
    OrganizedHand = {}
    for Number in Hand:
        if not isinstance(Number, int):
            return "Non-integer value: found '{}'".format(Number)
        if Number < 1 or Number > 12:
            return "Those aren't all valid Phase 10 values: found {}".format(Number)
        if Number in OrganizedHand.keys():
            OrganizedHand[Number] += 1
        else:
            OrganizedHand[Number] = 1
    #print("Here is the hand grouped: {}".format(OrganizedHand))
    CurrentRun = 0
    PriorNum = 0
    Phase1Met = False  #2 sets of 3
    Phase2Met = False  #set of 3; run of 4
    Phase3Met = False  #set of 4; run of 4
    Phase4Met = False  #run of 7
    Phase5Met = False  #run of 8
    Phase6Met = False  #run of 9
    Phase7Met = False  #2 sets of 4
    Phase9Met = False  #set of 5; set of 2
    Phase10Met = False #set of 5; set of 3
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    for CardNum in sorted(OrganizedHand.keys()):
        if OrganizedHand[CardNum] > 8:
            return "Invalid hand, there are only 8 cards of any given number. Found {} {}'s".format(OrganizedHand[CardNum], CardNum)
        if OrganizedHand[CardNum] > 7:
            Phase10Met = True
            Phase9Met = True
            Phase7Met = True
            Phase1Met = True
        elif OrganizedHand[CardNum] == 7:
            Phase9Met = True
            Phase1Met = True
            count5 += 1
        elif OrganizedHand[CardNum] == 6:
            Phase1Met = True
            count5 += 1
        elif OrganizedHand[CardNum] == 5:
            count5 += 1
        elif OrganizedHand[CardNum] == 4:
            count4 += 1
        elif OrganizedHand[CardNum] == 3:
            count3 += 1
        elif OrganizedHand[CardNum] == 2:
            count2 += 1
        if PriorNum == 0:
            PriorNum = CardNum
        if CardNum == PriorNum + 1:
            CurrentRun += 1
        else:
            CurrentRun = 1
        if CurrentRun >= 4:
            if CurrentRun > 8:
                Phase4Met = True
                Phase5Met = True
                Phase6Met = True
            elif CurrentRun == 8:
                Phase4Met = True
                Phase5Met = True
            elif CurrentRun == 7:
                Phase4Met = True
            #print("found a run of 4 from {} to {}". format(CardNum - 3, CardNum))
            for SetNum in OrganizedHand.keys():
                if SetNum < CardNum - 3 or SetNum > CardNum:
                    #not part of the current run
                    if OrganizedHand[SetNum] >= 4:
                        #print("found a set of {} {}'s to go with it".format(OrganizedHand[SetNum], SetNum))
                        Phase2Met = True
                        Phase3Met = True
                    elif OrganizedHand[SetNum] == 3:
                        #print("found a set of {} {}'s to go with it".format(OrganizedHand[SetNum], SetNum))
                        Phase2Met = True
                else: #part of current run needs an extra card to count
                    if OrganizedHand[SetNum] > 4:
                        #print("found a set of {} {}'s to go with it".format(OrganizedHand[SetNum] - 1, SetNum))
                        Phase2Met = True
                        Phase3Met = True
                    elif OrganizedHand[SetNum] == 4:
                        #print("found a set of {} {}'s to go with it".format(OrganizedHand[SetNum] - 1, SetNum))
                        Phase2Met = True
        PriorNum = CardNum
    if count5 == 2:
        Phase10Met = True
        Phase9Met = True
        Phase7Met = True
        Phase1Met = True
    elif count5 == 1:
        if count4 >= 1:
            Phase10Met = True
            Phase9Met = True
            Phase7Met = True
            Phase1Met = True
        elif count3 >= 1:
            Phase10Met = True
            Phase9Met = True
            Phase1Met = True
        elif count2 >= 1:
            Phase9Met = True
    if count4 >= 2:
        Phase7Met = True
        Phase1Met = True
    elif count4 + count3 >= 2:
        Phase1Met = True
    if Phase1Met:
        PhasesPassed.append(1)
    if Phase2Met:
        PhasesPassed.append(2)
    if Phase3Met:
        PhasesPassed.append(3)
    if Phase4Met:
        PhasesPassed.append(4)
    if Phase5Met:
        PhasesPassed.append(5)
    if Phase6Met:
        PhasesPassed.append(6)
    if Phase7Met:
        PhasesPassed.append(7)
    if Phase9Met:
        PhasesPassed.append(9)
    if Phase10Met:
        PhasesPassed.append(10)

    #print("number of pairs: {}".format(count2))
    #print("number of triplets: {}".format(count3))
    #print("number of quadruplets: {}".format(count4))
    #print("groups of 5 to 7: {}".format(count5))
    #print("Meet's phases: {}".format(PhasesPassed))
    return PhasesPassed
