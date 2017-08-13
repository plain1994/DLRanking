#!/usr/bin/env python
# coding:utf-8

import os
import requests
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DLRanking.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


def main():
    from allframe.models import frameInfo
    frameInfo.objects.all().delete()
    headers = {"Authorization": "cc5f7d6c71541964dbcff7b4cbf45d233a7d8690"}
    theano = requests.get('https://api.github.com/repos/Theano/Theano').json()
    #print(theano)
    frameInfo.objects.create(name=theano['full_name'],
                             sname=theano['name'],
                             fork_num=theano['forks_count'],
                             star_num=theano['stargazers_count'],
                             watch_num=theano['subscribers_count'],
                             http_link=theano['html_url'],
                             img_link=theano['organization']['avatar_url'],
                             description=theano['description'])

    tensorflow = requests.get('https://api.github.com/repos/tensorflow/tensorflow').json()
    # print(theano)
    frameInfo.objects.create(name=tensorflow['full_name'],
                             sname=tensorflow['name'],
                             fork_num=tensorflow['forks_count'],
                             star_num=tensorflow['stargazers_count'],
                             watch_num=tensorflow['subscribers_count'],
                             http_link=tensorflow['html_url'],
                             img_link=tensorflow['organization']['avatar_url'],
                             description=tensorflow['description'])
    pytorch = requests.get('https://api.github.com/repos/pytorch/pytorch').json()
    # print(theano)
    frameInfo.objects.create(name=pytorch['full_name'],
                             sname=pytorch['name'],
                             fork_num=pytorch['forks_count'],
                             star_num=pytorch['stargazers_count'],
                             watch_num=pytorch['subscribers_count'],
                             http_link=pytorch['html_url'],
                             img_link=pytorch['organization']['avatar_url'],
                             description=pytorch['description'])
    caffe = requests.get('https://api.github.com/repos/BVLC/caffe').json()
    # print(theano)
    frameInfo.objects.create(name=caffe['full_name'],
                             sname=caffe['name'],
                             fork_num=caffe['forks_count'],
                             star_num=caffe['stargazers_count'],
                             watch_num=caffe['subscribers_count'],
                             http_link=caffe['html_url'],
                             img_link=caffe['organization']['avatar_url'],
                             description=caffe['description'])
    keras = requests.get('https://api.github.com/repos/fchollet/keras').json()
    # print(theano)
    frameInfo.objects.create(name=keras['full_name'],
                             sname=keras['name'],
                             fork_num=keras['forks_count'],
                             star_num=keras['stargazers_count'],
                             watch_num=keras['subscribers_count'],
                             http_link=keras['html_url'],
                             img_link=keras['owner']['avatar_url'],
                             description=keras['description'])
    deeplearning4j = requests.get('https://api.github.com/repos/deeplearning4j/deeplearning4j').json()
    # print(theano)
    frameInfo.objects.create(name=deeplearning4j['full_name'],
                             sname=deeplearning4j['name'],
                             fork_num=deeplearning4j['forks_count'],
                             star_num=deeplearning4j['stargazers_count'],
                             watch_num=deeplearning4j['subscribers_count'],
                             http_link=deeplearning4j['html_url'],
                             img_link=deeplearning4j['organization']['avatar_url'],
                             description=deeplearning4j['description'])
    dlib = requests.get('https://api.github.com/repos/davisking/dlib').json()
    # print(theano)
    frameInfo.objects.create(name=dlib['full_name'],
                             sname=dlib['name'],
                             fork_num=dlib['forks_count'],
                             star_num=dlib['stargazers_count'],
                             watch_num=dlib['subscribers_count'],
                             http_link=dlib['html_url'],
                             img_link=dlib['owner']['avatar_url'],
                             description=dlib['description'])
    dynet = requests.get('https://api.github.com/repos/clab/dynet').json()
    # print(theano)
    frameInfo.objects.create(name=dynet['full_name'],
                             sname=dynet['name'],
                             fork_num=dynet['forks_count'],
                             star_num=dynet['stargazers_count'],
                             watch_num=dynet['subscribers_count'],
                             http_link=dynet['html_url'],
                             img_link=dynet['organization']['avatar_url'],
                             description=dynet['description'])
    sonnet = requests.get('https://api.github.com/repos/deepmind/sonnet').json()
    # print(theano)
    frameInfo.objects.create(name=sonnet['full_name'],
                             sname=sonnet['name'],
                             fork_num=sonnet['forks_count'],
                             star_num=sonnet['stargazers_count'],
                             watch_num=sonnet['subscribers_count'],
                             http_link=sonnet['html_url'],
                             img_link=sonnet['organization']['avatar_url'],
                             description=sonnet['description'])
    neon = requests.get('https://api.github.com/repos/NervanaSystems/neon').json()
    # print(theano)
    frameInfo.objects.create(name=neon['full_name'],
                             sname=neon['name'],
                             fork_num=neon['forks_count'],
                             star_num=neon['stargazers_count'],
                             watch_num=neon['subscribers_count'],
                             http_link=neon['html_url'],
                             img_link=neon['organization']['avatar_url'],
                             description=neon['description'])
    caffe2 = requests.get('https://api.github.com/repos/caffe2/caffe2').json()
    #print(theano)
    frameInfo.objects.create(name=caffe2['full_name'],
                             sname=caffe2['name'],
                             fork_num=caffe2['forks_count'],
                             star_num=caffe2['stargazers_count'],
                             watch_num=caffe2['subscribers_count'],
                             http_link=caffe2['html_url'],
                             img_link=caffe2['organization']['avatar_url'],
                             description=caffe2['description'])
    CNTK = requests.get('https://api.github.com/repos/Microsoft/CNTK').json()
    # print(theano)
    frameInfo.objects.create(name=CNTK['full_name'],
                             sname=CNTK['name'],
                             fork_num=CNTK['forks_count'],
                             star_num=CNTK['stargazers_count'],
                             watch_num=CNTK['subscribers_count'],
                             http_link=CNTK['html_url'],
                             img_link=CNTK['organization']['avatar_url'],
                             description=CNTK['description'])
    chainer = requests.get('https://api.github.com/repos/chainer/chainer').json()
    # print(theano)
    frameInfo.objects.create(name=chainer['full_name'],
                             sname=chainer['name'],
                             fork_num=chainer['forks_count'],
                             star_num=chainer['stargazers_count'],
                             watch_num=chainer['subscribers_count'],
                             http_link=chainer['html_url'],
                             img_link=chainer['organization']['avatar_url'],
                             description=chainer['description'])
    mxnet = requests.get('https://api.github.com/repos/apache/incubator-mxnet').json()
    #print(theano)
    frameInfo.objects.create(name=mxnet['full_name'],
                             sname='mxnet',
                             fork_num=mxnet['forks_count'],
                             star_num=mxnet['stargazers_count'],
                             watch_num=mxnet['subscribers_count'],
                             http_link=mxnet['html_url'],
                             img_link=mxnet['organization']['avatar_url'],
                             description=mxnet['description'])
    torch7 = requests.get('https://api.github.com/repos/torch/torch7').json()
    #print(theano)
    frameInfo.objects.create(name=torch7['full_name'],
                             sname=torch7['name'],
                             fork_num=torch7['forks_count'],
                             star_num=torch7['stargazers_count'],
                             watch_num=torch7['subscribers_count'],
                             http_link=torch7['html_url'],
                             img_link=torch7['organization']['avatar_url'],
                             description=torch7['description'])
    tflearn = requests.get('https://api.github.com/repos/tflearn/tflearn').json()
    # print(theano)
    frameInfo.objects.create(name=tflearn['full_name'],
                             sname=tflearn['name'],
                             fork_num=tflearn['forks_count'],
                             star_num=tflearn['stargazers_count'],
                             watch_num=tflearn['subscribers_count'],
                             http_link=tflearn['html_url'],
                             img_link=tflearn['organization']['avatar_url'],
                             description=tflearn['description'])
    Paddle = requests.get('https://api.github.com/repos/PaddlePaddle/Paddle').json()
    # print(theano)
    frameInfo.objects.create(name=Paddle['full_name'],
                             sname=Paddle['name'],
                             fork_num=Paddle['forks_count'],
                             star_num=Paddle['stargazers_count'],
                             watch_num=Paddle['subscribers_count'],
                             http_link=Paddle['html_url'],
                             img_link=Paddle['organization']['avatar_url'],
                             description=Paddle['description'])


    #print(frameInfo.objects.all()[0].description)

if __name__ == "__main__":
    main()
    print('Done!')