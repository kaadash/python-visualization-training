#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math


from matplotlib import colors

def plot_color_gradients(gradients, names):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    #rc('text', usetex=True)
    #rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)

    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    fig.savefig('my-gradients.pdf')


def hsv2rgb(h, s, v):
    r = 0
    g = 0
    b = 0
    if v == 0:
        r = 0
        g = 0
        b = 0
    else:
        h /= 60
        i = math.floor(h)
        f = h - i
        p = v * (1 - s)
        q = v * (1 - (s * f))
        t = v * (1 - (s * (1 - f)))
        if i == 0:
            r = v
            g = t
            b = p
        elif i == 1:
            r = q
            g = v
            b = p
        elif i == 2:
            r = p
            g = v
            b = t
        elif i == 3:
            r = p
            g = q
            b = v
        elif i == 4:
            r = t
            g = p
            b = v
        elif i == 5:
            r = v
            g = p
            b = q

    return (r, g, b)


def gradient_rgb_bw(v):
    return (v, v, v)


def gradient_rgb_gbr(v):
    if v < 0.5:
        r = 0
        g = 1 - 2 * v
        b = 2 * v
    if v > 0.5:
        r = 2 * v - 1
        g = 0
        b = 1 - r
    return (r, g, b)


def gradient_rgb_gbr_full(v):
    if v < 0.25:
        r = 0
        g = 1
        b = 4 * v
    elif v < 0.5:
        r = 0
        g = 2 - 4 * v
        b = 1
    elif v < 0.75:
        r = 4 * v - 2
        g = 0
        b = 1
    else:
        r = 1
        g = 0
        b = 4 - 4 * v

    return (r, g, b)


def gradient_rgb_wb_custom(v):
    # 111
    if v < 1/7:
        r = 1
        g = 1
        b = 1 - 7 * v
    # 110
    elif v < 2/7:
        r = 1
        g = 2 - 7 * v
        b = 0
    # 100
    elif v < 3/7:
        r = 1
        g = 0
        b = 7 * v
    # 101
    elif v < 4/7:
        r = 4 - 7 * v
        g = 0
        b = 1
    # 001
    elif v < 5/7:
        r = 0
        g = 7 * v - 5
        b = 1
    # 011
    elif v < 6/7:
        r = 0
        g = 1
        b = 6 - 7 * v
    # 010
    else:
        r = 0
        g = 7 - 7 * v
        b = 0
    # 000
    return (r, g, b)




def gradient_hsv_bw(v):
    return hsv2rgb(0, 0, v)


def gradient_hsv_gbr(v):
    return hsv2rgb((360 * v + 180) * 0.666, 1, 1)



def gradient_hsv_unknown(v):
    x = 1 - v
    return hsv2rgb((360 * x) * 0.333, 0.5, 1)


def gradient_hsv_custom(v):
    return hsv2rgb(180 * v, v, 1)


if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])