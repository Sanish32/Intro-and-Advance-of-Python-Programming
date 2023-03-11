# Write your solution here
class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        if player1_word==1:
            return 1
        elif player2_word==2:
            return 2

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self,rounds:int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word)>len(player2_word):
            return 1
        elif len(player2_word)>len(player1_word):
           return 2


class MostVowels(WordGame):
    def __init__(self,rounds:int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        count1=0
        for items in player1_word:
            if items in "aeiou":
                count1+=1
        count2=0
        for items in player2_word:
            if items in "aeiou":
                count2+=1
        if count1>count2:
            return 1
        elif count2>count1:
            return 2
        return 0

class RockPaperScissors(WordGame):
    def __init__(self,rounds:int):
        super().__init__(rounds)

    def round_winner(self, player1, player2):
        options={"rock":1,"paper":2,"scissors":3}

        if not player2 in options and not player1 in options:
            return 0
        elif not player2 in options:
            return 1
        elif not player1 in options:
            return 2

        x=options[player2]-options[player1]
        
        
        if x==-2 or x==1:
            return 2
        elif x==0:
            return 0
        return 1
        
if __name__=="__main__":
    p=MostVowels(3)
    p.play()
