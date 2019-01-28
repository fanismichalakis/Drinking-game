from kivy.app import App
from kivy.app import *
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import json
from kivy.clock import Clock
from kivy.vector import Vector
import random

###############                               RELATIF AU QUIZZ                                                  #########

class Quiz(FloatLayout):
    def __init__(self, **kwargs):
        super(Quiz, self).__init__(**kwargs)

        with open('questions.json', "r") as q:
            questions = json.load(q)
        nombre_de_questions = 8
        liste_questions = [i for i in range(1, nombre_de_questions + 1)]
        print(liste_questions)
        choix_question = random.randint(0, len(liste_questions) - 1)
        question_choisie = str(liste_questions[choix_question])
        Question = questions[question_choisie]["texte"]
        ReponseA = questions[question_choisie]["reponseA"]
        ReponseB = questions[question_choisie]["reponseB"]
        ReponseC = questions[question_choisie]["reponseC"]
        ReponseD = questions[question_choisie]["reponseD"]
        self.BonneReponse = questions[question_choisie]["bonne_reponse"]

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

    popup = ObjectProperty()

    reponse_donnee = None

    def button_pressed(self, button):
        print(button.text)
        reponse_donnee = button.text
        bouton_continuer = Button(text='Continuer')
        popup_gagne = Popup(title='Gagné ! Distribue 2 gorgées', content=bouton_continuer, size_hint=(.6, .6),
                            pos_hint={'center_x': .5, 'center_y': .4}, auto_dismiss=True)
        bouton_continuer.bind(on_press=self.parent.quiz_init)
        if reponse_donnee == self.BonneReponse:
            self.add_widget(popup_gagne)
        bouton_continuer_perdu = Button(text='Continuer')
        bouton_continuer_perdu.bind(on_press=self.parent.quiz_init)
        popup_perdu = Popup(title='Perdu ! Bois 2 gorgées', content=bouton_continuer_perdu, size_hint=(.6, .6),
                                pos_hint={'center_x': .5, 'center_y': .4})
        if reponse_donnee != self.BonneReponse:
            self.add_widget(popup_perdu)


##########                              RELATIF AU MINI JEU                                                     ########


class PaddlePlayer(Widget):

    def end_game(self, ball):
        return self.collide_widget(ball)


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class Ball1(Widget):
    velocity_x1 = NumericProperty(0)
    velocity_y1 = NumericProperty(0)
    velocity1 = ReferenceListProperty(velocity_x1, velocity_y1)

    def move(self):
        self.pos = Vector(*self.velocity1) + self.pos


class Ball2(Widget):
    velocity_x2 = NumericProperty(0)
    velocity_y2 = NumericProperty(0)
    velocity2 = ReferenceListProperty(velocity_x2, velocity_y2)

    def move(self):
        self.pos = Vector(*self.velocity2) + self.pos


class MiniGame(Widget):
    ball = ObjectProperty(None)
    ball1 = ObjectProperty(None)
    ball2 = ObjectProperty(None)
    player = ObjectProperty(None)
    vel = [-2, random.choice([-2, -1, 0, 1, 2])]
    vel1 = [-2, random.choice([-2, -1, 0, 1, 2])]
    vel2 = [-2, random.choice([-2, -1, 0, 1, 2])]

    def serve_ball(self):
        self.ball.center = (self.width, self.height-random.randint(20, self.height-20))
        if -5 < self.vel[0] < 0:
            self.vel = [self.vel[0] * 1.2, random.uniform(-5, 5)]
        if -10 < self.vel[0] < -5:
            self.vel = [self.vel[0] * 1.03, random.uniform(-10, 10)]
        if -20 < self.vel[0] < -10:
            self.vel = [self.vel[0] * 1.03, random.uniform(-20, 20)]
        if -20 > self.vel[0]:
            self.vel = [self.vel[0], random.uniform(-25, 25)]
        self.ball.velocity = self.vel

    def serve_ball1(self):
        self.ball1.center = (self.width, self.height-random.randint(20, self.height-20))
        if -5 < self.vel1[0] < 0:
            self.vel1 = [self.vel1[0] * 1.2, random.uniform(-5, 5)]
        if -10 < self.vel1[0] < -5:
            self.vel1 = [self.vel1[0] * 1.03, random.uniform(-10, 10)]
        if -20 < self.vel1[0] < -10:
            self.vel1 = [self.vel1[0] * 1.03, random.uniform(-20, 20)]
        if -20 > self.vel1[0]:
            self.vel1 = [self.vel1[0], random.uniform(-25, 25)]
        self.ball1.velocity1 = self.vel1

    def serve_ball2(self):
        self.ball2.center = (self.width, self.height-random.randint(20, self.height-20))
        if -5 < self.vel2[0] < 0:
            self.vel2 = [self.vel2[0] * 1.2, random.uniform(-5, 5)]
        if -10 < self.vel2[0] < -5:
            self.vel2 = [self.vel2[0] * 1.03, random.uniform(-10, 10)]
        if -20 < self.vel2[0] < -10:
            self.vel2 = [self.vel2[0] * 1.03, random.uniform(-20, 20)]
        if -20 > self.vel2[0]:
            self.vel2 = [self.vel2[0], random.uniform(-25, 25)]
        self.ball2.velocity2 = self.vel2

    def update(self, dt):
        self.ball.move()
        self.ball1.move()
        self.ball2.move()

        if self.player.end_game(self.ball):
            pop_up = Popup(title='T es mauvais Jack, tu bois 3 gorgées')
            self.add_widget(pop_up)

        if self.player.end_game(self.ball1):
            pop_up = Popup(title='LEEEEEROOOOOOOOOOY JENKIINNNNSS, TU BOIS TOUT L ALCOOL DISPONIBLE')
            self.add_widget(pop_up)

        if self.player.end_game(self.ball2):
            pop_up = Popup(title='T es mauvais Jack, tu bois 4 gorgées')
            self.add_widget(pop_up)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        if (self.ball1.y < self.y) or (self.ball1.top > self.top):
            self.ball1.velocity_y1 *= -1

        if (self.ball2.y < self.y) or (self.ball2.top > self.top):
            self.ball2.velocity_y2 *= -1

        # balls went of to the left side an so their speed increase
        if self.ball.x < 0:
            self.serve_ball()

        if self.ball1.x < 0:
            self.serve_ball1()

        if self.ball2.x < 0:
            self.serve_ball2()

        # serve ball 1 and 2 according to the position of the ball
        if 0 < self.ball.x < self.width/3 and self.ball1.center[0] == self.width:
            self.serve_ball1()

        if self.width/3 < self.ball.x < self.width-self.width/3 and self.ball2.center[0] == self.width:
            self.serve_ball2()

    def on_touch_move(self, touch):
        if touch.x < self.width:
            self.player.center_y = touch.y
            self.player.center_x = touch.x


###############                                 RELATIF AU MENU                                             ############

class Menu(BoxLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        game_button = Button(text='I wanna play !', on_release=self.mini_game_init)
        quiz_button = Button(text='I wanna play the quiz!', on_release=self.quiz_init)
        self.add_widget(game_button)
        self.add_widget(quiz_button)

    def mini_game_init(self, obj):
        mini_game = MiniGame()
        self.clear_widgets()
        self.add_widget(mini_game)
        mini_game.serve_ball()
        Clock.schedule_interval(mini_game.update, 1.0 / 60.00)

    def quiz_init(self, obj):
        self.clear_widgets()
        self.quiz = quiz = Quiz()
        quiz.bind(size=self._update_rect, pos=self._update_rect)
        with quiz.canvas.before:
            Color(0, 1, 0, 1)
            self.rect = Rectangle(size=quiz.size, pos=quiz.pos)
        self.add_widget(quiz)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class GameApp(App):
    def build(self):
        return Menu()


if __name__ == '__main__':
    GameApp().run()
