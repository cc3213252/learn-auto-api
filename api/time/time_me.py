# encoding: utf-8
# Date: 2024/11/26 19:04

__author__ = 'yudan.chen'

from os import environ
from time import localtime


def timezone(event, context):
    return localtime(0).tm_zone


def location(event, context):
    return environ['AWS_REGION']