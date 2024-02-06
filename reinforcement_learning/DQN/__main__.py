import yaml
import gymnasium as gym
from collections import namedtuple

from reinforcement_learning.DQN.agent import DQNAgent
from reinforcement_learning.Log.neptune import Neptune
from reinforcement_learning.Log.console_logger import ConsoleLogger

def initialize() -> dict:
    """
    Reading learning parameters from .yaml file
    :return: a dictionary containing the parameters
    """

    with open('params.yaml', 'r') as file:
        config = yaml.safe_load(file)
        print(type(config))
    return config


if __name__ == '__main__':

    # creating environment
    env = gym.make('CartPole-v1',render_mode='human')

    # Determine hyperparameters
    config = initialize()

    #Add logger
    logger = ConsoleLogger(config)

    # adding an agent
    agent = DQNAgent(input_layer = config["state_size"],
                     hidden_layers=config["HIDDEN_LAYERS"],
                     output_layer = config["action_size"])

    #initialize target network
    target = agent
    # training loop
    for episode in range(1000):
        state = env.reset()
        done = False
        while not done:
            #action = agent.act(state)
            next_state, reward, done, _ = env.step(0)[:4]
            #agent.train(state, action, reward, next_state, done)

            state = next_state
            env.render()




    print("Training done...")
    # Final log