import matplotlib.pyplot as plt 
from pathlib import Path
import pandas as pd 

# in jupyter notebook
# DATA_PATH = "../../data/data_processing/"
DATA_PATH = Path(__file__).parents[2] / "data" / "data_processing"


# this is to be able to run this as a standalone script 
# the code below won't run when imported from another script
# as __name__ will be "story_charts.py" when imported
if __name__ == "__main__":
    print("\n\n")
    print(DATA_PATH)
    print(__name__)
