from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import json
import random

class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        bouton_question = Button(text=Question, size_hint = (1, .2), pos_hint = {'center_x': .5, 'center_y': .9})
        self.add_widget(bouton_question)

        boutonA = Button(text=ReponseA, size_hint = (.5, .4), pos_hint = {'center_x': .25, 'center_y': .6}, on_press = self.button_pressed)
        self.add_widget(boutonA)

        boutonB = Button(text=ReponseB, size_hint = (.5, .4), pos_hint = {'center_x': .75, 'center_y': .6}, on_press = self.button_pressed)
        self.add_widget(boutonB)

        boutonC = Button(text=ReponseC, size_hint = (.5, .4), pos_hint = {'center_x': .25, 'center_y': .2}, on_press = self.button_pressed)
        self.add_widget(boutonC)

        boutonD = Button(text=ReponseD, size_hint = (.5, .4), pos_hint = {'center_x': .75, 'center_y': .2}, on_press = self.button_pressed)
        self.add_widget(boutonD)









    reponse_donnee = None
    def button_pressed(self, button):
        print(button.text)
        reponse_donnee = button.text
        popup_gagne = Popup(title='Gagné ! Distribue 2 gorgées', content=Button(text='Continuer'), size_hint=(.6, .6), pos_hint = {'center_x': .5, 'center_y': .4})
        if reponse_donnee == BonneReponse:
            self.add_widget(popup_gagne)

        popup_perdu = Popup(title='Perdu ! Bois 2 gorgées', content=Button(text='Continuer'), size_hint=(.6, .6), pos_hint= {'center_x': .5, 'center_y': .4})
        if reponse_donnee != BonneReponse:
            self.add_widget(popup_perdu)



class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

###Questions et réponses###

with open('questions.json', "r") as q:
    questions = json.load(q)
nombre_de_questions = 6
liste_questions = [i for i in range(1,nombre_de_questions + 1)]
print(liste_questions)
choix_question = random.randint(0,len(liste_questions))
question_choisie = str(liste_questions[choix_question])
del liste_questions[choix_question]
Question = questions[question_choisie]["texte"]
ReponseA = questions[question_choisie]["reponseA"]
ReponseB = questions[question_choisie]["reponseB"]
ReponseC = questions[question_choisie]["reponseC"]
ReponseD = questions[question_choisie]["reponseD"]
BonneReponse = questions[question_choisie]["bonne_reponse"]

if __name__ == '__main__':
    MainApp().run()