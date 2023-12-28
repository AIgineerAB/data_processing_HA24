import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
from inspect import currentframe

DATA_PATH = Path(__file__).parents[1] / "data"
STYLES_PATH = Path(__file__).parent / "styles"
FIGURES_PATH = Path(__file__).parents[1] / "figures"

class StoryChart:
    def __init__(self) -> None:
        plt.style.use(STYLES_PATH / "base.mplstyle")

    def _set_labels(self, title, xlabel, ylabel):
        self.ax.set_xlabel(xlabel, loc="left")
        self.ax.set_ylabel(ylabel, loc="top")
        self.ax.set_title(title, loc="left", pad=15)

    def _plot(self, x,y, colors = "#0c4a6e", **label_kwargs):
        self.fig, self.ax = plt.subplots()
        
        # go back a frame in the call stack and retrieve name of method calling
        calling_method_name = currentframe().f_back.f_code.co_name
        if calling_method_name == "Line":
            self.ax.plot(x, y, color=colors)
        elif calling_method_name == "Bar":
            self.ax.bar(x, y, color=colors)
            self.ax.tick_params(axis='x', colors="#1f2937")
        
        self._set_labels(**label_kwargs)
        self.fig.tight_layout()
        plt.show()


    def Line(self, x, y, colors="#0c4a6e", **label_kwargs):
        self._plot(x,y, colors, **label_kwargs)

    def Bar(self, x, y, colors="#0c4a6e", **label_kwargs):
        self._plot(x,y, colors, **label_kwargs)


# manual testing
if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH / "co2_annmean_mlo.csv", skiprows=43)

    sc = StoryChart()
    title = "The annual mean of CO$_2$ emissions measured in Mauna Loa has \nincreased every year since 1959"
    sc.Line(
        df["year"],
        df["mean"],
        title=title,
        colors="#e11d48",
        xlabel="YEARS FROM 1959",
        ylabel="CO$_2$ MOLE FRACTON IN PPM",
    )

    sc.fig.savefig(FIGURES_PATH / "CO2_emissions_annual_mean.png", dpi=200)


    df = pd.read_html("https://www.worldometers.info/co2-emissions/co2-emissions-by-country/", index_col=0)[0]
    df = df.rename({"Share  of world": "World percentage"}, axis=1)
    df["World percentage"] = df["World percentage"].str.rstrip("%").astype(float)
    number_countries = 8
    
    dff = df.head(8)
    top_emitter = 3
    red, gray = "#be123c", "#4b5563"
    colors = [red] * top_emitter + [gray] * (number_countries - top_emitter)

    sc.Bar(
        x=dff["Country"],
        y=dff["World percentage"],
        title="The top three CO$_2$ emitters in the world stand for more than\n50% of the worlds total CO$_2$ emissions in 2022.",
        xlabel="TOP 8 CO$_2$ EMITTERS IN THE WORLD",
        ylabel="% OF THE WORLDS CO$_2$",
        colors= colors
    )

    sc.fig.savefig(FIGURES_PATH / "world_CO2_emissions.png", dpi=200)
