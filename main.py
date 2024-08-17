from flask import Flask,render_template,session,redirect,url_for,flash
from formularios.forms import Formulario
from metodo.main import informacionPokemon

app = Flask(__name__)

#Clave secreta para el formulario
app.config['SECRET_KEY'] = 'clavesecreta'


#Ruta donde se va a mostrar la informacion
@app.route('/informacion')
def informacion():
    try:
        nombre = session['nombre']
        datos = informacionPokemon(nombre)
        return render_template('informacion.html',name= datos)
    
    except:
        return redirect(url_for('mensaje'))


#Ruta Index: Se muesta el formulario
@app.route('/',methods=["GET","POST"])
def index():
    miFormulario = Formulario() #Hace una instancia hacia el formulario 
    #Se valida que el formulario se haya enviado. 
    if miFormulario.validate_on_submit():
        session['nombre'] = miFormulario.nombre.data #Guarda la informacion del campo

        return redirect(url_for('informacion')) #Redirecionando hacia la vista
    
    return render_template('index.html',formulario = miFormulario)#Si no envia la informacion se muestra el formulario de entrada.

#Ruta de mensaje de error
@app.route('/mensaje')
def mensaje():
    flash("Error ese pokemon no existe")
    return render_template('mensaje.html')

@app.errorhandler(404)
def paginaError(e):
    return render_template('error.html'),404





if __name__ == '__main__':
    app.run(debug=True)