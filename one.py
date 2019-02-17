#https://github.com/eduardoportilho/rock-paper-scissor/blob/master/rps.py
#was used for starting idea

import random

moves = ["rock", "paper", "scissors"]


class Player():

    def __init__(self):

        self.score = 0

    def move(self):

        return moves[0]

    def learn(self, learn_move):

        pass
# parent player class


class TheRock(Player):
    def move(self):
        throw = moves[0]
        self.step = self.step + 1


class RandomPlayer(Player):
    def move(self):
        throw = random.choice(moves)
        return (throw)
# random player class


class Cycler(Player):

    def __init__(self):

        Player.__init__(self)
        self.step = 0

    def move(self):
        if self.step == 0:
            throw = moves[0]
            self.step = self.step + 1
        elif self.step == 1:
            throw = moves[1]
            self.step = self.step + 1
        else:
            throw = moves[2]
            self.step = self.step + 1
        return throw
# class cycles through the 3 moves


class ImitaterPlayer(Player):

    def __init__(self):

        Player.__init__(self)
        self.learn_move = Player.__init__(self)

    def move(self):
        if self.learn_move is None:
            throw = moves[0]
            # 1st move is rock
        else:
            throw = self.learn_move
            # 2nd move is humanplayers 1st move
            return (throw)

    def learn(self, learn_move):

        self.learn_move = learn_move
# imitating human player move's class


class HumanPlayer(Player):

    def move(self):

        throw = input('rock, paper, scissors? >')

        while throw != 'rock'and throw != 'paper'and throw != 'scissors':
            print('I do not understand. Please try again.')
            throw = input('rock, paper, scissors? >')
        return (throw)
# class asks to make selection between rock paper and scissors


class Game():

    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_game(self):

        print("Rock Paper Scissors, Go!")
        for round in range(3):
            print (f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print('You won!')
        elif self.p1.score < self.p2.score:
            print('You lost and the other player won.:(')
        else:
            print('The game was a tie!')
        print('The final score ' + str(self.p1.score) + ' TO ' +
              str(self.p2.score))
# prints info and calls playround class
# prints final score

    def play_single(self):
        print("Rock Paper Scissors, Go!")
        print (f"Round 1 of 1:")
        self.play_round()
        if self.p1.score > self.p2.score:
            print('You won!!!')
        elif self.p1.score < self.p2.score:
            print('You lost:(')
        else:
            print('The game was a tie!')
        print('The final score ' + str(self.p1.score) + ' TO ' +
              str(self.p2.score))
# one round of rps
# copy of play_game w/o for loop

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)
# calls play class & stores player move

    def play(self, move1, move2):
            print(f"You played {move1}")
            print(f"Opponent played {move2}")
            if beats(move1, move2):
                print ("**YOU WON!!!**")
                print(f"Score: Player 1: {move1}  Player 2: {move2}\n\n")
                self.p1.score += 1
                return 1
            elif beats(move2, move1):
                print ("** YOU LOST:( **")
                print(f"Score: Player 1: {move1}  Player 2: {move2}\n\n")
                self.p2.score += 1
                return 2
            else:
                print ("** It's A TIE **")
                print(f"Score: Player 1: {move1}  Player 2: {move2}\n\n")
                return 0


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
if __name__ == '__main__':
    answer = [Player(), RandomPlayer(), Cycler(), ImitaterPlayer()]
    p2 = input('Who would you like to face?: [1]TheRock, [2]Random,[3]Imitater,or [4]Cycler: >')
# answer is a player class list

    while p2 != 1 or p2 != 2 or p2 != 3 or p2 != 4:
        p2 = random.choice(answer)
        break

    if p2 == '1':
        p2 = Player()
    elif p2 == '2':
        p2 = RandomPlayer()
    elif p2 == '3':
        p2 = Cycler()
    elif p2 == '4':
        p2 = ImitaterPlayer()

    rounds = input('Enter for [o]ne game or [a]ll games: >')
    Game = Game(p2)
    while True:
        if rounds == 'o':
            Game.play_single()
            break
        elif rounds == 'a':
            Game.play_game()
            break
        else:
            print('I do not understand what you just said. Please try again.')
            rounds = input('Enter 0 for one game and 1 for all games: >')
# human player chooses to play how many rounds
