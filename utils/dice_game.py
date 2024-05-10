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
        