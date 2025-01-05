from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    #metodo del bottone nuova partita
    def handleNuova(self,e):
        self._view._txtMrim.value=self._model._Mmax
        self._view._btnProva.disabled = False
        self._view._txtTentativo.disabled = False
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.Text("Indovina il numero.",color="green"))
        self._model.inizializza()
        self._view._pb.value = self._model._Mrim / self._model._Mmax
        self._view._page.update()

    #metodo del bottone prova il numero
    def handleProva(self,e):
        #catturo il numero
        tentativo = self._view._txtTentativo.value
        self._view._txtTentativo.value = ""

        #controllo il numero
        try:
            intTentativo = int(tentativo)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Il tentativo deve essere un intero."))
            self._view._page.update()
            return
        #se va bene, chiedo al model e gli passo il numero per lavorarci sopra
        # il metodo restituisce due valori
        mRim, result = self._model.indovina(intTentativo)

        #aggiornamento progress bar
        self._view._txtMrim.value = mRim
        self._view._pb.value = self._model._Mrim / self._model._Mmax
        self._view._page.update()

        #analizzo il risultato del metodo. Se ho finito i tentativi
        if mRim == 0:
            self._view._btnProva.disabled=True
            self._view._txtTentativo.disabled=True
            self._view._lvOut.controls.append(ft.Text("Hai perso! :-( Il segreto era: "
                                                      + str(self._model.segreto)))
            self._view._page.update()
            return
        # analizzo il risultato del metodo. Se ho indovinato il numero....
        if result == 0:
            self._view._lvOut.controls.append(ft.Text("Hai vinto! :-)"))
            self._view._btnProva.disabled=True
            self._view._page.update()
            return
        # analizzo il risultato del metodo. Se il numero è più piccolo
        elif result == -1:
            self._view._lvOut.controls.append(ft.Text("Nope, il segreto è più piccolo."))
            self._view._page.update()
            return
        # analizzo il risultato del metodo. Se il numero è più grande
        else:
            self._view._lvOut.controls.append(ft.Text("Nope, il segreto è più grande."))
            self._view._page.update()
            return

