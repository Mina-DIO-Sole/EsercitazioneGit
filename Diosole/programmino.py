somma = 0

while True:
    numero = int(input("Inserisci un numero intero: "))
    
    
    if numero == 0:
        break  
    
    
    somma += numero

print("La somma di tutti i numeri inseriti è:", somma)