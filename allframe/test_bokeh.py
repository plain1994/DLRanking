#!/usr/bin/env python
# coding:utf-8
from django.test import TestCase

# Create your tests here.

import os
import django

from bokeh.plotting import figure, show, output_file

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DLRanking.settings")

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


def main():
    from allframe.models import frameInfo
    starlist = frameInfo.objects.all().order_by('-star_num')
    factors = []
    starnums = []

    for frame in starlist:
        factors.append(frame.sname)
        starnums.append(frame.star_num)
    print(factors)
    print(starnums)

    output_file('vbar.html')
    #colors = ["red", "olive", "darkred", "goldenrod", "skyblue", "orange", "salmon"]

    p = figure(title="Star Graph", x_range=factors, y_range=(0, starnums[0] * 1.05),
               plot_width=1000, plot_height=600, tools="")
    p.vbar(x=factors, width=0.6, bottom=0,
           top=starnums, color="#CAB2D6")

    show(p)


if __name__ == "__main__":
    main()
    print('Done!')
