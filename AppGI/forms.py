from django import forms

class Usuarios_formulario (forms.Form):

    usuario = forms.CharField(max_length=15)
    email = forms.EmailField()
    uids = forms.IntegerField()
    server = forms.CharField(max_length=10)


class e_adventure_formulario (forms.Form):

    pj_nombre = forms.CharField(max_length=15)
    pj_elemento = forms.CharField(max_length=10)
    pj_lv = forms.IntegerField()


class e_abiss_formulario (forms.Form):

    pj_nombre = forms.CharField(max_length=15)
    pj_elemento = forms.CharField(max_length=10)
    pj_lv = forms.IntegerField()
    fecha_abismo = forms.DateField()
    paso = forms.BooleanField()

