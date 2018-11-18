import matplotlib.pyplot as plt
from typing import Dict


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
