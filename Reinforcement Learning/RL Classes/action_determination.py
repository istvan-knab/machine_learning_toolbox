import random as random
class EpsilonGreedyPolicy:
    def __init__(self, EPSILON_DECAY):
        self.action_set = ("explore","exploit")
        self.EPSILON_DECAY = EPSILON_DECAY
        self.epsilon = 1

    def step(self) -> float:
        action_type = self.choose_action_type()
        action = self.choose_action()
        self.update()

        return action

    def update(self):
        self.epsilon = self.EPSILON_DECAY * self.epsilon
    def choose_action(self):
        pass
    def choose_action_type(self):
        baseline = random.random()
        if self.epsilon >= baseline:
            action_type = self.action_set[0]
        else:
            action_type = self.action_set[1]

        return action_type
