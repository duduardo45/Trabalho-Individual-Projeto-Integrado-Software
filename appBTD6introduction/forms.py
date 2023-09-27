from django.forms import ModelForm,Textarea

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
