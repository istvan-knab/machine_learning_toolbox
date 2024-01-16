import torch
import gymnasium as gym

if __name__ == '__main__':
    # creating environment
    env = gym.make('CartPole-v1')

    # adding an agent
    ...
    # training loop
    for episode in range(EPISODES):
        state = env.reset()
        done = False
        while not done:
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            agent.train(state, action, reward, next_state, done)
            state = next_state



    print("Training done...")
    # Final log