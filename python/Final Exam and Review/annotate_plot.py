import matplotlib.pyplot as plt
import numpy as np

def annotate_plot(annotations: dict):
    """
    Add text annotations to a plot using Pyplot's text function.

    Parameters:
    annotations (dict): Each key is the label (str), and each value is a dict with:
        - 'position' (tuple or list of 2 floats): (x, y) coordinates
        - 'alignment' (tuple or list of 2 str): (horizontalalignment, verticalalignment)
        - 'fontsize' (float): Size of the text
    """
    for label, props in annotations.items():
        # Ensure proper unpacking and provide fallbacks
        position = props.get('position', (0.5, 0.5))
        ha, va = props.get('alignment', ('center', 'center'))
        fontsize = props.get('fontsize', 12)

        if not isinstance(position, (tuple, list, np.ndarray)) or len(position) != 2:
            raise ValueError(f"Invalid position for label '{label}': must be a 2-element tuple/list")

        x, y = position

        plt.text(x, y, label,
                 horizontalalignment=ha,
                 verticalalignment=va,
                 fontsize=fontsize)
