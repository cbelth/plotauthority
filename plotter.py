import matplotlib.pyplot as plt
from color_theory import ColorTheory

class Plotter:
    def __init__(self):
        self.color_genie = ColorTheory()
        return

    def plot(self, title, size=(15,10), xscale=None, yscale=None):
        '''
        The main plot function. This is responsible for managing the plot.
        Every type of plot should call this function.
        '''
        fig = plt.figure(figsize=size)
        if xscale:
            plt.xscale(xscale)
        if yscale:
            plt.yscale(yscale)

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
