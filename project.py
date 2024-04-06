import random

class CardGame:
    def __init__(self):
        self.cardSet = self.createCardSet()
        self.passes = []
        self.out = []
        self.numberOfPlayers = 0
        self.playerDict = {}

    def main(self):
        self.numberOfPlayers = self.getNumberOfPlayers()
        self.playerDict = self.getPlayerSet(self.numberOfPlayers)
        self.startTheGame()
        self.endOfGame()

    def getNumberOfPlayers(self):
        while True:
            try:
                numberOfPlayer = int(input("Number of Players(at least two): "))
                if numberOfPlayer > 1:
                    break

            except ValueError:
                continue
        return numberOfPlayer

    def startTheGame(self):
        while len(set(self.passes)) + len(set(self.out)) != self.numberOfPlayers:
            for name, cards in self.playerDict.items():
                self.playerTurn(name, cards)

    def createCardSet(self):
        cardSet = []
        for i in range(1, 11):
            cardSet.extend([i] * 8)
        return cardSet

    def getPlayerSet(self, n):
        sets = {}
        for i in range(1, n + 1):
            sets[f"player{i}"] = []
            for _ in range(3):
                random_card = random.choice(self.cardSet)
                sets[f"player{i}"].append(random_card)
                self.cardSet.remove(random_card)
        return sets

    def playerTurn(self, name, cards):
        if name in self.passes:
            print(f"{name} pass")
            self.passes.append(name)
            self.endOfTurn()
            return

        if sum(cards) > 31:
            print(f"{name} Out")
            self.out.append(name)
            self.endOfTurn()
            return

        input(f"{name} press enter. ")
        print(f"{name} card set: {cards}")

        while True:
            userAnswer = input("do you want a card?(y/N) ")
            if userAnswer == "y" or userAnswer == "N":
                break
            else:
                continue

        if userAnswer != "y":
            print(f"{name} pass")
            self.passes.append(name)
            self.endOfTurn()
            return

        self.continueGambling(name, cards)

        if sum(cards) > 31:
            self.out.append(name)
            print(f"{name} is out")

        self.endOfTurn()

    def continueGambling(self, name, cards):
        gamble = random.choice(self.cardSet)
        print(f"This is your choice: {gamble} \n \n")
        cards.append(gamble)
        self.cardSet.remove(gamble)
        print(f"Player {name} card set {cards}")

    def endOfTurn(self):
        input("press enter and pass it to the next player")
        input(" \n \n \n \n \n \n press enter")
        print("\n \n \n \n \n")

    def endOfGame(self):
        print("\n \n \n \nResults: ")
        print("These players are out: ")

        for player in set(self.out):
            print(player, self.playerDict[player], f"with total: {sum(self.playerDict[player])}")

        print("\nThese players are passes: ")
        for player in set(self.passes):
            print(player, self.playerDict[player], f"with total: {sum(self.playerDict[player])}")

        self.findWinner()

    def findWinner(self):
        winnerScore = 0
        winnerName = []

        for player in set(self.passes):
            if sum(self.playerDict[player]) > winnerScore:
                winnerScore = sum(self.playerDict[player])
                winnerName = [player]

            elif sum(self.playerDict[player]) == winnerScore:
                winnerName.append(player)

        if len(winnerName) == 1:
            print(f"\nThe winner is {winnerName[0]}, with score: {winnerScore}")

        else:
            print("\nThe winners are:")

            for player in winnerName:
                print(f"{player}, with score: {winnerScore}")

if __name__ == "__main__":
    game = CardGame()
    game.main()
