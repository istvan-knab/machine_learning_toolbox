import numpy
import random as random

from reinforcement_learning.Environments.TicTacToe import TicTacToe

class QTable:
    def __init__(self):

        self.Q_table = {}
        self.epsilon = 0
        self.epsilon_decay = 0
        self.epsilon_decay_step = 0
        self.epsilon_decay_rate = 0

    def bellman_equation(self, state):
        ...
