
__author__ = 'stubborn'
# -*- coding: utf8 -*-
import sys
# from unittest import TestCase
class OpenUHWResult:
   def __init__(self, title=None):
      self._title=title if title else ''
      self._answers=[]

   def _get_answer(self):
      return self._answers
   answers = property(_get_answer)

   def _get_title(self):
      return self._title
   title = property(_get_title)

   def __str__(self):
      res_str = u"Answers for {0}:".format(self._title)
      for ans in self._answers:
         description = ans.get("descr")
         result = ans.get("result")
         tmp_str = description + u"="
         if isinstance(result, (float, int, )):
            tmp_str += unicode(result)
         else:
            tmp_str += result
         res_str += u'\n'
         res_str += tmp_str
      return res_str


class OpenUHW:
   def __init__(self):
      # _answers = []
      self._results = []
      self._solvers = []
      pass

   def make_hr_line(self, ch, length):
      return ch*length

   def hr_line(self,ch="=", length=40):
      print self.make_hr_line(ch, length)

   def add_solver(self, d):
      if not callable(d):
         raise ValueError(u"result must be a function!")
      try:
         self._solvers.append(d)
         self._results.append(None)
      except Exception, e:
         return False
      return True

   def solve(self, print_solution=False):
      for idx, solver in enumerate(self._solvers):
         self._results[idx] = solver()
         if print_solution:
            print u"{0}".format(self._results[idx])
            self.hr_line()

