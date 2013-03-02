__author__ = 'stubborn'
# -*- coding: utf8 -*-
import sys
# from unittest import TestCase
class OpenUHW:
   answers = []
   def __init__(self):
      pass

   def add(self, d):
      if not isinstance(d, dict):
         raise ValueError("result must be a dictionary!")
      self.answers.append(d)

   def print_out(self):
      for i, ans in enumerate(self.answers):
         idx = i+1
         print u"Answer #{idx}: ".format(**locals()),
         sys.stdout.flush()
         print u"title: {title}".format(**ans)
         for j, res in enumerate(ans.get("answer")):
            print u'{descr}={result}'.format(**res)

