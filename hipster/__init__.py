#!/usr/bin/python
 # -*- coding: utf-8 -*-

__all__ = ['hipster','config', 'errors']


from hipster import *

@singleton_with_methods
class Hipster():
    def __init__(self, token, proxy = None):
        self.AUTH_TOKEN = token
        self.PROXY = proxy

