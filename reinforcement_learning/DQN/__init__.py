import yaml
import gymnasium as gym

from reinforcement_learning.DQN.agent import DQNAgent

def initialize() -> dict:
    with open('params.yaml', 'r') as file:
        config = yaml.safe_load(file)
        print(type(config))
    return


if __name__ == '__main__':
    # creating environment
    env = gym.make('CartPole-v1',render_mode='human')

    config = initialize()
    # adding an agent
    #agent = DQNAgent()
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