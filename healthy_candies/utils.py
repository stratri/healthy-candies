from typing import Dict

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import pandas as pd


def plot_settings(info: Dict[str, str]) -> None:
    """
        Helper function to set several plot parameters simply
        Title, xlabel and ylabel are supported.

        eg:
        plot_settings({'title': "My title"})
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
        plt.yscale(info['yscale'])


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


# taken from http://gvallver.perso.univ-pau.fr/?p=712
def show_colors(colors):
    """
    Draw a square for each color contained in the colors list
    given in argument.

    `colors`: array of tuple of RGB values
    """
    with plt.rc_context(plt.rcParamsDefault):
        fig = plt.figure(figsize=(6, 1), frameon=False)
        ax = fig.add_subplot(111)
        for x, color in enumerate(colors):
            ax.add_patch(
                mpl.patches.Rectangle(
                    (x, 0), 1, 1, facecolor=color
                )
            )
        ax.set_xlim((0, len(colors)))
        ax.set_ylim((0, 1))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect("equal")

    return fig
