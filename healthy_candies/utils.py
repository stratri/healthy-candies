import matplotlib.pyplot as plt
from typing import Dict
import pandas as pd
import numpy as np


def plot_decription(info: Dict[str, str]) -> None:
    """
        Helper funciton to add label/title to plots.
        Title, xlabel and ylabel are supported.

        eg:
        plot_decription({'title': "My title"})
    """
    if 'title' in info.keys():
        plt.title(info['title'])
    if 'xlabel' in info.keys():
        plt.xlabel(info['xlabel'])
    if 'ylabel' in info.keys():
        plt.ylabel(info['ylabel'])
    if 'xscale' in info.keys():
        plt.xscale(info['xscale'])
    if 'yscale' in info.keys():
        plt.xscale(info['yscale'])


def log_bins(serie: pd.Series, nb_of_bins: int) -> np.ndarray:
    """
      This function generates a logarithmic series between
      min(serie) and max(serie),
      with nb_of_bins intervals
    """
    begin = min(serie)
    end = max(serie)
    bins = np.logspace(np.log10(begin), np.log10(end), nb_of_bins+1)
    # Make sure there are no numerical errors on the beginning and end
    bins[0] = begin
    bins[-1] = end
    return bins
