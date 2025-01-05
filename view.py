from tkinter.constants import CENTER

import flet as ft


class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    # metodo che carica gli elementi
    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        #Row 1
        #poiche il view non accede al modello, il valore di default  del modello lo prendo
        # passando attraverso il controller  -> controller.modello.attributi....
        self._txtNmax = ft.TextField(label="N Max", width=100,
                                     disabled=True, value=self._controller._model._NMax)
        self._txtMmax = ft.TextField(label="Tentativi Max", width=100,
                                     disabled=True, value=self._controller._model._Mmax)
        self._txtMrim = ft.TextField(label="Tentativi Rim", width=100,
                                     disabled=True, value=self._controller._model._Mrim)

        self.row1 = ft.Row([self._txtNmax,self._txtMmax, self._txtMrim], alignment=ft.MainAxisAlignment.CENTER)


        #Row 2
        self._txtTentativo = ft.TextField(label="Tentativo", width=100,disabled=True)
        self._btnNuova = ft.ElevatedButton(text="Nuova Partita",
                                           on_click=self._controller.handleNuova) #metodo nel controller
        self._btnProva = ft.ElevatedButton(text="Prova",
                                           on_click=self._controller.handleProva, #metodo nel controller
                                           disabled=True)
        self.row2 = ft.Row([self._txtTentativo,self._btnNuova, self._btnProva], alignment=ft.MainAxisAlignment.CENTER)

        #progressBar
        self._pb = ft.ProgressBar(width=400, color="amber")

        #spazio per scrivere
        self._lvOut = ft.ListView(width=300)
        self.row3 = ft.Row([self._lvOut], alignment=ft.MainAxisAlignment.CENTER)

        #aggiungi gli elementi alla pagina e aggiorna
        self._page.add(self.row1,self.row2,self._pb,self.row3)




    def setController(self, controller):
        self._controller = controller


