from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired #Validar los campos que no esten vacios


class Formulario(FlaskForm):
    '''nombre = StringField(
                        validators = [DataRequired()],
                        render_kw = {"placeholder":"Introduce el nombre de un pokemon",
                                    "class":"input_text"})'''
    nombre = StringField(
                        validators = [DataRequired()],
                        render_kw = {"class":"input_text"})
                         
    enviar = SubmitField("Enviar",
                         render_kw={"class": "button"})

