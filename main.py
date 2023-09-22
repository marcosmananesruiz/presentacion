import tkinter as tk
from tkinter import ttk

presentation = tk.Tk()
presentation.title("Presentacion AW - Marcos Mañanes Ruiz")


tabControl = ttk.Notebook(presentation)

tabPersonal = ttk.Frame(tabControl)
tabHobbies = ttk.Frame(tabControl)
tabGustos = ttk.Frame(tabControl)
tabWeb = ttk.Frame(tabControl)

tabControl.add(tabPersonal, text="Datos Personales")
tabControl.add(tabGustos, text="Mis Gustos")
tabControl.add(tabHobbies, text="Mis Hobbies")
tabControl.add(tabWeb, text="Aplicacion Web que uso")
tabControl.pack(expand=True, fill="y")

#PESTAÑA PERSONAL

frmIntro = ttk.LabelFrame(tabPersonal, text="¿Quien Soy?")
frmIntro.grid(column=0,row=0,padx=30)
txtNombre = ttk.Label(frmIntro, text="Nombre: Marcos")
txtNombre.grid(column=0,row=0,padx=5)
txtApellidos = ttk.Label(frmIntro, text="Apellidos: Mañanes Ruiz")
txtApellidos.grid(column=0,row=1,padx=5)
txtEdad = ttk.Label(frmIntro, text="Edad: 18 Años (13-07-2005)")
txtEdad.grid(column=0,row=2,padx=5)

frmAbout = ttk.LabelFrame(tabPersonal, text="¿Como Soy?")
frmAbout.grid(column=1,row=0, padx=60, pady=20)
txtAbout1 = ttk.Label(frmAbout, text="Simpatico")
txtAbout1.grid(column=0,row=0,padx=5)
txtAbout2 = ttk.Label(frmAbout, text="Introvertido")
txtAbout2.grid(column=0,row=1)
txtAbout3 = ttk.Label(frmAbout, text="Con Determinacion")
txtAbout3.grid(column=0,row=2)
txtAbout4 = ttk.Label(frmAbout, text="Me adapto facil al entorno")
txtAbout4.grid(column=0, row=3)

frmActiv = ttk.LabelFrame(tabPersonal, text="¿Cosas que no dejaria de hacer?")
frmActiv.grid(column=2,row=0,padx=90,pady=20)
txtAct1 = ttk.Label(frmActiv, text="Jugar mis juegos favoritos\nAunque llege un momento que tenga poro tiempo para ello,\nsiempre intentare sacar esos ratos para\ndesconectar del mundo real y perderme en mis aventuras")
txtAct1.grid(column=0,row=0,padx=5,pady=5)
txtAct2 = ttk.Label(frmActiv, text="Series y Peliculas:\nAunque no vea apenas series ni peliculas ultimamente,\nsiempre me encanta ponerme una serie cada cierto tiempo, sea con mi familia o con mis amigos,\nmeternos todos en la trama y disfrutarla")
txtAct2.grid(column=0,row=1,padx=5,pady=5)
txtAct3 = ttk.Label(frmActiv, text="Caminatas:\nDesconectar completamente de la tecnologia y andar con amigos hasta donde el cuerpo nos aguante.\nNunca me negaria a esas conversacion de varias horas mientras exploramos alrededor nuestra.")
txtAct3.grid(column=0,row=2,padx=5,pady=5)

#PESTAÑA GUSTOS

frmGustos = ttk.LabelFrame(tabGustos, text="¿Que me gusta a mi?")
frmGustos.grid(column=0,row=0,padx=5,pady=5)

####SUBPESTAÑA ME GUSTA:

frmLike = ttk.LabelFrame(frmGustos,text="ME GUSTAN:")
frmLike.grid(column=0,row=0,padx=5, pady=5)


def showGatos(): selectedLike.set("Me encantan la mayoría de animales, pero en especial los Gatos,\ndesde que tengo a mi gata Lía descubrí la pasión que tengo por los felinos.\nUn gato ronroneando en la tripa mientras haces cualquier cosa es\nuna sensación única!")
def showMusic(): selectedLike.set("La música forma parte en la vida de todos nosotros.\nYo escucho prácticamente de todo, tengo mis generos mas y menos preferidos,\npero cuando tengo que trabajar en algo o quiero concentrarme siempre recurro\na música tranquila como LoFi o alguna cancion chula de Rock que me guste\nen el momento")
def showAstro(): selectedLike.set("La astronomía y todo lo relacionado con el espacio es algo que me parece asombroso\ny terrorífico al mismo tiempo. Siempre que he ido a ver una lluvia de estrellas\no he ido a algún planetario siempre tengola misma sensacion en el cuerpo de: 'WOW'.\nDudo mucho que incluso mi generación sea capaz tener la Luna como sitio turístico,\npero a mi ya con poder ver cosas como los cometas o las lluvias de estrellas\nme basta y me sirve para adorarlo")

optGatos = ttk.Radiobutton(frmLike, text="Gatos", command=showGatos, value=1)
optGatos.grid(column=0,row=0,padx=5,pady=5)
optMusic = ttk.Radiobutton(frmLike, text="Música", command=showMusic, value=2)
optMusic.grid(column=0,row=1,padx=5,pady=5)
optAstronomia = ttk.Radiobutton(frmLike, text="Astronomía", command=showAstro, value=3)
optAstronomia.grid(column=0,row=2,padx=5,pady=5)


selectedLike = tk.StringVar()
selectedLike.set("Clica los botones para saber más!")

txtLiked = ttk.Label(frmLike, textvariable=selectedLike)
txtLiked.grid(column=0,row=3, padx=5,pady=10)

####SUBPESTAÑA NO ME GUSTA

frmDislike = ttk.LabelFrame(frmGustos, text="NO ME GUSTAN:")
frmDislike.grid(column=1,row=0,padx=5,pady=5)

def showArañas(): selectedDislike.set("No hay bicho que aborrezca más que los arácnidos.\nUna fobia heredada de mi madre que con solo saber que\nhay una arañita en la misma habitación que yo me pone\nincómodo y con escalofríos, y si ya aparece al lado mía ni te cuento...")
def showMar(): selectedDislike.set("De pequeño tuve un problemita en una playa que fue algo traumante. Desde aquello todo lo que es\nadentrarme a mar adentro(ya sea en barco, lanchas o más...) me encoge el pecho.\nCon el tiempo lo he ido superando, pero el agobio aún no me lo quita nadie")
def showMT(): selectedDislike.set("Conozco gente que le encanta el ambiente nublado y con lluvias, pero a mí no me gusta nada.\nSiempre me ha parecido demasiado deprimente, todo muy apagado.\nAdemás de que si llueve nadie quiere salir a pasear por la zona. Nunca me he quejado\nni me quejaré realmente de ello por todo el tema de las sequías en Madrid. Se que viene muy bien que\nllueva, pero si tengo que elegir prefiero un ambiente más soleado con flores.")

optArañas = ttk.Radiobutton(frmDislike, text="Arañas", command=showArañas, value=4)
optArañas.grid(column=0,row=0,padx=5,pady=5)
optMar = ttk.Radiobutton(frmDislike, text="El Mar", command=showMar, value=5)
optMar.grid(column=0,row=1,padx=5,pady=5)
optMalTiempo = ttk.Radiobutton(frmDislike, text="El mal tiempo", command=showMT, value=6)
optMalTiempo.grid(column=0,row=2,padx=5,pady=5)

selectedDislike = tk.StringVar()
selectedDislike.set("Clica los botones para saber más!")

txtDisliked = ttk.Label(frmDislike, textvariable=selectedDislike)
txtDisliked.grid(column=0,row=3, padx=5,pady=10)


#PESTAÑA HOBBIES

selectedInfo = tk.StringVar()
selectedInfo.set("Clica en los botones para conocer mis hobbies!")

txtAllAbout = ttk.Label(tabHobbies, textvariable=selectedInfo)
txtAllAbout.grid(column=1,row=0, padx=5)

def setGameInfo():
    selectedInfo.set("Cualquier juego con una historia que\nsea capaz de disfrutar me vale, pero tampooco me niego a jugar juegos\ncomo shooters o party games con mis amigos.")

def setCodingInfo():
    selectedInfo.set("Llevo años siendo fan de este mundillo, la programación es algo que a dia de hoy me divierte bastante.\nEl tener una idea y pelear con toda la lógica del codigo se me hace entretenido,\nme gusta verlo como si fuera una Puzle a resolver\nSin embargo, soy plenamente consciente de que lo que se no me sirve ni para trabajar de ello\nni para hacer alguna idea loca que se me ocurra en el futuro, por eso quise hacer\neste curso, para asentar unas bases y luego ir de cabeza a DAM.\nA dia de hoy he tenido experiencia con lenguajes como Java, HTML, C#, Python(aqui por ejemplo xd) y VBA,\nexperiencias básicas pero que me sirven para ir tomando práctica")

def setWalkInfo():
    selectedInfo.set("Los otros 2 hobbies dan a entender que soy alguien que se pasa todo el día\nen el PC(que es verdad), pero a pesar de ello, raro será el día que me niegue a salir con colegas,\nmás cuando sea para ir a explorar.\nNuestra ciudad la tenemos bastante conocida así que ir a cualquier otro sitio a caminar y conocer lugares me encanta.\nLos otros hobbies he llegado a juntarlos programando cosas en algún juego, pero este es una desconexión\nde ambos que en algun momento de estrés de que algo no funcione viene de perlas.")

frmSelect = ttk.LabelFrame(tabHobbies, text="Mis diferentes hobbies")
frmSelect.grid(column=0, row=0, padx=20,pady=10)
btnJuegos = ttk.Button(frmSelect, text="Juegos🎮", command=setGameInfo)
btnJuegos.grid(column=0,row=0,padx=50,pady=10)
btnCoding = ttk.Button(frmSelect, text="Coding🧑‍💻", command=setCodingInfo)
btnCoding.grid(column=0,row=1,padx=50,pady=10)
btnWalk = ttk.Button(frmSelect, text="Paseos🚶", command=setWalkInfo)
btnWalk.grid(column=0, row=2, padx=50, pady=10)

#PESTAÑA APLICACION WEB

frmAppWeb = ttk.LabelFrame(tabWeb, text="")
frmAppWeb.grid(column=0,row=0,padx=20,pady=10)

txtTitulo = ttk.Label(frmAppWeb, text="¿Aplicacion Web que use diariamente?")
txtTitulo.grid(column=0,row=0)
txtTitulo2 = ttk.Label(frmAppWeb, text="YOUTUBE", font=100, background="#FF0000", foreground="#FFFFFF")
txtTitulo2.grid(column=0,row=1, pady=50)
txtInfoWeb = ttk.Label(frmAppWeb, text="YouTube es una aplicacion web diseñada con lenguajes como HTML implementando css, JavaScript y herramientas de Python\nEsta aplicacion yo la uso mucho tanto pot ocio tanto por aprendizaje.\nCon YouTube he aprendido multiples cosas como algunos lenguajes de Programacion o detalles curiosos de canales sobre Ciencia,\npero tambien me gusta ver videos para reirme o mantenerme entretenido durante alguna tarea\ntediosa.")
txtInfoWeb.grid(column=1,row=0,padx=20)

txtLink = ttk.Label(frmAppWeb, text="https://creativewhisper.es/lenguaje/con-que-lenguaje-de-programacion-se-hizo-youtube/")
presentation.mainloop()
