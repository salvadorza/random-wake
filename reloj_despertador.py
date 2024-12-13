import random
import webbrowser
from datetime import datetime
from customtkinter import *

# Crear ventana principal
raiz = CTk()
raiz.geometry("600x400")
raiz.title("Reloj Despertador")
set_appearance_mode("dark")

hora_alarma = None
minuto_alarma = None

# Función para actualizar la hora
def actualizar_hora():
    global hora_alarma,minuto_alarma
    hora_actual = datetime.now().strftime("%H:%M:%S")  # Formato de 24 horas
    mostrar_hora.configure(text=hora_actual)  # Actualizar el texto de la etiqueta
    if hora_alarma is not None and minuto_alarma is not None:
        hora_minuto_actual = datetime.now().strftime("%H:%M")
        hora_minuto_alarma = f"{hora_alarma}:{minuto_alarma:02d}"
        if hora_minuto_actual == hora_minuto_alarma:
            webbrowser.open("https://www.youtube.com/watch?v=2oyhlad64-s")
            hora_alarma = None  # Resetear la alarma para que no suene continuamente
    mostrar_hora.after(1000, actualizar_hora)  # Repetir cada 1000 ms (1 segundo)


def establecer_alarma():
    global hora_alarma,minuto_alarma
    hora_alarma = opciones_hora.get().split(":")[0]
    minuto_alarma = int(float(opciones_minutos.get()))
    alarma_label.configure(text=f"Alarma establecida para las {hora_alarma}:{minuto_alarma:02d}")

# Crear widgets
mostrar_hora = CTkLabel(master=raiz, font=("Digital-7 Mono", 50), text_color="#5caf52")
mostrar_hora.place(relx=0.5, rely=0.15, relwidth=0.4, relheight=0.2, anchor="center")

texto_alarma = CTkLabel(master=raiz, text="Establece una alarma", font=("Digital-7 Mono", 28), text_color="#5caf52")
texto_alarma.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2, anchor="center")

# ComboBox para horas
opciones_hora = CTkComboBox(master=raiz, values=[f"{h:02d}:00" for h in range(24)],button_color="#095600",button_hover_color="#5caf52",
                            dropdown_hover_color="#095600",text_color="#5caf52",corner_radius=5,border_color="#5caf52")
opciones_hora.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.06, anchor="center")

# ComboBox para minutos agrupados en intervalos de 5
opciones_minutos = CTkSlider(master=raiz, from_=0,to=59,button_color="#5caf52",progress_color="#095600")
opciones_minutos.place(relx=0.7, rely=0.4, relwidth=0.3, relheight=0.06, anchor="center")

label_minuto = CTkLabel(master=raiz, text="30", font=("Arial", 18), text_color="#5caf52")
label_minuto.place(relx=0.7, rely=0.48, anchor="center")

boton_alarma = CTkButton(master=raiz,text="Establecer",corner_radius=3,fg_color="#095600",hover_color="#5caf52",command=establecer_alarma)
boton_alarma.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.06, anchor="center")

alarma_label = CTkLabel(master=raiz, text="", font=("Arial", 22,"bold"), text_color="#5caf52")
alarma_label.place(relx=0.5, rely=0.75, anchor="center")

def mostrar_valor_minutos(valor):
    label_minuto.configure(text=f"{int(valor):02d}")

opciones_minutos.configure(command=mostrar_valor_minutos)    


# Iniciar la actualización de la hora
actualizar_hora()

raiz.mainloop()
