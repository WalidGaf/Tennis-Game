class Tennis:
    firstPlayerScore = 0
    secondPlayerScore = 0

    def __init__(self, firstPlayerName, secondPlayerName):
        self.firstPlayerName = firstPlayerName
        self.secondPlayerName = secondPlayerName

    def firstPlayerPoint(self):
        self.firstPlayerScore += 1

    def secondPlayerPoint(self):
        self.secondPlayerScore += 1

    def highestScore(self):
        if self.firstPlayerScore > self.secondPlayerScore:
            return self.firstPlayerName
        else:
            return self.secondPlayerName

    def gameWin(self):
        if self.firstPlayerScore >= 4 and self.firstPlayerScore >= self.secondPlayerScore + 2:
            return True
        elif self.secondPlayerScore >= 4 and self.secondPlayerScore >= self.firstPlayerScore + 2:
            return True
        else:
            return False

    def advantage(self):
        if (self.firstPlayerScore >= 4 and self.firstPlayerScore == self.secondPlayerScore + 1):
            return True
        elif self.secondPlayerScore >= 4 and self.secondPlayerScore == self.firstPlayerScore + 1:
            return True
        else:
            return False

    def deuce(self):
        return self.secondPlayerScore >= 3 and self.secondPlayerScore == self.firstPlayerScore

    def pointTennis(self, point):
        switcher = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty"
        }
        return switcher.get(point, lambda: "Invalid point")

    def getScore(self):
        if self.gameWin():
            return f"{self.highestScore()} is winner !!!!."
        if self.advantage():
            return f"Advatange {self.highestScore()}"
        if self.deuce():
            return "Deuce"
        if (self.firstPlayerScore == self.secondPlayerScore):
            return f"{self.pointTennis(self.firstPlayerScore)} all"
        return f"{self.firstPlayerName} : {self.pointTennis(self.firstPlayerScore)}  ; {self.secondPlayerScore} : {self.pointTennis(self.secondPlayerScore)} "


""""
if __name__ == '__main__':
    game = Tennis("nadal", "federer")

    print(game.getScore())
    print(game.firstPlayerScore)
    print(game.secondPlayerScore)
    print(game.highestScore())
    print(game.gameWin())
    print(f"{game.highestScore()} is winner with  {game.secondPlayerScore} !!!!.")
    print(game.pointTennis(game.secondPlayerScore))
      game.firstPlayerPoint()
    game.firstPlayerPoint()
    game.firstPlayerPoint()
    game.secondPlayerPoint()
    game.secondPlayerPoint()
    game.secondPlayerPoint()
    game.firstPlayerPoint()
    game.firstPlayerPoint()
    game.firstPlayerPoint()
"""
