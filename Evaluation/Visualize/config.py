from enum import Enum


class InputProcessing():
    def __init__(self):
        pass

    def plot_class(self):
        self.PLOT_CLASS = input("\t 1:Matplotlib \n \t 2:Seaborn \n \t Your choice : ")
        if self.PLOT_CLASS == 1:
            self.PLOT_CLASS == "matplotlib"
        elif self.PLOT_CLASS == 2:
            self.PLOT_CLASS == "seaborn"
        else:
            raise EnvironmentError("You have to choose between mpl and sns")

        return self.PLOT_CLASS
    def choose_plot_type(self):

        if self.PLOT_CLASS == "matplotlib":
            pass

        if self.PLOT_CLASS == "seaborn":
            pass

        return "string"

class ConfigParameters(Enum):

    set = InputProcessing()
    PLOT_CLASS = set.plot_class()
    PLOT_TYPE = set.choose_plot_type()
    PLOT_TITLE = input("Title:")



