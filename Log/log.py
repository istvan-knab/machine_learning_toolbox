from neptune_ai import NeptuneAI
from tensorboard import TensorBoard


class Log():
    def __init__(self, log_type: str) -> None:
        self.select(log_type=log_type)

    def select(self, log_type: str) -> None:
        if log_type == "tensorboard":
            self.logger = TensorBoard()
        elif log_type == "neptuneai":
            self.logger = NeptuneAI()
        else:
            raise EnvironmentError("The logger must be Tensorboard or NeptuneAI")

    def update(self) -> None:
        pass

