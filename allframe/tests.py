#!/usr/bin/env python
# coding:utf-8
from django.test import TestCase

# Create your tests here.

import os
import requests
import django
from django.core import serializers

import json
from itertools import chain



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DLRanking.settings")

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


def main():
    from allframe.models import frameInfo
    data1 = serializers.serialize("json", frameInfo.objects.all().order_by('-star_num'))
    data2 = serializers.serialize("json", chain(frameInfo.objects.all().order_by('-star_num'),
                                                frameInfo.objects.all().order_by('-fork_num')))
    data = data1+data2
    print(len(json.loads(data2)))
    print(json.loads(data2)[0])
if __name__ == "__main__":
    main()
    print('Done!')