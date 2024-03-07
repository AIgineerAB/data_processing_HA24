import matplotlib.pyplot as plt 
from pathlib import Path
import pandas as pd 

# in jupyter notebook
# DATA_PATH = "../../data/data_processing/"
DATA_PATH = Path(__file__).parents[2] / "data" / "data_processing"

class StoryCharts:
    def __init__(self) -> None:
        pass

    def _plot(self, x, y, colors = "#0c4a6e", **label_kwargs):
        self.fig, self.ax = plt.subplots()

        plt.show()
    
    def Line(self, x, y):
        pass 

# this is to be able to run this as a standalone script 
# the code below won't run when imported from another script
# as __name__ will be "story_charts.py" when imported
if __name__ == "__main__":
    print("\n\n")
    # print(DATA_PATH)
    # print(__name__)

    df = pd.read_csv(DATA_PATH / "co2_annmean_mlo.csv", skiprows=43)

    print(df.head())

    sc = StoryCharts()
    sc._plot(2,3)