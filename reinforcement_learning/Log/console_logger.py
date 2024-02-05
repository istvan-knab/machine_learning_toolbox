class ConsoleLogger:
    def __init__(self, config):
        self.device = config["device"]
        #get device
        ...

    def start_logging(self):
        """
        This method is called by starting training
        :return: None
        """

        print('Training Started---------------------')
        print(f"Logging number {self.log_number}")
        print(f"Episodes : {self.EPISODES}")
        print(f"Step size {self.step_size}")
        print(f"Discount factor {self.GAMMA}")
        print(f"Learning rate {self.ALPHA}")
        print(f"Device {self.device}")
        print("-------------------------------------")

    def logger_step(self, episode, EPISODES, avg_reward, epsilon):
        """
        This logger is called in every episode
        :param episode: Counts of episodes
        :param avg_reward: Displays the average reward
        :param epsilon: Epsilon greedy policy
        :return:
        """

        print(f'------Episode : {episode}-------------')
        print(f'Progress : {episode / EPISODES} %')
        print(f"Average reward: {avg_reward}")
        print(f"Epsilon: {epsilon}")


    def final_logging(self):
        ...
