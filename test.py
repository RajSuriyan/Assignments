import re
string='boo loo'
match=re.findall('[bl]oo',string,re.IGNORECASE)
print(match)