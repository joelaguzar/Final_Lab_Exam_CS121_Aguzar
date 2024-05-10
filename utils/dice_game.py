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