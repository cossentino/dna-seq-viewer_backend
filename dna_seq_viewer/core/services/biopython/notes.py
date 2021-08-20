import pdb
from operator import itemgetter


mydict = {'user': 'fred', 'name': 'fred2', 'age': 25}


test = itemgetter('user', 'name')(mydict)

pdb.set_trace()
