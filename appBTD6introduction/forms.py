from django.forms import ModelForm,Textarea
#from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User

from .models import Generos,Historia

class GeneroForm(ModelForm):
  class Meta:
    model = Generos
    fields = "__all__"
    widgets = {
            "dentro_de_BTD6": Textarea(attrs={"cols": 60, "rows": 10}),
        }

class HistoriaForm(ModelForm):
  class Meta:
    model = Historia
    fields = ["autor","titulo"]
    labels = {
      "autor":"Seu nome",
      "titulo":"Conte sua história que aconteceu em BTD6",
    }
    widgets = {
      "titulo":Textarea(attrs={"cols": 80, "rows": 20})
    }


class UserForm(ModelForm):
  class Meta:
    model = User
    fields = [
      "username",
      "first_name",
      "last_name",
      "email"
    ]
    labels = {
      "username":"Nome de Usuário",
      "first_name":"Primeiro Nome",
      "last_name":"Sobrenome",
      "email":"Seu email",
    }