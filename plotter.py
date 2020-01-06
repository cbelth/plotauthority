import matplotlib.pyplot as plt
import seaborn as sns
from color_theory import ColorTheory
import numpy as np
from theme import Theme
import utils
from collections import defaultdict

class Plotter:
    def __init__(self, fontsize=30, theme=None, backend=None):
        self.fontsize = fontsize
        if not theme:
            self.theme = Theme() # default theme
        self.color_genie = ColorTheory()
        if backend:
            plt.switch_backend(backend)
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
        plt.title(title, fontsize=self.fontsize)
        plt.xlabel(xlabel, fontsize=self.fontsize)
        plt.ylabel(ylabel, fontsize=self.fontsize)
        if xscale:
            plt.xscale(xscale)
        if yscale:
            plt.yscale(yscale)

        plt.xticks(fontsize=self.fontsize)
        plt.yticks(fontsize=self.fontsize)
        plt.rcParams['axes.facecolor'] = background
        plt.grid()

    def save(self, path, dpi=500, sns_plot=None):
        if not path.endswith('.jpg'):
            print('Path to save should end in .jpg')
            return
        if sns_plot:
            sns_plot.savefig(path, format='jpg', dpi=dpi, bbox_inches='tight')
        else:
            plt.savefig(path, format='jpg', dpi=dpi, bbox_inches='tight')

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
             dpi=500,
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
            self.save(save_path, dpi)
        plt.show()

    def multi_rank(self,
                   values_list,
                   title='Rank Plot',
                   xlabel='ranks of values',
                   ylabel='values',
                   save_path=None,
                   dpi=500,
                   color=None,
                   alpha=1.,
                   xscale='log',
                   yscale='log'):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale)
        for values in values_list:
            plt.plot(sorted(values, reverse=True), 'o', color=self.color(color, 'random'), alpha=alpha)
        if save_path:
            self.save(save_path, dpi)
        plt.show()


    def histogram(self,
                  values,
                  title='Histogram',
                  xlabel='bins',
                  ylabel='number of items in bins',
                  save_path=None,
                  dpi=500,
                  color=None,
                  alpha=1.,
                  bins=10,
                  xlim=None,
                  xticks=None,
                  xscale=None,
                  yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim)
        plt.hist(values, bins=bins, edgecolor='black', color=self.color(color), alpha=alpha)
        if xticks:
            plt.xticks(np.arange(len(values)), xticks)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def basic_plot(self,
                   values,
                   title='A simple plot of the points',
                   xlabel='x',
                   ylabel='values',
                   save_path=None,
                   dpi=500,
                   color=None,
                   alpha=1.,
                   xticks=None,
                   xscale=None,
                   yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale)
        plt.plot(values, 'o', color=self.color(color), alpha=alpha)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def multi_histogram(self,
                        values_list,
                        title='Histogram',
                        xlabel='bins',
                        ylabel='number of items in bins',
                        save_path=None,
                        dpi=500,
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
            self.save(save_path, dpi)
        plt.show()

    def loglog(self,
               values,
               title='log-log',
               xlabel='rank',
               ylabel='value',
               save_path=None,
               dpi=500,
               color=None,
               alpha=1.,
               xscale='symlog',
               yscale='symlog'):
        self.plot(title=title, xscale=xscale, yscale=yscale)
        plt.plot(sorted(values, reverse=True), 'o', color=self.color(color), alpha=alpha)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def density_scatter(self,
                        x,
                        y,
                        z='heat',
                        title='Density Scatter',
                        save_path=None,
                        dpi=500,
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

        fig = plt.figure(figsize=(15,10))
        plt.rc('legend', fontsize=30)
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
            self.save(save_path, dpi)
        plt.show()

    def x_vs_y(self,
               x,
               y,
               title='y = f(x)',
               xlabel='x',
               ylabel='f(x)',
               save_path=None,
               dpi=500,
               color=None,
               alpha=1.,
               with_line=False,
               xlim=None,
               ylim=None,
               xscale=None,
               yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim)
        if with_line:
            plt.plot(x, y, '-o', color=self.color(color), alpha=alpha)
        else:
            plt.scatter(x, y, color=self.color(color), alpha=alpha)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def pdf(self,
            data,
            title='pdf',
            xlabel='x',
            ylabel='p(x)',
            save_path=None,
            dpi=500,
            color=None,
            alpha=0.8,
            marker='o',
            xlim=None,
            ylim=None,
            xscale='log',
            yscale='log'):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim)
        counts = defaultdict(int)
        for x in data:
            counts[x] += 1
        x = list()
        y = list()
        for d in sorted(list(set(data))):
            x.append(d)
            y.append(counts[d])
        y = np.asarray(y) / np.sum(y)
        plt.plot(x, y, marker, color=self.color(color), alpha=alpha)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def pareto(self,
               data,
               title='pareto',
               xlabel='x',
               ylabel='p(deg >= x)',
               save_path=None,
               dpi=500,
               color=None,
               alpha=0.8,
               marker='o',
               xlim=None,
               ylim=None,
               xscale='log',
               yscale='log'):
        counts = defaultdict(int)
        m = np.max(data)
        for x in data:
            counts[x] += 1
        x = list()
        y = list()
        s = len(data)
        for _x in sorted(list(set(data))):
            x.append(_x)
            s -= counts[_x]
            y.append(s)

        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim)
        y = np.asarray(y) / np.sum(y)
        plt.plot(x, y, marker, color=self.color(color), alpha=alpha)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def zipf(self,
             data,
             title='zipf',
             xlabel='rank',
             ylabel='val',
             save_path=None,
             dpi=500,
             color=None,
             alpha=1.,
             marker='o',
             xlim=None,
             ylim=None,
             xscale='symlog',
             yscale='symlog'):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim)
        plt.plot(sorted(data, reverse=True), marker, color=self.color(color), alpha=alpha)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def confusion_matrix(self,
                         values,
                         title='Confusion Matrix',
                         cmap='inverted',
                         with_nums=False,
                         save_path=None,
                         dpi=500,
                         names=None,
                         vmin=None,
                         vmax=None):
        self.plot(title=title, ylabel='', xlabel='')
        sns.set(font_scale=3)
        sns_plot = sns.heatmap(values,
                    xticklabels=names,
                    yticklabels=names,
                    vmin=vmin,
                    vmax=vmax,
                    annot=with_nums,
                    cmap=sns.cm.rocket_r if cmap == 'inverted' else None,
                    linewidth=1,
                    linecolor='black')
        sns_plot = sns_plot.get_figure()

        # from: https://github.com/mwaskom/seaborn/issues/1773
        # fix for mpl bug that cuts off top/bottom of seaborn viz
        b, t = plt.ylim() # discover the values for bottom and top
        b += 0.5 # Add 0.5 to the bottom
        t -= 0.5 # Subtract 0.5 from the top
        plt.ylim(b, t) # update the ylim(bottom, top) values
        plt.show() # ta-da!

        if save_path:
            self.save(save_path, dpi, sns_plot)
        plt.show()

    def x_vs_y_with_line(self,
                         x,
                         y,
                         title='y = f(x)',
                         xlabel='x',
                         ylabel='f(x)',
                         save_path=None,
                         dpi=500,
                         color=None,
                         alpha=1.,
                         xlim=None,
                         ylim=None,
                         xscale=None,
                         yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim)
        plt.scatter(x, y, color=self.color(color), alpha=alpha)
        _x = np.log(x) if xscale in {'log', 'symlog'} else x
        _y = np.log(y) if yscale in {'log', 'symlog'} else y
        slope, intercept = np.polyfit(_x, _y, deg=1)
        _x = range(int(round(np.min(x))), int(round(np.max(x)) * 2))
        _x = np.round(plt.xlim())
        _y = intercept + slope * np.log(_x) if xscale in {'log', 'symlog'} else intercept + slope * _x
        if yscale in {'log', 'symlog'}:
            _y = np.e ** _y
        plt.plot(_x, _y, color=self.color(color), alpha=alpha, label='slope = {}'.format(round(slope, 2)))
        plt.legend(fontsize=26)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def x_vs_y_with_log_func(self,
                             x,
                             y,
                             title='y = f(x)',
                             xlabel='x',
                             ylabel='f(x)',
                             save_path=None,
                             dpi=500,
                             color=None,
                             alpha=1.,
                             xlim=None,
                             ylim=None,
                             xscale=None,
                             yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim)
        plt.scatter(x, y, color=self.color(color), alpha=alpha)
        slope, intercept = np.polyfit(np.log(x), y, 1)
        _x = range(1, int(np.ceil(plt.xlim()[1])))
        _y = intercept + slope * np.log(_x)#* np.log(_x) if xscale in {'log', 'symlog'} else intercept + slope * _x
        #if yscale in {'log', 'symlog'}:
        #    _y = np.e ** _y
        print(slope, intercept)

        plt.plot(_x, _y, '-', color=self.color(color), alpha=alpha, label='exp = {}'.format(round(slope, 2)))
        #plt.legend(fontsize=16)
        plt.legend(fontsize=16)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def x_vs_y_multiple(self,
                        xs,
                        ys,
                        labels,
                        title='y = f(x)',
                        xlabel='x',
                        ylabel='f(x)',
                        save_path=None,
                        dpi=500,
                        colors=[None, None],
                        alpha=1.,
                        with_line=False,
                        xlim=None,
                        ylim=None,
                        xscale=None,
                        yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim)
        if with_line:
            for x, y, label, color in zip(xs, ys, labels, colors):
                plt.plot(x, y, '-o', label=label, color=self.color('random') if not color else color, alpha=alpha)
        else:
            for x, y, label, color in zip(xs, ys, labels, colors):
                plt.scatter(x, y, label=label, color=self.color('random') if not color else color, alpha=alpha)
        plt.legend(fontsize=30)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def x_vs_y_with_y_eq_x(self,
                           x,
                           y,
                           title='y = f(x)',
                           xlabel='x',
                           ylabel='f(x)',
                           save_path=None,
                           dpi=500,
                           color=None,
                           alpha=1.,
                           xlim=None,
                           ylim=None,
                           xscale=None,
                           yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim)
        plt.scatter(x, y, color=self.color(color), alpha=alpha)
        slope, intercept = (1, 0)
        _x = range(round(np.min(x)), round(np.max(x)) * 2)
        _x = np.round(plt.xlim())
        _y = intercept + slope * np.log(_x) if xscale in {'log', 'symlog'} else intercept + slope * _x
        plt.plot(_x, np.e ** _y, color=self.color(color), alpha=alpha, label='{} = {}'.format(ylabel, xlabel))
        plt.legend(fontsize=16)
        if save_path:
            self.save(save_path, dpi)
        plt.show()

    def bar(self,
            x,
            y,
            title='Bar plot',
            xlabel='items',
            ylabel='number',
            save_path=None,
            dpi=500,
            color=None,
            alpha=1.,
            xlim=None,
            xticks=None,
            xscale=None,
            yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim)
        plt.bar(x, y, color=self.color(color), alpha=alpha)
        if xticks:
            plt.xticks(np.arange(1, len(x) + 1), xticks, rotation=90)
        if save_path:
            self.save(save_path, dpi)
        plt.show()
