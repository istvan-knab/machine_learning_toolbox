import random as random
import torch
from torch import FloatTensor


class EpsilonGreedyPolicy:

    def __init__(self, EPSILON_DECAY):
        self.action_set = ("explore", "exploit")
        self.EPSILON_DECAY = EPSILON_DECAY
        self.epsilon = 1

    def step(self) -> float:
        """
        This function is the connection between the agent and the epsilon greedy
        policy
        :return: A choosen value from the action set
        """
        action_type = self.choose_action_type()
        action = self.choose_action(action_type)
        self.update()

        return action

    def update(self):
        self.epsilon = self.EPSILON_DECAY * self.epsilon

    def choose_action(self, action_type:  str) -> float:
        """
        Here will be choosen the random or the optimal solution
        :param action_type: explore or exploit
        :return: action in form of a numerical output
        """
        if action_type == "explore":
            pass
        else:
            pass

        action = None
        return action

    def choose_action_type(self):
        baseline = random.random()
        if self.epsilon >= baseline:
            action_type = self.action_set[0]
        else:
            action_type = self.action_set[1]

        return action_type
