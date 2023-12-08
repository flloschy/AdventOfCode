
from collections import Counter
import time
start = time.perf_counter()
####
content = open("./2023/Day7/input.txt", "r").read().splitlines()
hands = [(line.split(" ")[0], int(line.split(" ")[1])) for line in content]


orderOfPriority = list("J23456789TQKA")
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
    amounts = Counter(hand)
    if hand == "JJJJJ": hand = "AAAAA"
    elif "J" in hand:
        del amounts["J"]
        common = amounts.most_common(1)
        hand = hand.replace("J",common[0][0])

    amounts = Counter(hand)

    types = len(set(hand))

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


hands = [(hand[0], hand[1], getTypeOfHand(hand[0])) for hand in hands]


n = len(hands)
for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
        if hands[j][2] > hands[j+1][2]:
            hands[j], hands[j+1] = hands[j+1], hands[j]
            swapped = True
        elif hands[j][2] == hands[j+1][2]:
            if alternativeRules(hands[j][0], hands[j+1][0]):
                hands[j], hands[j+1] = hands[j+1], hands[j]
                swapped = True
    if not swapped:
        break

sum_ = 0
for rank, (_, bid, _) in enumerate(hands):
    sum_ += bid * (rank+1)
print(f"{sum_=}", 249631254, f"{sum_-249631254=}", sep="\t")


###
print(f"Time Taken: {time.perf_counter()-start}s")
