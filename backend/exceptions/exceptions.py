# -*- coding: utf-8 -*-


class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args)
        self.data = kwargs

