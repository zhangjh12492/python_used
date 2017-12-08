import re
print(re.findall(r'\bf[a-z]*','which food or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the hat'))

print('tea for too'.replace('too', 'two'))


