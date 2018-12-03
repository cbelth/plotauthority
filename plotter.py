import matplotlib.pyplot as plt
import seaborn as sns
from color_theory import ColorTheory
import numpy as np

class Plotter:
    def __init__(self):
        self.color_genie = ColorTheory()
        return

    def plot(self,
             title,
             xlabel='X-axis',
             ylabel='Y-axis',
             size=(15,10),
             xscale=None,
             yscale=None,
             fontsize=16,
             background=(0.8588235294117647, 0.8588235294117647, 0.8588235294117647)):
        '''
        The main plot function. This is responsible for managing the plot.
        Every type of plot should call this function.

        :title: The title for the plot
        :xlabel: The xlabel for the plot
        :ylabel: The ylabel for the plot
        '''
        fig = plt.figure(figsize=size)
        plt.title(titel, fontsize=fontsize)
        plt.xlabel(xlabel, fontsize=fontsize)
        plt.ylabel(ylabel, fontsize=fontsize)
        if xscale:
            plt.xscale(xscale)
        if yscale:
            plt.yscale(yscale)
        plt.rcParams['axes.facecolor'] = background
        plt.grid()

    def color(self, given_color):
        if given_color:
            return given_color
        else:
            return self.color_genie.get_color()

    def rank(self,
             values,
             title='Rank Plot',
             color=None,
             alpha=1.,
             xscale='log',
             yscale='log'):
        '''
        Plots a set of values by rank, from largest to smallest.

        :values: the values to plot
        '''
        self.plot(title=title, xscale=xscale, yscale=yscale)
        plt.plot(sorted(values, reverse=True), color=self.color(color), alpha=alpha)
        plt.show()

    def multi_rank(self,
                   values_list,
                   title='Rank Plot',
                   color=None,
                   alpha=1.,
                   xscale='log',
                   yscale='log'):
        self.plot(title=title, xscale=xscale, yscale=yscale)
        for values in values_list:
            plt.plot(sorted(values, reverse=True), color=self.color(color), alpha=alpha)
        plt.show()


    def histogram(self,
                  values,
                  title='Histogram',
                  color=None,
                  alpha=1.,
                  xscale=None,
                  yscale=None):
        self.plot(title=title, xscale=xscale, yscale=yscale)
        plt.hist(values, color=self.color(color), alpha=alpha)
        plt.show()

    def loglog(self,
               values,
               title='log-log',
               color=None,
               alpha=1.,
               xscale='symlog',
               yscale='symlog'):
        self.plot(title=title, xscale=xscale, yscale=yscale)
        plt.plot(sorted(values, reverse=True), 'o', color=self.color(color), alpha=alpha)
        plt.show()

    def density_scatter(self,
                        x,
                        y,
                        z='heat',
                        title='Density Scatter',
                        color=None,
                        alpha=1.,
                        xscale='symlog',
                        yscale='symlog',
                        vmin=0.0,
                        vmax=None):
        self.plot(title=title, xscale=xscale, yscale=yscale)
        xy_unique = dict()
        # count the number of occurrences of each x, y value
        for _x, _y in zip(x, y):
            if (_x, _y) not in xy_unique:
                xy_unique[(_x, _y)] = 0.0
            xy_unique[(_x, _y)] += 1.0
        x = list(_x for _x, _ in xy_unique.keys())
        y = list(_y for _, _y in xy_unique.keys())
        # the 3rd dimension is the counts
        z_vals = xy_unique.values()

        ax = fig.add_subplot(1, 1, 1)
        ax.grid(True, linestyle='-', color='0.75')
        if z = 'heat': # plot density as heat map
            if not vmax:
                vmax = np.max(z_vals) # make one heat color range to max density
            density = ax.scatter(x, y, s=20, c=z_vals, marker='o', cmap='gist_heat_r', vmin=vmin, vmax=vmax)
        else: # plot density as point size
            density = ax.scatter(x, y, s=z_vals, marker='o')
        fig.colorbar(density, label='density of points')
        plt.show()
