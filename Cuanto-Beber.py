import random
guessestaken = 0

print ('Hola! Cual es tu nombre?')
myname = input()

number = random.randint(1,10)
print(myname + ' , tengo sed de la peligrosa y estoy pensando tomarme entre 1 y 10 Cheves')

while guessestaken < 6:
    print('Podras ayudarme a decidir cuantas cheves tomar hoy ??')
    guess=input()
    guess=int(guess)

    guessestaken = guessestaken +1

    if guess < number:
        print('Son Muy Pocas')
    if guess > number:
        print('No Crees tu que sean demasiadas para hoy ?')

    if guess == number:
        break
if  guess == number:
    guessestaken = str(guessestaken)
    print('Bueno ' + myname + ' Despues de incistirme ' + guessestaken + ' veces , me has convencido vamos a tomarnos unas ' + str(number) +' cheves cada quien' )

if guess != number:
    number = str(number)
    print('No me convences yo pensaba en unas ' + number + 'cheves mas o menos')

