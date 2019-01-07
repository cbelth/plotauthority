import matplotlib.pyplot as plt
import seaborn as sns
from color_theory import ColorTheory
import numpy as np
from theme import Theme
import utils

class Plotter:
    def __init__(self, theme=None):
        if not theme:
            self.theme = Theme() # default theme
        self.color_genie = ColorTheory()
        return

    def set_theme(self, theme):
        self.theme = theme

    def plot(self,
             title,
             xlabel='X-axis',
             ylabel='Y-axis',
             size=(15,10),
             xscale=None,
             yscale=None,
             fontsize=16,
             xlim=None,
             ylim=None,
             background=(0.8588235294117647, 0.8588235294117647, 0.8588235294117647)):
        '''
        The main plot function. This is responsible for managing the plot.
        Every type of plot should call this function.

        :title: The title for the plot
        :xlabel: The xlabel for the plot
        :ylabel: The ylabel for the plot
        '''
        fig = plt.figure(figsize=size)
        if xlim:
            plt.xlim(xlim)
        if ylim:
            plt.ylim(xlim)
        plt.title(title, fontsize=fontsize)
        plt.xlabel(xlabel, fontsize=fontsize)
        plt.ylabel(ylabel, fontsize=fontsize)
        if xscale:
            plt.xscale(xscale)
        if yscale:
            plt.yscale(yscale)
        plt.rcParams['axes.facecolor'] = background
        plt.grid()

    def save(self, path):
        if not path.endswith('.jpg'):
            print('Path to save should end in .jpg')
            return
        plt.savefig(path, format='jpg', dpi=500)

    def color(self, given_color):
        if given_color:
            if given_color == 1:
                return self.theme.primary
            elif given_color == 2:
                return self.theme.secondary
            elif given_color == 3:
                return self.theme.secondary
            elif given_color == 'random':
                return self.color_genie.get_color()
            return given_color
        else:
            return self.theme.primary

    def rank(self,
             values,
             title='Rank Plot',
             xlabel='rank of values',
             ylabel='value',
             save_path=None,
             color=None,
             alpha=1.,
             xscale='log',
             yscale='log'):
        '''
        Plots a set of values by rank, from largest to smallest.

        :values: the values to plot
        '''
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale)
        plt.plot(sorted(values, reverse=True), 'o', color=self.color(color), alpha=alpha)
        if save_path:
            self.save(save_path)
        plt.show()

    def multi_rank(self,
                   values_list,
                   title='Rank Plot',
                   xlabel='ranks of values',
                   ylabel='values',
                   save_path=None,
                   color=None,
                   alpha=1.,
                   xscale='log',
                   yscale='log'):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale)
        for values in values_list:
            plt.plot(sorted(values, reverse=True), 'o', color=self.color(color, 'random'), alpha=alpha)
        if save_path:
            self.save(save_path)
        plt.show()


    def histogram(self,
                  values,
                  title='Histogram',
                  xlabel='bins',
                  ylabel='number of items in bins',
                  save_path=None,
                  color=None,
                  alpha=1.,
                  bins=10,
                  xscale=None,
                  yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale)
        plt.hist(values, bins=bins, edgecolor='black', color=self.color(color), alpha=alpha)
        if save_path:
            self.save(save_path)
        plt.show()

    def multi_histogram(self,
                        values_list,
                        title='Histogram',
                        xlabel='bins',
                        ylabel='number of items in bins',
                        save_path=None,
                        bins=10,
                        labels=['first', 'second'],
                        colors=None,
                        alphas=[0.5, 0.5],
                        xscale=None,
                        yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale)
        #if not utils.check_args(values_list, colors, alphas):
        #    return
        for i, values in enumerate(values_list):
            color = colors[i] if colors else i + 1
            plt.hist(values, bins=bins, edgecolor='black', color=self.color(color), alpha=alphas[i], label=labels[i])
        plt.legend(fontsize=16)
        if save_path:
            self.save(save_path)
        plt.show()

    def loglog(self,
               values,
               title='log-log',
               xlabel='rank',
               ylabel='value',
               save_path=None,
               color=None,
               alpha=1.,
               xscale='symlog',
               yscale='symlog'):
        self.plot(title=title, xscale=xscale, yscale=yscale)
        plt.plot(sorted(values, reverse=True), 'o', color=self.color(color), alpha=alpha)
        if save_path:
            self.save(save_path)
        plt.show()

    def density_scatter(self,
                        x,
                        y,
                        z='heat',
                        title='Density Scatter',
                        save_path=None,
                        color=None,
                        alpha=1.,
                        xscale='symlog',
                        yscale='symlog',
                        vmin=0.0,
                        vmax=None):
        #self.plot(title=title, xscale=xscale, yscale=yscale)
        xy_unique = dict()
        # count the number of occurrences of each x, y value
        for _x, _y in zip(x, y):
            if (_x, _y) not in xy_unique:
                xy_unique[(_x, _y)] = 0.0
            xy_unique[(_x, _y)] += 1.0
        x = list(_x for _x, _ in xy_unique.keys())
        y = list(_y for _, _y in xy_unique.keys())
        # the 3rd dimension is the counts
        z_vals = list(xy_unique.values())

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.grid() # TODO: ax.grid(True, linestyle='-', color='0.75'?)
        if z == 'heat': # plot density as heat map
            if not vmax:
                vmax = np.max(z_vals) # make one heat color range to max density
            density = ax.scatter(x, y, s=20, c=z_vals, marker='o', cmap='gist_heat_r', vmin=vmin, vmax=vmax)
        else: # plot density as point size
            density = ax.scatter(x, y, s=z_vals, marker='o')
        fig.colorbar(density, label='density of points')
        if save_path:
            self.save(save_path)
        plt.show()

    def x_vs_y(self,
               x,
               y,
               title='y = f(x)',
               xlabel='x',
               ylabel='f(x)',
               save_path=None,
               color=None,
               alpha=1.,
               xlim=None,
               ylim=None,
               xscale=None,
               yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim)
        plt.plot(x, y, '-o', color=self.color(color), alpha=alpha)
        if save_path:
            self.save(save_path)
        plt.show()

    def confusion_matrix(self,
                         values,
                         title='Confusion Matrix',
                         save_path=None,
                         names=None,
                         vmin=None,
                         vmax=None):
        self.plot(title=title, ylabel='', xlabel='')
        sns.heatmap(values, xticklabels=names, yticklabels=names, vmin=vmin, vmax=vmax)
        if save_path:
            self.save(save_path)
        plt.show()
