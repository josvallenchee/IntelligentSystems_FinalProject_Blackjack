from random import shuffle

class Box():
    def __init__(self, deck):
        self.deck_type = deck

class Brand(Box):
    def __init__(self):
        super(Brand, self).__init__(1)
        self.type = "Marlboro"

def Shufflin():
    Deck = {"Spades":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"],"Hearts":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"],
    "Clovers":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"],"Diamonds":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]}

    Values = []
    for key in Deck:
        for values in Deck[key]:
            Values.append(values)

    shuffle(Values)

    for i in range(len(Values)):
        if Values[i] == "J" or Values[i] == "Q" or Values[i] == "K":
            Values[i] = 10
    return Values

def Game(Cards):
    hand1 = []
    hand1.append(Cards.pop())
    hand1.append(Cards.pop())
    print(hand1)

    while True:
        request = input("Do you want to add your hand?")
        if request == "y":
            hand1.append(Cards.pop())
            print(hand1)
        if request == "n":
            break

    if "A" in hand1:
        countA = hand1.count("A")
        hand1 = list(filter(lambda a: a != "A", hand1))
        result = sum(hand1)
        result += countA
        if result > 21:
            print("Bust! You lose the game!")
        elif result <12:
            result += 10
            print("Your points is:",result)
        else:
            print("Your points is:",result)
    else:
        result = sum(hand1)
        if result > 21:
            print("Your points is:",result)
        else:
            print("Your points is:",result)


