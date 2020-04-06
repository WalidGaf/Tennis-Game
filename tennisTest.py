import unittest
from tennisGame import Tennis

class tennisTest(unittest.TestCase):

    def setUp(self):
        self.game = Tennis("nadal", "federer")

    def testLoveALL(self):
        love = self.game.getScore()
        self.assertEqual(love, "love all")

    def testDeuce(self):
        self.game.firstPlayerPoint()
        self.game.secondPlayerPoint()
        self.game.firstPlayerPoint()
        self.game.secondPlayerPoint()
        self.game.firstPlayerPoint()
        self.game.secondPlayerPoint()
        deuce = self.game.getScore()
        self.assertEqual(deuce, "Deuce")

    def testAdvantage(self):
        self.game.firstPlayerPoint()
        self.game.secondPlayerPoint()
        self.game.firstPlayerPoint()
        self.game.secondPlayerPoint()
        self.game.firstPlayerPoint()
        self.game.secondPlayerPoint()
        self.game.firstPlayerPoint()
        avantage = self.game.getScore()
        self.assertEqual(avantage, "Advatange nadal")

    def testWinner(self):

        self.game.firstPlayerPoint()
        self.game.secondPlayerPoint()
        self.game.firstPlayerPoint()
        self.game.secondPlayerPoint()
        self.game.firstPlayerPoint()
        self.game.secondPlayerPoint()
        self.game.firstPlayerPoint()
        self.game.firstPlayerPoint()
        winner = self.game.getScore()
        self.assertEqual(winner, "nadal is winner !!!!.")

if __name__ == '__main__':
    unittest.main()
