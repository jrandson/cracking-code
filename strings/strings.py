

class StringLib():

	def __init__(self):
		pass

	def has_repeated_caracter(self, str):
		for i in range(len(str)-1):
			for j in range(i+1, len(str)):
				if str[i] == str[j]:
					return True

		return False

	def reverse(self, str):
		str_reverse = ''
		lengh = len(str)
		for i in range(lengh):
			str_reverse += str[lengh - i -1]

		return str_reverse


	def remove_blank(self,str):
		new_str = ''
		for c in str:
			if not c  == ' ':
				new_str += c

		return new_str

	def is_eneagram(self, str):
		l = len(str)
		for i in range(l/2):
			if not str[i] == str[l-i-1]:
				return False

		return True

	def replace_with(self,str, seach,replace):
		new_str = ''
		for c in str:
			if c == seach:
				new_str += replace
			else:
				new_str += c

		return new_str
