from tkinter import *
from tkinter.messagebox import *
import math, random
#J'ai importé random, math et messagebox qui n'ont rien à voire mais je me suis dit pk pas pour une amélioration future !




'''calculatrice permettant d'effectuer des calcules simples (addition, soustraction, division et multiplication). Il reste certaines
choses à améliorer comme la fonction Supp qui ne permet pas un véritable retour en arrière, enlever les boutons au profit d'un detecteur
de souris et de clic '''



def reset():
	#Fonction pour tout reset 
	Texte.set(' ')
	calc.set('')

def existanceNb(nb):
	#Fonction pour savoir si un nb peut être converti en float
	try :
		nb = float(nb)
	except ValueError :
		calc.set('')
		Texte.set('ERROR')
	else:
		return True

def Calcule():
	#Tout d'abord, regarde s'il y a un signe de calcule dans le str contenant l'opération (calc) et si oui effectue l'opération
	#dictée dans calc, renvoit True si un calcule été fait
	s = calc.get()
	if '*' in s:
		if existanceNb(s.split('*')[0]) and existanceNb(s.split('*')[1]):
			res = float(s.split('*')[0]) * float(s.split('*')[1])
			Texte.set(str(testInt(res)) + ' ' )
			calc.set(res)
			return True
	elif '+' in s:
		if existanceNb(s.split('+')[0]) and existanceNb(s.split('+')[1]):
			res = float(s.split('+')[0]) + float(s.split('+')[1])
			Texte.set(str(testInt(res)) + ' ' )
			calc.set(res)
			return True
	elif '-' in s:
		if existanceNb(s.split('-')[0]) and existanceNb(s.split('-')[1]):
			res = float(s.split('-')[0]) - float(s.split('-')[1])
			Texte.set(str(testInt(res)) + ' ')
			calc.set(res)
			return True
	elif ':' in s:
		if existanceNb(s.split(':')[0]) and existanceNb(s.split(':')[1]):
			res = float(s.split(':')[0]) / float(s.split(':')[1])
			Texte.set(str(testInt(res)) + ' ' )
			calc.set(res)
			return True
	else:
		return False

def testInt(nb):
	#va de paire avec la fonction Calcule, permet un meilleur affichage (au lieu d'avoir 14.0 on obtiendra 14)
	if int(nb) == nb:
		return int(nb)
	else:
		return nb

def Res():
	#Fonction associer au bouton =, ne permet pas de faire des calcules avec le résultat obtenu
	Calcule()
	calc.set('')

def Supp():
	#supprime le dernier caractère des deux str
	if not len(calc.get()) == 0:
		calc.set(calc.get()[:-1])
		Texte.set(Texte.get()[:-1])

#Pour les 4 prochaines fonctions, on regarde s'il y a un signe d'opération contenu dans calc et si oui on réalise l'opération
def multiplier():
	if not Error():
		if not Calcule():
			Texte.set('x')
		calc.set(calc.get()+ '*')
		print(calc.get())
def plus():
	if not Error():
		if not Calcule():
			Texte.set('+')
		calc.set(calc.get()+ '+')
		print(calc.get())
def moins():
	if not Error():
		if not Calcule():
			Texte.set('-')
		calc.set(calc.get()+ '-')
		print(calc.get())
def diviser():
	if not Error():
		if not Calcule():
			Texte.set(':')
		calc.set(calc.get()+ ':')
		print(calc.get())

def Error():
	#elle est la pour vérifier que l'utilisateur ne commence pas un calcule par +, -, * ou :
	if calc.get() == '':
		Texte.set("ERROR")
		return True
	else:
		return False

#Fonctions pour les boutons nombre et le points
def sept():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':', ' '] or calc.get() == '':
		#cette condition permet une amélioration de l'affichage
		Texte.set('7')
	else:
		Texte.set(Texte.get() + '7')
	calc.set(calc.get()+ '7')
	print(calc.get())
def huit():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':', ' '] or calc.get() == '':
		Texte.set('8')
	else:
		Texte.set(Texte.get() + '8')
	calc.set(calc.get()+ '8')
	print(calc.get())
def neuf():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':', ' '] or calc.get() == '':
		Texte.set('9')
	else:
		Texte.set(Texte.get() + '9')
	calc.set(calc.get()+ '9')
	print(calc.get())
def quatre():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':', ' '] or calc.get() == '':
		Texte.set('4')
	else:
		Texte.set(Texte.get() + '4')
	calc.set(calc.get()+ '4')
	print(calc.get())
def cinq():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':', ' '] or calc.get() == '':
		Texte.set('5')
	else:
		Texte.set(Texte.get() + '5')
	calc.set(calc.get()+ '5')
	print(calc.get())
def six():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':', ' '] or calc.get() == '':
		Texte.set('6')
	else:
		Texte.set(Texte.get() + '6')
	calc.set(calc.get()+ '6')
	print(calc.get())
def un():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':',' '] or calc.get() == '':
		Texte.set('1')
	else:
		Texte.set(Texte.get() + '1')
	calc.set(calc.get()+ '1')
	print(calc.get())
def deux():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':', ' '] or calc.get() == '':
		Texte.set('2')
	else:
		Texte.set(Texte.get() + '2')
	calc.set(calc.get()+ '2')
	print(calc.get())
def trois():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':',' '] or calc.get() == '':
		Texte.set('3')
	else:
		Texte.set(Texte.get() + '3')
	calc.set(calc.get()+ '3')
	print(calc.get())
def zéro():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':',' '] or calc.get() == '':
		Texte.set('0')
	else:
		Texte.set(Texte.get() + '0')
	calc.set(calc.get()+ '0')
	print(calc.get())
def point():
	if Texte.get()[-1] in ['R', 'e', '+', '-', 'x', ':',' '] or calc.get() == '':
		Texte.set('.')
	else:
		Texte.set(Texte.get() + '.')
	calc.set(calc.get()+ '.')
	print(calc.get())


#initialisation de l'asistant graphique
root = Tk()
root.title('Calculatrice')
root['bg'] = 'bisque'

#initialisation des variables
Texte = StringVar()
Texte.set('Bienvenue')
calc = StringVar()

#label où se trouve les calcules
Label(root, textvariable = Texte, width = '10').grid(row = 1, column = 2)

#Les boutons
Button(root, text = 'AC', width = '10', command = reset).grid(row = 2, column = 1)
Button(root, text = 'DEL',width = '10',command = Supp).grid(row = 2, column = 2)
Button(root, text = 'x',width = '10',command =multiplier).grid(row = 2, column = 3)
Button(root, text = '+',width = '10',command =plus).grid(row = 3, column = 1)
Button(root, text = '-',width = '10',command =moins).grid(row = 3, column = 2)
Button(root, text = ':',width = '10',command =diviser).grid(row = 3, column = 3)
Button(root, text = '7',width = '10',command =sept).grid(row = 4, column = 1)
Button(root, text = '8',width = '10',command =huit).grid(row = 4, column = 2)
Button(root, text = '9',width = '10',command =neuf).grid(row = 4, column = 3)
Button(root, text = '4',width = '10',command =quatre).grid(row = 5, column = 1)
Button(root, text = '5',width = '10',command =cinq).grid(row = 5, column = 2)
Button(root, text = '6',width = '10',command =six).grid(row = 5, column = 3)
Button(root, text = '1',width = '10',command =un).grid(row = 6, column = 1)
Button(root, text = '2',width = '10',command =deux).grid(row = 6, column = 2)
Button(root, text = '3',width = '10',command =trois).grid(row = 6, column = 3)
Button(root, text = '.',width = '10',command =point).grid(row = 7, column = 1)
Button(root, text = '0',width = '10',command =zéro).grid(row = 7, column = 2)
Button(root, text = '=',width = '10',command = Res).grid(row = 7, column = 3)

root.mainloop()