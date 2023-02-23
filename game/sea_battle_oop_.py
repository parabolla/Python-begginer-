from random import shuffle, randint, random


class Player:
    def __init__(self):
        _horizon = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        counter = 10
        g = []
        while counter > 0:
            counter -= 1
            g.append([_horizon[random.randint(0, 9)], random.randint(1, 10)])
            for i in g:
                Board(i[0], i[1])
class Board:
    def __init__(self, horizont: str, vertical: str) -> None:
        self.horizont = horizont
        self.vertical = vertical
        self.position = []

    def position(self):
        self.position = [self.horizont,self.vertical]
        print(self.position)
        return self.position


    @property
    def desk(self):
        print(f"что на доске {self.horizont}{self.vertical}")
        return f"что на доске {self.horizont}{self.vertical}"

    @desk.setter
    def desk(self, value):
        return self.position.pop()


def main():
    player1 = Player
    bord1 = Board
    bord1.position
    bord1.desk
    print(player1)
    print(bord1)
    print(bord1.position)
    print(bord1.desk)
    print(Board)

if __name__ == "__main__":
    main()
