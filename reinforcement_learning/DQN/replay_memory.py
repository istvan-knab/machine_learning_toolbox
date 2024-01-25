from collections import deque


class ReplayMemory:
    def __init__(self, BUFFER_SIZE, BATCH_SIZE):
        self.memory = deque(maxlen=BUFFER_SIZE)
        self.BATCH_SIZE = BATCH_SIZE

    def add(self, state, action, reward, next_state):
        ...

    def sample(self):
        ...


