class EpsilonGreedyPolicy:
    def __init__(self):
        self.action_set = ("explore","exploit")

    def step(self):
        self.choose_action()
        self.update()

    def update(self):
        pass
    def choose_action(self):
        pass
