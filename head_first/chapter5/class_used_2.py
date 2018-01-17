class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name=a_name

johnny=NamedList('John Paul Jones')
print(type(johnny))
print(dir(johnny))
print('=========================\n')
# print(locals())

print(johnny)
johnny.append('Base player')
johnny.extend(['Composer','Arranger','Musician'])
print(johnny)