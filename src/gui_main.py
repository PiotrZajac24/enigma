from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QListWidgetItem, QDialog
import sys
from src.ui_mainwindow import Ui_MainWindow
from src.enigma_exceptions import *
from src.enigma_settings import Rotor, StaticRotor, ReverseRotor, ConnectedRotors, Settings, str_links, full_sample
from src.enigma_machine import Enigma
from src.io_enigma import read_from_json, read_text_from_file, read_text_from_json, write_to_file
from os.path import exists, splitext


class EnigmaWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loadFileButton.clicked.connect(self.openReadSettingsDialog)
        self.ui.writeFileButton.clicked.connect(self.openSaveSettingsDialog)
        self.ui.encryptButton.clicked.connect(self.encryptText)
        self.ui.saveSettings.clicked.connect(self.saveNewSettings)
        self.ui.textSettings.setText("Maszyna nie jest jeszcze skonfigurowana.")
        self.ui.clearSettings.clicked.connect(self.clearSettings)
        self.ui.resetCurrentSettings.clicked.connect(self.deleteCurrentSettings)
        self.ui.randomSettings.clicked.connect(self.drawRandomSettings)
        self.ui.rotorsList.itemClicked.connect(self.showRotorSettings)
        self.ui.saveLetterOrderButton.clicked.connect(self.setCurrentItemLetterOrder)
        self.ui.saveRotationButton.clicked.connect(self.setCurrentItemRotation)
        self.ui.loadTextButton.clicked.connect(self.readTextFromFile)
        self.ui.loadTextAndSettingsButton.clicked.connect(self.readTextAndSettingsFromFile)
        self.ui.saveTextAndSettingsButton.clicked.connect(self.saveTextAndSettingsToFile)
        self.ui.drawLetterOrder.clicked.connect(self.randomLetterOrder)
        self.ui.drawAdditionalRotation.clicked.connect(self.randomRotation)
        self.ui.randomEntranceSwaps.clicked.connect(self.drawEntranceSwaps)
        self.ui.randomReverseSwaps.clicked.connect(self.drawReverseSwaps)
        self.ui.randomCode.clicked.connect(self.drawCode)
        self.ui.randomOrder.clicked.connect(self.drawOrder)
        self.ui.clearText.clicked.connect(self.deleteText)
        self.current_machine = Enigma()

    def deleteText(self):
        """
        Czyści pole, w którym można wpisać tekst do zaszyfrowania.
        """
        self.ui.textEdit.setText("")

    def randomLetterOrder(self):
        """
        Ustawia losową kolejność liter w odpowiednim polu.
        """
        new_letter_order = Rotor.random_letter_order()
        self.ui.letterOrder.setText(new_letter_order)

    def randomRotation(self):
        """
        Ustawia losową literę w odpowiednim polu.
        """
        new_rotation = Rotor.random_rotation()
        self.ui.rotationEdit.setText(new_rotation)

    def drawCode(self):
        """
        Ustawia losowy kod w odpowiednim polu, jeśli maszyna ma już potencjalne ustawienia.
        """
        if self.current_machine.potential_settings:
            self.ui.textCode.setText(self.current_machine.potential_settings.connected_rotors().random_code())
        else:
            self.message(EnigmaSettingsError('Nie można wylosować kodu.'), 'Uwaga')

    def drawOrder(self):
        """
        Ustawia losową kolejność wirników (wszystkie wirnki będą użyte), jeśli maszyna ma już potencjalne ustawienia.
        """
        if self.current_machine.potential_settings:
            self.ui.textRotorOrder.setText(self.current_machine.potential_settings.connected_rotors().random_order())
        else:
            self.message(EnigmaSettingsError('Nie można wylosować kolejności.'), 'Uwaga')

    def setCurrentItemLetterOrder(self):
        """
        Zmienia kolejność liter w wybranym wirniku na taką jaka podana jest w polu do wpisywania kolejności liter.
        """
        try:
            if self.ui.rotorsList.currentItem():
                new_letter_order = self.ui.letterOrder.text()
                item = self.ui.rotorsList.currentItem()
                # print(item.index)
                self.current_machine.potential_settings.connected_rotors()(item.index).set_letter_order(new_letter_order)
                item.letter_order = new_letter_order
                self.showRotorSettings(item)
            else:
                self.message("Nie wybrano wirnika")
        except Exception as e:
            self.message(e)

    def setCurrentItemRotation(self):
        """
        Zmienia literę dla, której wybranym wirniku sąsiedni wirnik się obraca, na takąjaka podana jest w polu
         do wpisywania kolejności liter.
        """
        try:
            if self.ui.rotorsList.currentItem():
                item = self.ui.rotorsList.currentItem()
                new_rotation = self.ui.rotationEdit.text().upper()
                # print(item.index)
                self.current_machine.potential_settings.connected_rotors()(item.index).set_additional_rotation(new_rotation)
                item.additional_rotation = new_rotation
                self.showRotorSettings(item)
            else:
                self.message("Nie wybrano wirnika")
        except Exception as e:
            self.message(e)

    def readTextAndSettingsFromFile(self):
        """
        Wczytuje z pliku ustawienia maszyny i tekst. Jeśli zaznaczona jest odpowiednia opcja, to ustawienia
        maszyny automatycznie się zapiszą.
        """
        filename = QFileDialog.getOpenFileName(self, "Wczytaj ustawienia i tekst z pliku", "ustawienia/")
        path = filename[0]
        if path:
            try:
                self.current_machine.load_from_json(path)
                with open(path, "r") as file_handle:
                    self.ui.textEdit.setText(read_text_from_json(file_handle))
                self.clearSettings()
                self.fillBoxes()
                self.ui.textShow.setText("")
                if self.ui.autoSave.isChecked():
                    self.saveNewSettings()
                self.printSettings()
            except KeyError as e:
                self.message(f'Missing rotor key: {e}', "Nie można wczytać danych")
            except Exception as e:
                self.message(e, "Nie można wczytać danych")

    def saveTextAndSettingsToFile(self):
        """
        Pozwala zapisać aktualne ustawienia maszyny oraz zaszyfrowany/odszyfrowany tekst do pliku.
        Jeśli, maszyna nie jest skonfigurowana lub nie ma żadnego tekstu nie będzie można zapisać pliku.
        """
        if self.current_machine.settings and self.ui.textShow.toPlainText():
            filename = QFileDialog.getSaveFileName(self, "Zapisz ustawienia i zaszyfrowany tekst do pliku",
                                                   "ustawienia/new_settings.json", "*.json")
            path = filename[0]
            ext = splitext(path)[-1][1:]
            if path:
                if ext == "json":
                    with open(path, "w") as file:
                        try:
                            self.saveSettingsToFile(file, self.ui.textShow.toPlainText())
                        except Exception as e:
                            self.message(e)
                else:
                    self.message(PathExtensionError(ext), "Nie można zapisać ustawień i tekstu")
        else:
            self.message(DataError(), "Nie można zapisać ustawień i tekstu")

    def drawEntranceSwaps(self):
        """
        Ustawia losowe połączenia na łącznicy(ich ilość jest określona przez użytkownika) w odpowiednim polu.
        """
        self.ui.entranceSwapsText.setText(str_links(StaticRotor.random_keyboard_links(
            self.ui.entranceSwaps.value())).rstrip()
                                          )

    def drawReverseSwaps(self):
        """
        Ustawia losowe połączenia na wirniku odwracającym w odpowiednim polu.
        """
        self.ui.reverseSwapsText.setText(str_links(StaticRotor.random_keyboard_links(13)).rstrip())

    def encryptText(self):
        """
        Szyfruje/deszyfruje tekst podany w odpowiednim polu i wyświetla go.
        """
        if self.current_machine:
            try:
                # self.saveNewSettings()
                if self.current_machine.settings:

                    encrypted = self.current_machine.settings.encrypt_text(self.ui.textEdit.toPlainText())
                    self.ui.textShow.setText(encrypted)
                    self.printSettings()
                else:
                    self.message(EnigmaSettingsError())
            except Exception as e:
                self.message(e)

        else:
            self.message(EnigmaSettingsError())

    def drawRandomSettings(self):
        """
        Wypełnia wypełnia odpowiednie pola losowymi ustawieniami (zmienne to ilość wirników i ilość połączeń
         na łącznicy).
        """
        self.clearSettings()
        number_of_rotors = self.ui.rotorsNumber.value()
        number_of_entrance_links = self.ui.entranceSwaps.value()
        self.current_machine.set_potential_random_settings(number_of_rotors, number_of_entrance_links)
        self.fillBoxes()
        self.ui.textShow.setText("")

    def readTextFromFile(self):
        """
        Wczytuje tekst z pliku i wypełnia nim odpowiednie pole. Jeśli wybrany został plik .json tekst zostanie wczytany
        jeśli zawiera pole "text". Można wczytać też z pliku o innym foramcie.
        """
        filename = QFileDialog.getOpenFileName(self, "Wczytaj ustawienia i tekst z pliku", "ustawienia/")
        path = filename[0]
        ext = splitext(path)[-1][1:]
        try:
            if path:
                with open(path, "r") as file_handle:
                    if ext != "json":
                        self.ui.textEdit.setText(read_text_from_file(file_handle))
                    else:
                        self.ui.textEdit.setText(read_text_from_json(file_handle))
        except Exception as e:
            self.message(e, "Nie można wczytać tekstu")

    def openReadSettingsDialog(self):
        """
        Pozwala wczytać ustawienia z pliku .json. Jeśli dane w pliku są prawidłowe, zosatną wypełnione odpowiednie pola.
        """
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        if path:
            try:
                self.current_machine.load_from_json(path)
                self.clearSettings()
                self.fillBoxes()
                if self.ui.autoSave.isChecked():
                    self.saveNewSettings()
                self.printSettings()
            except KeyError as e:
                self.message(f'Missing rotor key: {e}', "Nie można wczytać ustawień")
            except Exception as e:
                self.message(e, "Nie można wczytać ustawień")

    def clearSettings(self):
        """
        Czyści pola, w których można wpisać ustawienia.
        """
        self.ui.entranceSwapsText.setText("")
        self.ui.reverseSwapsText.setText("")
        self.ui.rotorSettings.setText("")
        self.ui.letterOrder.setText("")
        self.ui.rotationEdit.setText("")
        for _ in range(self.ui.rotorsList.count()):
            self.ui.rotorsList.takeItem(0)
        self.ui.textRotorOrder.setText("")
        self.ui.textCode.setText("")

    def deleteCurrentSettings(self):
        """
        Usuwa aktualne ustawienia maszyny.
        """
        if self.current_machine:
            if self.current_machine.settings:
                self.current_machine.reset_settings()
                self.ui.textShow.setText("")
        self.printSettings()

    def openSaveSettingsDialog(self):
        """
        Pozwala zapisać aktualne ustawienia maszyny do pliku.
        """
        if self.current_machine.settings:
            filename = QFileDialog.getSaveFileName(self, "Zapisz ustawienia do pliku", "ustawienia/new_settings.json",
                                                   "*.json")
            path = filename[0]
            ext = splitext(path)[-1][1:]
            if path:
                if ext == "json":
                    with open(path, "w") as file:
                        try:
                            self.saveSettingsToFile(file)
                        except Exception as e:
                            self.message(e)
                else:
                    self.message(PathExtensionError(ext))
        else:
            self.message(EnigmaSettingsError("Maszyna nie jest skonfigurowana."), "Nie można zapisać ustawień.")

    def readSettings(self):
        """
        Jeśli dane wpisane w odpowiednich polach są prawidłowe, tworzy instancję klasy Settings.
        """
        number_of_rotors = self.ui.rotorsList.count()
        entrance_rotor = StaticRotor(self.ui.entranceSwapsText.text())
        reverse_rotor = ReverseRotor(self.ui.reverseSwapsText.text())
        order = self.ui.textRotorOrder.text()
        initial_code = self.ui.textCode.text()
        rotors = self.readRotors()
        connected_rotors = ConnectedRotors(number_of_rotors, rotors, order.split(), initial_code)
        settings = Settings(connected_rotors, entrance_rotor, reverse_rotor)
        return settings

    def saveNewSettings(self):
        """
        Jeśli dane wpisane w odpowiednich polach są prawidłowe, zapisuje je jako nowe ustawienia maszyny.
        """
        try:
            self.current_machine.potential_settings = self.readSettings()
            if self.current_machine.potential_settings:
                self.current_machine.set_settings()
                self.printSettings()
                self.ui.textShow.setText("")
        except Exception as e:
            self.message(e, "Nie można zapisać ustawień")

    def saveSettingsToFile(self, file_handle, text=None):
        """
        Pozwala zapisać aktualne ustawienia maszyny do pliku.
        """
        try:
            if file_handle:
                write_to_file(file_handle, self.current_machine.settings, text)
        except Exception as e:
            raise e

    def printSettings(self):
        """
        W odpowiednim polu wyświetla aktualne ustawienia maszyny.
        """
        if self.current_machine.settings:
            self.ui.textSettings.setText(str(self.current_machine))
        else:
            self.ui.textSettings.setText("Maszyna nie jest jeszcze skonfigurowana.")

    def fillBoxes(self):
        """
        Wypełnia pola, w których można zmieniać ustawienia, według danych zapisanych w potencjalnych ustawieniach.
        """
        if self.current_machine.potential_settings:
            self.ui.rotorsNumber.setValue(self.current_machine.potential_settings.connected_rotors().number_of_rotors())
            self.ui.entranceSwapsText.setText(str(self.current_machine.potential_settings.entrance_rotor()))
            self.ui.reverseSwapsText.setText(str(self.current_machine.potential_settings.reverse_rotor()))
            self.fillRotors()
            self.ui.textRotorOrder.setText(self.current_machine.potential_settings.order())
            self.ui.textCode.setText(self.current_machine.potential_settings.initial_code())

    def fillRotors(self):
        """
        Dodaję do listy wirników ich ustawienia.
        """
        # print(self.current_machine.potential_settings.order())
        for index in range(1, self.ui.rotorsNumber.value()+1):
            rotor_item = QListWidgetItem(f"Wirnik {index}")
            rotor = self.current_machine.potential_settings.connected_rotors()(str(index))
            rotor_item.index = str(index)
            rotor_item.letter_order = rotor.letter_order()
            rotor_item.additional_rotation = rotor.additional_rotation()
            self.ui.rotorsList.addItem(rotor_item)

    def showRotorSettings(self, item):
        """
        Po wybraniu wirnika wyświetla w odpwienim miejscu informacje o nim.
        """
        self.ui.rotorSettings.setText("")
        info = f"Wirnik {item.index}\n"
        info += f"Kolejność liter: {item.letter_order}\n"
        info += f"Dodatkowy obrót: {item.additional_rotation}"
        self.ui.rotorSettings.setText(info)

    def readRotors(self):
        """
        Czyta dane zapisane w liście wirników i tworzy słownik, którego wartościami są instancje klasy Rotor,
        a kluczami indeksy (int zamienione na str).
        """
        rotors = {}
        for i in range(self.ui.rotorsList.count()):
            # print(i)
            let = self.ui.rotorsList.item(i).letter_order
            # print(let)
            rot = self.ui.rotorsList.item(i).additional_rotation
            # print(rot)
            rotors[str(i+1)] = Rotor(let, rot)
        return rotors

    def message(self, error, msg="Uwaga"):
        """
        Wyświetla okno z informacją o błędzie, zawierające opis zdarzenia.
        """
        QMessageBox.warning(self, msg, str(error))


def guiMain(args):
    app = QApplication(args)
    window = EnigmaWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
