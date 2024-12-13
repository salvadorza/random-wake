import random
import webbrowser
from datetime import datetime
from customtkinter import *

# Creamos la ventana principal del despertador
raiz = CTk()
raiz.geometry("600x400")
raiz.title("Reloj Despertador")
set_appearance_mode("dark")

# Creamos una lista con las diferentes canciones que queremos que se puedan reproducir al sonar la alarma
canciones = [
    "https://www.youtube.com/watch?v=2oyhlad64-s",
    "https://www.youtube.com/watch?v=3KZyy8Oc1QA",
    "https://www.youtube.com/watch?v=RldFPCQGOwk"
]

# Establecemos las variables para almacenar la hora de la alarma
hora_alarma = None
minuto_alarma = None

# Función para poder actualizar la hora
def actualizar_hora():
    global hora_alarma, minuto_alarma

    # Obtenemos la hora actual
    hora_actual = datetime.now().strftime("%H:%M:%S")
    mostrar_hora.configure(text=hora_actual)

    # Vemos si la hora actual coincide con la alarma que hemos establecido
    if hora_alarma is not None and minuto_alarma is not None:
        hora_minuto_actual = datetime.now().strftime("%H:%M")
        hora_minuto_alarma = f"{hora_alarma}:{minuto_alarma:02d}"
        if hora_minuto_actual == hora_minuto_alarma:
            cancion = random.choice(canciones)  # Si coincide la hora, suena una cancion al azar
            webbrowser.open_new_tab(cancion)    # Abrimos el navegador para que se reproduzca
            alarma_label.configure(text="¡Alarma activada!", text_color="red")
            hora_alarma = None  # Tenemos que resetear la alarma para que no siga sonando continuamente

    # Le decimos que se repita la hora cada 1000ms que equivale a 1 segundo
    mostrar_hora.after(1000, actualizar_hora)

# Función para poder establecer la alarma
def establecer_alarma():
    global hora_alarma, minuto_alarma

    # Tenemos que obtener la hora y los minutos que ha introducido el usuario
    hora_alarma = opciones_hora.get().split(":")[0]
    minuto_alarma = int(float(opciones_minutos.get()))
    alarma_label.configure(text=f"Alarma establecida para las {hora_alarma}:{minuto_alarma:02d}", text_color="#5caf52")

# Creamos un label donde se va a mostrar la hora
mostrar_hora = CTkLabel(master=raiz, font=("Digital-7 Mono", 50), text_color="#5caf52")
mostrar_hora.place(relx=0.5, rely=0.15, relwidth=0.4, relheight=0.2, anchor="center")

# Texto para decirle al usuario que ponga una alarma
texto_alarma = CTkLabel(master=raiz, text="Establece una alarma", font=("Digital-7 Mono", 22), text_color="#5caf52")
texto_alarma.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.2, anchor="center")

# Usamos combobox para mostrar las horas
opciones_hora = CTkComboBox(
    master=raiz,
    values=[f"{h:02d}:00" for h in range(24)],
    button_color="#095600",
    button_hover_color="#5caf52",
    dropdown_hover_color="#095600",
    text_color="#5caf52",
    corner_radius=5,
    border_color="#5caf52"
)
opciones_hora.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.06, anchor="center")

# Para los minutos vamos a usar un slider
opciones_minutos = CTkSlider(master=raiz, from_=0, to=59, button_color="#5caf52", progress_color="#095600")
opciones_minutos.place(relx=0.7, rely=0.4, relwidth=0.3, relheight=0.06, anchor="center")

# Label para que se vea el valor del slider
label_minuto = CTkLabel(master=raiz, text="30", font=("Arial", 18), text_color="#5caf52")
label_minuto.place(relx=0.7, rely=0.48, anchor="center")

# Este label es para mostrar la hora a la que sea puesto la alarma y tambien mostrará por pantalla un texto cuando suene 
alarma_label = CTkLabel(master=raiz, text="", font=("Arial", 22,"bold"), text_color="#5caf52")
alarma_label.place(relx=0.5, rely=0.75, anchor="center")

def mostrar_valor_minutos(valor):
    label_minuto.configure(text=f"{int(valor):02d}")

opciones_minutos.configure(command=mostrar_valor_minutos)

# Este boton es para que cuando el usuario lo pulse, se establezca la alarma
boton_alarma = CTkButton(
    master=raiz,
    text="Establecer",
    corner_radius=3,
    fg_color="#095600",
    hover_color="#5caf52",
    command=establecer_alarma
)
boton_alarma.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.06, anchor="center")

# Llamamos a la funcion para que se vaya actualizando la hora
actualizar_hora()

raiz.mainloop()
