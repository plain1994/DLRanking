from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from allframe import models
from itertools import chain

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components


# Create your views here.


def index(request):
    # return HttpResponse("hello worker")

    return render(request, "index.html")


def real(request):
    # return HttpResponse("hello worker")

    return render(request, "real.html")


def star(request):
    return render(request, "star.html")


def fork(request):
    return render(request, "fork.html")


def watch(request):
    return render(request, "watch.html")


def star_graph(request):
    starlist = models.frameInfo.objects.all().order_by('-star_num')
    factors = []
    starnums = []

    for frame in starlist:
        factors.append(frame.sname)
        starnums.append(frame.star_num)
    # print(factors)
    # print(starnums)

    p = figure(title="Star Graph", x_range=factors, y_range=(0, starnums[0] * 1.05),
               plot_width=1000, plot_height=350, tools="")
    p.vbar(x=factors, width=0.6, bottom=0,
           top=starnums, color="#CAB2D6")

    script, div = components(p, CDN)

    return JsonResponse({"script": script, "div": div})


def fork_graph(request):
    forklist = models.frameInfo.objects.all().order_by('-fork_num')
    factors = []
    forknums = []

    for frame in forklist:
        factors.append(frame.sname)
        forknums.append(frame.fork_num)
    # print(factors)
    # print(starnums)

    p = figure(title="Fork Graph", x_range=factors, y_range=(0, forknums[0] * 1.05),
               plot_width=1000, plot_height=350, tools="")
    p.vbar(x=factors, width=0.6, bottom=0,
           top=forknums, color="#CAB2D6")

    script, div = components(p, CDN)

    return JsonResponse({"script": script, "div": div})


def watch_graph(request):
    watchlist = models.frameInfo.objects.all().order_by('-fork_num')
    factors = []
    watchnums = []

    for frame in watchlist:
        factors.append(frame.sname)
        watchnums.append(frame.fork_num)
    # print(factors)
    # print(starnums)

    p = figure(title="Watch Graph", x_range=factors, y_range=(0, watchnums[0] * 1.05),
               plot_width=1000, plot_height=350, tools="")
    p.vbar(x=factors, width=0.6, bottom=0,
           top=watchnums, color="#CAB2D6")

    script, div = components(p, CDN)

    return JsonResponse({"script": script, "div": div})


def frameinfo(request):
    if request.method == "POST":
        starlist = models.frameInfo.objects.all().order_by('-star_num')
        forklist = models.frameInfo.objects.all().order_by('-fork_num')
        watchlist = models.frameInfo.objects.all().order_by('-watch_num')
        # watchnum = starlist[0].watch_num

        data = serializers.serialize("json", chain(starlist, forklist, watchlist))
    return HttpResponse(data)
