import random

# È la classe dell'applicazione. Sarebbe la partita che istanzio quando lancio l'applicazione
class Model(object):
    def __init__(self):
        self._NMax = 100 #numero massimo
        self._Mmax = 6 #numero massimo di tentativi
        self._Mrim = self._Mmax  #tentativi rimasti
        self._segreto = None  # lo creo ad ogni partita lanciando il metodo inizializza()


    # quando premo il bottone "nuova partita" lancio questa funzione. Resetta tutto
    # crea numero segreto e riassegna i tentativi massimi a disposizione.
    # in questo modo non devo chiudere il programma e riaprirlo per ricominciare
    def inizializza(self):
        self._segreto = random.randint(1, self._NMax)  # numero segreto
        self._Mrim = self._Mmax                           # ripristino tentativi
        print(self._segreto)


    # la lancio quando premo il bottone "indovina"
    # l'utente prova un numero
    def indovina(self, tentativo):

        #se non ho più tentativi restituisco i tentivi =0 e un valore None che inidica fine partita
        if self._Mrim == 0:
            return self._Mrim, None
        # se ho ancora vite ne tolgo una e poi controllo.....
        else:
            self._Mrim = self._Mrim - 1
        # se il numero corrisponde restituisco le vite e 0
        if tentativo == self._segreto:
            return self._Mrim, 0
        # se il numero e maggiore restituisco le vite e -1
        elif tentativo > self._segreto:
            return self._Mrim, -1
        # se il numero è minore restituisco le vite e 1
        else:
            return self._Mrim, 1
