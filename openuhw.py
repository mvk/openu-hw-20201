#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "Max Kovgan <kovganm@gmail.com>,"
__doc__ = """
    defines:
        OpenUHWResult - howework result
        OpenUHWSolver - howework solver

"""


class OpenUHWResult:
    def __init__(self, title=None):
        self._title = title if title else ''
        self._answers = []
        self._res_str = u""

    @property
    def answers(self):
        return self._answers

    # answers = property(_get_answer)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,t):
        self._title = t

    # title = property(_get_title)

    def set_res_str(self):
        res_str = u"Answer"
        res_str += len(self._answers) > 1 and u"s " or u" "
        res_str += u"for "
        res_str += "{0}:".format(self._title)
        self._res_str = res_str

    def __str__(self):
        self.set_res_str()
        res_str = self._res_str
        for idx, ans in enumerate(self._answers):
            description = ans.get("descr")
            result = ans.get("result")
            tmp_str = u"\t{0}.{1}. {2}=".format(self._title, idx + 1, description)
            if isinstance(result, (float, int, )):
                tmp_str += unicode(result)
            else:
                tmp_str += result
            res_str += u"\n" + tmp_str
        return res_str


class OpenUHWSolver:
    def __init__(self):
        # _answers = []
        self._results = list()
        self._solvers = list()
        pass

    def make_hr_line(self, ch, length):
        return ch * length

    def hr_line(self, ch="=", length=40):
        print self.make_hr_line(ch, length)

    def add_solver(self, d):
        if not callable(d):
            raise ValueError(u"result must be a function!")
        self._solvers.append(d)
        self._results.append(None)
        return True

    def solve(self, print_solution=False):
        for idx, solver in enumerate(self._solvers):
            self._results[idx] = solver()
            if print_solution:
                print u"{0}".format(self._results[idx])
                self.hr_line()

