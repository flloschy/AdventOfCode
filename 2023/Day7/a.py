
import time
start = time.perf_counter()
####
content = open("./2023/Day7/input.txt", "r").read().splitlines()
hands = [(line.split(" ")[0], int(line.split(" ")[1])) for line in content]


orderOfPriority = list("23456789TJQKA")
def priority(card:str): return orderOfPriority.index(card)

class typeOfHand:
    Five_of_a_kind = 6
    Four_of_a_kind = 5
    Full_house = 4
    Three_of_a_kind = 3
    Two_pair = 2
    One_pair = 1
    High_Card = 0

def getTypeOfHand(hand:str):
    amounts = {}
    types = 0

    for card in hand:
        if card not in amounts:
            amounts[card] = 1
            types += 1
        else: amounts[card] += 1

    if types == 1: return typeOfHand.Five_of_a_kind
    if types == 2:
        if 4 in amounts.values(): return typeOfHand.Four_of_a_kind
        return typeOfHand.Full_house
    if types == 3:
        if 3 in amounts.values(): return typeOfHand.Three_of_a_kind
        return typeOfHand.Two_pair
    if types == 4:
        return typeOfHand.One_pair
    return typeOfHand.High_Card

def alternativeRules(hand1:str, hand2:str):
    for card1, card2 in zip(hand1, hand2):
        prio1 = priority(card1)
        prio2 = priority(card2)
        if prio1 > prio2: return True
        if prio2 > prio1: return False


# original from https://www.geeksforgeeks.org/bubble-sort/
n = len(hands)
for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
        type1 = getTypeOfHand(hands[j][0])
        type2 = getTypeOfHand(hands[j+1][0])
        if type1 > type2:
            hands[j], hands[j+1] = hands[j+1], hands[j]
            swapped = True
        elif type1 == type2:
            if alternativeRules(hands[j][0], hands[j+1][0]):
                hands[j], hands[j+1] = hands[j+1], hands[j]
                swapped = True
    if (swapped == False):
        break

sum_ = 0
for rank, (_, bid) in enumerate(hands):
    sum_ += bid * (rank+1)
print(sum_)


###
print(f"Time Taken: {time.perf_counter()-start}s")
