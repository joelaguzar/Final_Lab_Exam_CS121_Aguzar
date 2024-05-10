from .user_manager import UserManager
from .score import Score
from .user import User
import datetime
import os
import random

class DiceGame:
    def __init__(self):
        self.user_manager = UserManager()
        self.scores = []
        self.current_user = None
        self.load_scores()
        
    def load_scores(self):
        try:
            with open("data/rankings.txt", "r") as file:
                for line in file:
                    username, game_id, points, wins = line.strip().split("|")
                    score = Score(username, (game_id))
                    score.points = int(points)
                    score.wins = int(wins)
                    self.scores.append(score)
        except FileNotFoundError:
            return None
        except ValueError:
            print("Error: Invalid data in ranking file.")
            return None
        
    def save_scores(self):
        with open("data/rankings.txt", "w") as file:
            for score in self.scores:
                file.write(f"{score.username}|{score.game_id}|{score.points}|{score.wins}\n")
    
    def play_game(self):
        if not self.current_user:
            print("\nYou need to log in to play the game.")
            return
        player_name = self.current_user.username

        now = datetime.datetime.now()
        game_id = now.strftime("%d %b %Y %I:%M %p") 
        current_score = Score(self.current_user.username, game_id)
        stage = 1

        while True:
            print(f"\n--- STAGE {stage} ---")
            player_wins = 0
            computer_wins = 0

            rounds = 3
            while rounds > 0:
                player_roll = random.randint(1, 6)
                computer_roll = random.randint(1, 6)
                print(f"\n{player_name} rolled: {player_roll}")
                print(f"Computer rolled: {computer_roll}")

                if player_roll > computer_roll:
                    print(f"{player_name} win this round!")
                    player_wins += 1
                    current_score.points += 1
                elif computer_roll > player_roll:
                    print("Computer wins this round!")
                    computer_wins += 1
                else:
                    print("It's a tie! Roll again.")
                rounds -= 1

            if player_wins >= 2:
                print(f"\n{player_name} won stage {stage}!")
                current_score.points += 3
                current_score.wins += 1
                choice = input("\nEnter any character to continue to the next stage, or 0 to stop playing: ")
                if choice == '0':
                    break
                stage += 1
            else:
                print("Game over. You didn't win any stage.")
                break

        self.scores.append(current_score)
        self.save_scores()
        print(f"\nTotal Points: {current_score.points}")
        print(f"Stages Won: {current_score.wins}")