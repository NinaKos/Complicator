# Na zacetek damo knjiznice, ki jih uporabljamo
from datetime import datetime
from decimal import Decimal

# Naslednja sprem je 'najpomembnejsa', zato z veliko
MAX_SCORE = 3

# Funkcija
# V age (lahko poimenujes kako drugace) povemo s katero vrednostjo 
# naj dela funkcija
# Funkcije lahko imajo argumente ali ne
# Na podlagi tega kar dobijo vrzejo ven nek rezultat
# Funkcijo definiraj na zacetku datoteke !!
def starost(stevilo):
	if  stevilo<20:
		return 1
	elif stevilo<30:
		return 2
	else:
		return MAX_SCORE

def FBfriend(stevilo):
	if stevilo<100:
		return 1
	elif stevilo<200:
		return 2
	else:
		return MAX_SCORE

def bus(stevilo):
	if stevilo<2:
		return 1
	elif stevilo<3:
		return 2
	else:
		return MAX_SCORE

def family(stevilo):
	if stevilo<2:
		return 1
	elif stevilo<3:
		return 2
	else:
		return MAX_SCORE

def money(stevilo):
	if stevilo<100:
		return 1
	elif stevilo<300:
		return 2
	else:
		return MAX_SCORE

def calculate_complexity(p1, p2, p3, p4, p5):
	p1 = Decimal(p1)
	p2 = Decimal(p2)
	p3 = Decimal(p3)
	p4 = Decimal(p4)
	p5 = Decimal(p5)
	comp = p1+p2+p3+p4+p5
	realFeel = comp/(5*MAX_SCORE)
	return str(comp), str(realFeel)


age = raw_input("How old are you? ")
age_score = starost(int(age))

# Funkcija za stevilo prijateljev na facebook-u
st = raw_input("Number of friends on facebook? ")
fb_score = FBfriend(int(st))

# Funkcija za stevilo avtobusov
missBus = raw_input("How many buses did you miss? ")
bus_score = bus(int(missBus))

# Funkcija za stevilo druzinskih clanov
fam = raw_input("How many family members do you have? ")
fam_score = family(int(fam))

# Funkcija za denar
m = raw_input("How much money do you need? ")
money_score = money(int(m))

# Complexity
score = calculate_complexity(age_score, fb_score, bus_score, 
fam_score, money_score)
print "Result: ", score

