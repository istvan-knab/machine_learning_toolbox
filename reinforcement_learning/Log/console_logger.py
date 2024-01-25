class ConsoleLogger:
    def __init__(self):
        #Read the yaml file
        #get device
        ...

    def start_logging(self):
        print('Training Started---------------------')
        print(f"Logging number {self.log_number}")
        print(f"Episodes : {self.EPISODES}")
        print(f"Step size {self.step_size}")
        print(f"Discount factor {self.GAMMA}")
        print(f"Learning rate {self.ALPHA}")
        print(f"Device {self.device}")
        print("-------------------------------------")

    def logger_step(self, episode):
        print(f'Episode : {episode}')

    def final_logging(self):
        ...
