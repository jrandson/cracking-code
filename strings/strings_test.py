
import unittest

from strings import StringLib

class StringLab(unittest.TestCase):

	_string = StringLib()

	def test_has_repeated_caracter(self):
		s = 'abc'
		self.assertEqual(False,self._string.has_repeated_caracter(s))
		s = 'aab'
		self.assertEqual(True,self._string.has_repeated_caracter(s))
		s = 'a'
		self.assertEqual(False,self._string.has_repeated_caracter(s))

	def test_reverse(self):
		s = 'a'
		self.assertEqual('a',self._string.reverse(s))
		s = 'ab'
		self.assertEqual('ba',self._string.reverse(s))
		s = 'abc'
		self.assertEqual('cba',self._string.reverse(s))

	def test_remove_blank(self):
		s = ''
		self.assertEqual('',self._string.remove_blank(s))
		s = 'a b'
		self.assertEqual('ab',self._string.remove_blank(s))
		s = ' a'
		self.assertEqual('a',self._string.remove_blank(s))
		s = 'b '
		self.assertEqual('b',self._string.remove_blank(s))

	def test_is_eneagram(self):
		s = 'abc'
		self.assertEqual(False,self._string.is_eneagram(s))
		s = 'a'
		self.assertEqual(True,self._string.is_eneagram(s))
		s = 'abcba'
		self.assertEqual(True,self._string.is_eneagram(s))
		s = 'aa'
		self.assertEqual(True,self._string.is_eneagram(s))

	def test_replace_with(self):
		s = 'Hello name'
		search = ':name'
		replace = 'Joe'
		self.assertEqual('Hello Joe',self._string.replace_with(s,search,replace))

if __name__ == '__main__':
	unittest.main()