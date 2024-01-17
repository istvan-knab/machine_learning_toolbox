import gymnasium as gym
import numpy as np
import pygame
class TicTacToe(gym.Env):
    def __init__(self):

        self.state = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.info = {}

    def step(self, action):

        self.state = np.reshape(self.state, newshape=(9,1))
        if self.state[action] == 1:
            done = True
            reward = -1
        else:
            self.state[action] = 1
            reward = 0.5
            done = False

        self.state = np.reshape(self.state, newshape=(3,3))

        return self.state, reward, done, self.info

    def reset(self):

        self.state = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

        return self.state
    def render(self, mode='human'):
        ...
    def close(self):
        ...
    def seed(self, seed):
        ...
    def action_handler(self):
        ...
    def check_done(self):
        ...
