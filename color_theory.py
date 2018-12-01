import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import random

class ColorTheory:
    '''
    This class is designed to help make a plot's color scheme aesthetically
    pleasing given humanity's current understanding of psychology and color.
    '''
    def __init__(self):
        self.default_palettes = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']
        self.basic_palettes = ['Blues', 'Greens', 'Reds']
        self.diverging_palettes = ['BrBG', 'RdBu_r', 'coolwarm']
        # all palettes
        self.palettes = self.default_palettes + self.basic_palettes + self.diverging_palettes
        # all colors from palettes
        self.colors = self.load_colors()

    def load_colors(self):
        '''
        This method loads all the named Matplotlib colors and colors from the seaborn palettes.
        '''
        colors = list(mcolors.BASE_COLORS.values()) + list(mcolors.CSS4_COLORS.values())
        for palette_name in self.palettes:
            palette = sns.color_palette(palette_name)
            for color in palette:
                colors.append(color)
        return colors

    def get_color(self):
        '''
        For now, this method just returns a random color. In the future, it
        will pick colors more intelligently.

        :return: a colorself.
        '''
        return random.choice(self.colors)

    def view_colors(self):
        '''
        This code is slightly adapted from https://matplotlib.org/examples/color/named_colors.html

        Use this method to avoid having to Google "matplotlib named colors" every
        time you plot.
        '''
        colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

        # Sort colors by hue, saturation, value and name.
        by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                        for name, color in colors.items())
        sorted_names = [name for hsv, name in by_hsv]

        n = len(sorted_names)
        ncols = 4
        nrows = n // ncols + 1

        fig, ax = plt.subplots(figsize=(15, 10))

        # Get height and width
        X, Y = fig.get_dpi() * fig.get_size_inches()
        h = Y / (nrows + 1)
        w = X / ncols

        for i, name in enumerate(sorted_names):
            col = i % ncols
            row = i // ncols
            y = Y - (row * h) - h

            xi_line = w * (col + 0.05)
            xf_line = w * (col + 0.25)
            xi_text = w * (col + 0.3)

            ax.text(xi_text, y, name, fontsize=(h * 0.8),
                    horizontalalignment='left',
                    verticalalignment='center')

            ax.hlines(y + h * 0.1, xi_line, xf_line,
                      color=colors[name], linewidth=(h * 0.6))

        ax.set_xlim(0, X)
        ax.set_ylim(0, Y)
        ax.set_axis_off()

        fig.subplots_adjust(left=0, right=1,
                            top=1, bottom=0,
                            hspace=0, wspace=0)
        plt.show()

    def view_color_palettes(self):
        '''
        Use this method to list a bunch of possible color palettes.
        '''
        for palette_name in self.palettes:
            palette = sns.color_palette(palette_name)
            sns.palplot(palette)
            print(palette_name)
            plt.show()
