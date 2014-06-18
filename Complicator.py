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
def starost(age):
	if  age<20:
		return 1
	elif age<30:
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

def calculate_complexity(p1, p2):
	p1 = Decimal(p1)
	p2 = Decimal(p2)
	comp = p1+p2
	realFeel = (p1+p2)/(2*MAX_SCORE)
	return str(comp), str(realFeel)

def bus(stevilo):
	if stevilo<2:
		return 1
	elif stevilo<3:
		return 2
	else:
		return MAX_SCORE


# KOMENTARJI:
# 1) Funkcija je vedno vracala 3, dokler smo imeli shranjeno naso
#    starost kot niz znakov (string)
# 2) raw_input() vrne string
# 3) print starost(int(age))
#    int - spremeni niz znakov v stevilo
# 4) %d is for writing the numbers

# PRIMERI funkcij:
# def age_score():
#	print starost(age)

# def display_age(age):
#	print age

# def funny_fun():
#	print age_score(5)

# def simple_fun():
#	print "Yeah!"


# With raw input
age = raw_input("How old are you? ")
# print "I'm %r years old." % age


# Funkcija za stevilo prijateljev na facebook-u
st = raw_input("Stevilo prijateljev na facebook-u? ")
fb_score = FBfriend(int(st))


# Complexity
score = calculate_complexity(starost(int(age)), fb_score)
print "Koncni rezultat: ", score


missBus = raw_input("How many buses did you miss? ")
bus_score = bus(int(missBus))
print bus_score


# deadline = raw_input("Do you have deadlines? ")




# print "Do you have deadlines?"
# deadline = raw_input()
# print "%r" % deadline




# import datetime
# currentTime = datetime.datetime.now()
# Ce das import datetime lahko izbrises v ukazih datetime
# today = date.today
# print currentTime
# Obvezno daj brez narekovajev, printa ti danasnji datum

# print "Do you have a lack of money?"
# money = raw_input()
# print "%r" % money

# print "How much?"
# x = raw_input()
# print "%r" % x

# x = raw_input("How much?")
# print x


# attending = ["loving it", "hating it", "don't know"]
# numberFamily = raw_input()
# temp =
# speedInternet =




