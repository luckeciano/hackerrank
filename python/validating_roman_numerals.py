thoushand = "M{0,3}"
hundred = "(C[MD]|D?C{0,3})"
dez = "(X[CL]|L?X{0,3})"
n = "(I[XV]|V?I{0,3})"

regex_pattern = thoushand + hundred + dez + n + "$"	# Do not delete 'r'.

import re