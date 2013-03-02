__author__ = 'stubborn'
from openuhw import OpenUHWResult,OpenUHW
import unittest

class TestOpenUHWResult(unittest.TestCase):
   def Setup(self):
      pass

   def test_instantiation(self):
      res = OpenUHWResult()
      self.assertEqual(res.title, '')
      self.assertEqual(res.answers, [])

   def test_title_setting(self):
      res = OpenUHWResult()
      test_val = "new title"
      res.title = test_val
      self.assertEqual(res.title, test_val)

   def test_answer_setting(self):
      res = OpenUHWResult()
      test_val1 = "item 1"
      test_val2 = "item 2"
      res.answers.append(test_val1)
      self.assertEqual(res.answers, [test_val1] )
      res.answers.append(test_val2)
      self.assertEqual(res.answers, [test_val1, test_val2,] )

   def test_str_converter(self):
      res = OpenUHWResult(title="test_x")
      test_val1 = dict(descr='x^2', result=4,)
      test_val2 = dict(descr='x^3', result=8.3234,)
      test_val3 = dict(descr='x^x', result=u"shjsss",)
      s1 = u"Answers for test_x:"
      self.assertEqual(s1, res.__str__())

      s1 = u"Answers for test_x:\nx^2=4"
      res.answers.append(test_val1)
      self.assertEqual(s1, res.__str__())

      s1 = u"Answers for test_x:\nx^2=4\nx^3=8.3234"
      res.answers.append(test_val2)
      self.assertEqual(s1, res.__str__())

      s1 = u"Answers for test_x:\nx^2=4\nx^3=8.3234\nx^x=shjsss"
      res.answers.append(test_val3)
      self.assertEqual(s1, res.__str__())

class TestOpenUHW(unittest.TestCase):
   def Setup(self):
      pass
   def test_make_hr_line(self):
      ou_hw = OpenUHW()
      def_str = '='*40
      self.assertEqual(ou_hw.make_hr_line(ch='=',length=40), def_str)
      special_str='~'*0
      self.assertEqual(ou_hw.make_hr_line(ch='~', length=0), special_str)
      normal_str='-'*80
      self.assertEqual(ou_hw.make_hr_line(ch='-', length=80), normal_str)

   def test_add_solver(self):
      ou_hw = OpenUHW()
      def solver_x():
         return dict(
            title="kuku",
            answer=[
               dict(descr='lala', result=0),
               dict(descr='lulu', result=1),
            ]
         )

      ou_hw.add_solver(solver_x)




def test_main():
   suite = unittest.TestSuite(
      tests=(
         TestOpenUHWResult,
      )
   )
   suite.run()



if __name__ == '__main__':
   test_main()