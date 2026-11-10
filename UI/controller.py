import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):      # riempio i due dropdown con le opzioni lette dal db
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for b in self._model.get_biblioteche():
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(b.nome))

        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for g in self._model.get_generi():
            self._view.dd_genere.options.append(ft.dropdown.Option(g))

    # CALLBACKS DROPDOWN
    def handle_biblioteca(self, e):
        print("Biblioteca selezionata")
        if self._view.dd_biblioteca.value == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = self._view.dd_biblioteca.value


    def handle_genere(self, e): # quando l'utente sceglie un genere salvo il genere
        print("Genere selezionato")
        if self._view.dd_genere.value == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = self._view.dd_genere.value

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        print("Button mostra libri clicked")
        result = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        self._view.lv_libri.controls.clear()
        # se la lista è vuota mostro l'alert e mi fermo
        if len(result) == 0:
            self._view.show_alert("Nessun libro trovato")
            self._view.update()
            return

        # il primo elemento è il numero di libri trovati
        self._view.lv_libri.controls.append(ft.Text(f"{len(result)}"))
        for libro in result:
            self._view.lv_libri.controls.append(ft.Text(f"{libro}"))
        self._view.update()
