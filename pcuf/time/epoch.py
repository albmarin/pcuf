# -*- coding: utf-8 -*-
import time


def seconds():
    return int(round(time.time()))


def centiseconds():
    return int(round(time.time() * 100))


def milliseconds():
    return int(round(time.time() * 1000))
