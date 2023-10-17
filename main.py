from kivy.app import App

from kivy.uix.boxlayout import (BoxLayout)


from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder

Builder.load_file("Quiz-Page.kv")

users = ["dog21","YellowisMellow","Bowser35","TikiTorch10"]
passwords = {"dog21":"Dallas76","YellowisMellow":"George98","Bowser35":"Apple124","TikiTorch10":"AXBYndRgyY5"}

class QuizPageApp(App):
    def build(self):
        return LoginManager()



class LoginManager(ScreenManager):

   pass




class LoginPage(Screen):
    def check_user(self,username,password):
        if username in users and passwords[username] == password:
           self.manager.current = "welcome"
        else:
           self.ids.blank.text = "No User Found or Password does not match"
    def new_account(self):
        self.manager.current = "new"

def isnumeric(string):
    if "1" in string or "1" in string or "2" in string or "3" in string or "4" in string or "5" in string or "6" in string or "7" in string or "8" in string or "9" in string:
       return True
def isupper(string):
    if "A" in string or "B" in string or "C" in string or "D" in string or "E" in string or "F" in string or "G" in string or "H" in string or "I" in string or "J" in string or "K" in string or "L" in string or "M" in string or "N" in string or "O" in string or "P" in string or "Q" in string or "R" in string or "S" in string or "T" in string or "U" in string or "V" in string or "W" in string or "X" in string or "Y" in string or "Z" in string:
        return True
def islower(string):
    if "a" in string or "b" in string or "c" in string or "d" in string or "e" in string or "f" in string or "g" in string or "h" in string or "i" in string or "j" in string or "k" in string or "l" in string or "m" in string or "n" in string or "o" in string or "p" in string or "q" in string or "r" in string or "s" in string or "t" in string or "u" in string or "v" in string or "w" in string or "x" in string or "y" in string or "z" in string:
        return True

class NewUser(Screen):
    def set_user(self, new_username, new_password):
        users.append(new_username)
        if isupper(new_password) == True and islower(new_password) == True and isnumeric(new_password) == True and len(new_password)>=8:
           passwords[new_username] = new_password
           self.manager.current= "login"

class WelcomeScreen(Screen):
    pass



if __name__ == "__main__":

   QuizPageApp().run()