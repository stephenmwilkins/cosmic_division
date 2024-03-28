
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import cmasher as cmr

# set style
plt.style.use('matplotlibrc.txt')


all_divisions = {}
all_divisions['redshift'] =[
    ['low-redshift', 0.0, 0.5],
    ['intermediate-redshift', 0.5, 4.0],
    ['high-redshift', 4.0, 7.0],
    ['very-high redshift', 7.0, 10.0],
    ['ultra-high redshift', 10.0, 15.0],
    ['exceptionally-high redshift', 15.0, 20.0],
]

all_divisions['time_of_day'] =[
    ['evening', -1.0, 0.0],
    ['dusk', 0.0, 0.5],
    ['afternoon', 0.5, 2.0],
    ['noon', 1.0, 3.0],
    ['morning', 2.0, 10.0],
    ['dawn', 10., 20.0],
]

all_divisions['culinary1'] =[
    ['supper', -1.0, -0.5],
    ['dinner', -0.5, 0.5],
    ['afternoon tea', 0.5, 1.0],
    ['lunch', 1.0, 3.0],
    ['brunch', 3.0, 7.0],
    ['elevenses', 4.0, 7.0],
    ['second breakfast', 7., 10.0],
    ['breakfast', 10., 20.0],
]

all_divisions['culinary2'] =[
    ['supper', -1.0, -0.5],
    ['tea', -0.5, 0.5],
    ['afternoon snack', 0.5, 1.0],
    ['dinner', 1.0, 3.0],
    ['brunch', 3.0, 7.0],
    ['elevenses', 4.0, 7.0],
    ['second breakfast', 7., 10.0],
    ['breakfast', 10., 20.0],
]

def madau_and_dickinson(z):
    return 0.015 * ((1+z)**2.7) / (1+ ((1+z)/2.9)**5.6)



for division_scheme in ['redshift', 'time_of_day', 'culinary1', 'culinary2']:

    fig = plt.figure(figsize=(3.5, 3.5))

    bottom = 0.15
    height = 0.8
    left = 0.15
    width = 0.8

    ax = fig.add_axes((left, bottom, width, height))

    divisions = all_divisions[division_scheme] 

    colours = cmr.take_cmap_colors('cmr.guppy_r', len(divisions))

    # plot cosmic star formation history

    z = np.arange(-5., 20., 0.01)
    ax.plot(z, madau_and_dickinson(z), c='k', lw=2, alpha=0.1, label = 'Madau & Dickinson (2014) - extrapolated')

    z = np.arange(0.0, 8., 0.01)
    ax.plot(z, madau_and_dickinson(z), c='k', lw=1, alpha=0.5, label = 'Madau & Dickinson (2014)')


    for division, c in zip(divisions, colours):

        label, zmin, zmax = division

        ax.fill_between([zmin, zmax], [0., 0.], [100., 100.], alpha=0.1, color=c)
        ax.text(0.5*(zmin+zmax), 0.03, label.upper(), fontsize=7, ha='center', va='center', rotation=90., color=c,weight="bold")




    ax.legend(fontsize=6, labelspacing=0.05)

    ax.set_xlim([-1., 20])
    ax.set_ylim([0.001, 0.7])
    ax.set_yscale('log')



    ax.set_xlabel(r'$\rm z$')
    ax.set_ylabel(r'$\rm \rho_{\star}/M_{\odot}\ yr^{-1}\ Mpc^{-3}$')

    fig.savefig(f'figs/redshift_division-{division_scheme}.pdf')
    fig.clf()