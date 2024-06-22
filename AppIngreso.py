                                        #############################
                                        ## Importacion de las lib. ##
                                        #############################

import requests
import os
import customtkinter
from customtkinter import *
from tkinter import *
from tkinter import messagebox
from reportlab.pdfgen import canvas
from email.message import EmailMessage
import ssl
import smtplib 
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



                                        #################################
                                        ## Algunas configs del tkinter ##    
                                        #################################
                                        

app = customtkinter.CTk() # Crea la aplicaion de tkinter
app.title("Ingreso Pasajeros - Bosque Sur")  # Titulo de la Ventana
app.geometry("1366x768")  # Tamaño de la ventana
app.resizable(False, False) # Activar o desactivar el resizing



                                        ###############################        
                                        ## Fuentes a usar el el code ##
                                        ###############################
                                        
font1 = ("Arial", 16, "bold") ### Fuente numero 1 para utilizar al momento de escribir los datos
font2 = ("Arial", 12, "bold") ### Fuente numero 2 para utilizar al momento de escribir los datos
font3 = ("Arial", 10, "bold") ### Fuente numero 3 para utilizar al momento de escribir las descripciones


                                        #################
                                        ## RutaDestino ##
                                        #################
                                        
### E S T A B L E C E R   L A   R U T A   D E   D E S T I N O    D E   L O S   A R C H I V O S ###
# ruta de ejemplo #

ruta_destino = "C:/Users/Lenovo/Desktop/ArchivosPDF"                                   


           
                                        ###########################
                                        ## FUNCION DE ENVIAR SMS ##
                                        ###########################


def EnviarSMS():
    DocumentoDeIdentidad = str(identification_entry.get())
    CorreoElectronico = str(CorreoElectronico_entry.get())
    PlacaPatente = str(PlacaPatente_entry.get())
    NumeroPasajeros = str(NumeroPasajeros_entry.get())
    Nacionalidad = str(nacionalidad_entry.get())
    Direccion = str(direccion_entry.get())
    Ciudad = str(ciudad_entry.get())
    FechaDeIngreso = str(FechaIngreso_entry.get())
    FechaDeSalida = str(FechaSalida_entry.get())
    ControlValue = str(control.get())
    NombreCompleto = name_entry.get()
    Telefono = telefono_entry.get()
    NumeroCabana = Cabana_entry.get()
    apiSecret = "ApiSecretdelsmschef" --> lo puedes hacer importando os --> os.getenv("APISECRET")
    deviceId = "ApiSecretdedeviceID" --> lo puedes hacer importando os --> os.getenv("DEVICEID")
    
    
    PhoneReceiver = "telefono de quien recibe"
    
    if NombreCompleto == "" or DocumentoDeIdentidad == "" or CorreoElectronico == "" or PlacaPatente == "" or NumeroCabana == "" or NumeroPasajeros =="" or Nacionalidad == "" or Direccion == "" or Ciudad == "" or Telefono == "" or FechaDeIngreso == "" or FechaDeSalida == "" or ControlValue == "0":
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
    else:   
    
        message = # Este es el texto que se enviará HACIA al dispositivo

        message = {
        "secret": apiSecret,
        "mode": "devices",
        "device": deviceId,
        "sim": 1,
        "priority": 1,
        "phone": PhoneReceiver,
        "message": message
     }


      #Este es el encargado de que se envíe el mensaje al dispositivo
        r = requests.post(url = "https://www.cloud.smschef.com/api/send/sms", params = message)
  
        # ver el estado del envio
        result = r.json()

        print(result)




                                        ##################################################
                                        ## ENVIAR NUMERO DE TELEFONO POR SMS A PASAJERO ##
                                        ##################################################


        # Las credenciales de envio se mantienen en base a los valores de las mismas variables 
        # Anteriormente mencionadas...
        # Este es el numero de telefono HACIA el que se enviará el mensaje 
        PhoneReceiver = "+56" + Telefono

        # Este es el texto que se enviará HACIA al dispositivo
        message = "Hola! " + NombreCompleto + "\nEl número al que debes llamar \npara abrir el portón \nes el siguiente: "numero de telefono"  \n\nEquipo de Cabañas Bosque Sur"

        message = {
        "secret": apiSecret,
        "mode": "devices",
        "device": deviceId,
        "sim": 1,
        "priority": 1,
        "phone": PhoneReceiver,
        "message": message
        }


        #Este es el encargado de que se envíe el mensaje al dispositivo
        r = requests.post(url = "https://www.cloud.smschef.com/api/send/sms", params = message)
  
        # Ver el estado del envio
        result = r.json()

        print(result)
    
        messagebox.showinfo("Operacion Exitosa", "Se ha registrado en el porton y enviado el SMS")

           
               
                                        ###############################
                                        ## FUNCION CHECKEAR INTERNET ##
                                        ###############################
def check_internet_connection():
    

    try:
        # Intentar conectarse a google por su dirección IP
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False
                                        
                                    

                                        ########################
                                        ## FUNCION EnviarMail ##
                                        ########################
def EnviarMail():
    
    
    NombreCompleto = str(name_entry.get())
    DocumentoDeIdentidad = str(identification_entry.get())
    CorreoElectronico = str(CorreoElectronico_entry.get())
    PlacaPatente = str(PlacaPatente_entry.get())
    NumeroCabana = str(Cabana_entry.get())
    NumeroPasajeros = str(NumeroPasajeros_entry.get())
    Nacionalidad = str(nacionalidad_entry.get())
    Direccion = str(direccion_entry.get())
    Ciudad = str(ciudad_entry.get())
    Telefono = str(telefono_entry.get())
    FechaDeIngreso = str(FechaIngreso_entry.get())
    FechaDeSalida = str(FechaSalida_entry.get())
    ControlValue = str(control.get())
    
    email_sender = "example@gmail.com"
    password = "xxxx xxxx xxxx xxxx" #??? ---> api de google para enviar correos
    email_reciever = CorreoElectronico #--> Direccion a la que se quiere enviar el correo
    subject = "Hola! " + NombreCompleto 
    
    #Mamotrero --> #
    body = "Hemos registrado los siguientes datos de ingreso :" + "\nNombre: " + NombreCompleto + "\nDocumento de Identidad: " + DocumentoDeIdentidad + "\nCorreo Electronico: " + CorreoElectronico + "\nPlaca de Patente: " + PlacaPatente + "\nNumero de Cabana: " + NumeroCabana + "\nNumero de Pasajeros: " + NumeroPasajeros + "\nNacionalidad: " + Nacionalidad + "\nDireccion: " + Direccion + "\nCiudad: " + Ciudad + "\nTelefono: " + Telefono + "\nFecha de Ingreso: "+ FechaDeIngreso + "\nFecha de Salida: "+ FechaDeSalida +"\n\n\n[HORARIOS]"+"\nEl horario de ingreso es a partir de las 15:00 hrs."+ "\nLa salida debe realizarse antes de las 11:00 am."+ "\n\n[ASEO DIARIO]"+"\nIncluimos servicio de aseo diario de 11:00 a 15:00 hrs"+"\nsiempre que las cabañas estén desocupadas"+ "\n\n[PROHIBICIÓN DE FUMAR DENTRO DE LAS CABAÑAS]"+ "\nSolicitamos no fumar en el interior de las cabañas."+"\nContamos con detectores de humo que emiten un fuerte sonido" + "\nlo cual puede resultar molesto para usted y los demás pasajeros." + "\n\n[PROHIBICIÓN DE RUIDOS MOLESTOS]" + "\nSomos cabañas de descanso y siempre buscamos mantener la tranquilidad." + "\nEvite música fuerte y gritos." + "\n\n[CALEFACCIÓN]" + "\nTodas las cabañas cuentan con calefacción de aire acondicionado."+ "\nLos departamentos tipo estudio disponen de calefacción eléctrica." + "\n\n[AL MOMENTO DEL CHECK OUT]" + "\nEl día de su salida, le solicitamos dejar las llaves en recepción." + "\n\n[COMUNICACION]" + "\nEs importante mantener una buena comunicación." + "\nEstamos siempre disponibles a través del número de celular y/o WhatsApp" + "\n+56 9 9811 5213, el cual se encuentra en el llavero y tazones." + "\n\n\nEquipo de Cabañas Bosque Sur"


    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciever
    em["Subject"] = subject
    em.set_content(body)

    context =ssl.create_default_context()

    if not check_internet_connection():
        messagebox.showerror("Error", "No se ha podido conectar con el servidor de internet")
    elif NombreCompleto == "" or DocumentoDeIdentidad == "" or CorreoElectronico == "" or PlacaPatente == "" or NumeroCabana == "" or NumeroPasajeros == "" or Nacionalidad == "" or Direccion == "" or Ciudad == "" or Telefono == "" or FechaDeIngreso == "" or FechaDeSalida == "" or ControlValue == "0":
        print("No se ha ingresado todos los campos")  
    else:    
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())

        print("Se ha enviado el correo")

                                        ####################
                                        ## FUNCION SUBMIT ##
                                        ####################
def submit():
    
    # Variables Tema Del Pdf #
    NombreCompleto = str(name_entry.get())
    DocumentoDeIdentidad = str(identification_entry.get())
    CorreoElectronico = str(CorreoElectronico_entry.get())
    PlacaPatente = str(PlacaPatente_entry.get())
    NumeroCabana = str(Cabana_entry.get())
    NumeroPasajeros = str(NumeroPasajeros_entry.get())
    Nacionalidad = str(nacionalidad_entry.get())
    Direccion = str(direccion_entry.get())
    Ciudad = str(ciudad_entry.get())
    Telefono = str(telefono_entry.get())
    FechaDeIngreso = str(FechaIngreso_entry.get())
    FechaDeSalida = str(FechaSalida_entry.get())
    ControlValue = str(control.get())
    
    
    #Ojo con esto, no se está desplegando el messagebox#
    if NombreCompleto == "" or DocumentoDeIdentidad == "" or CorreoElectronico == "" or PlacaPatente == "" or NumeroCabana == "" or NumeroPasajeros =="" or Nacionalidad == "" or Direccion == "" or Ciudad == "" or Telefono == "" or FechaDeIngreso == "" or FechaDeSalida == "" or ControlValue == "0":
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
    else:
        
        #Encargado de generar el PDF --->
        pdf_file = os.path.join(ruta_destino,"C-" + NumeroCabana + "-" + NombreCompleto + ".pdf") 
        c = canvas.Canvas(pdf_file)
        c.setFont("Helvetica", 12)
        
        c.drawString(100, 800, "Ingreso Pasajeros")
        c.drawString(100, 780, "Nombre: " + NombreCompleto)
        c.drawString(100, 760, "Identificación: " + DocumentoDeIdentidad)
        c.drawString(100, 740, "Correo: " + CorreoElectronico)
        c.drawString(100, 720, "Placa Patente: " + PlacaPatente)    
        c.drawString(100, 700, "Cabana: " + NumeroCabana)
        c.drawString(100, 680, "Pasajeros: " + NumeroPasajeros)
        c.drawString(100, 660, "Nacionalidad: " + Nacionalidad)
        c.drawString(100, 640, "Dirección: " + Direccion)
        c.drawString(100, 620, "Ciudad: " + Ciudad)
        c.drawString(100, 600, "Telefono: " + Telefono)
        c.drawString(100, 580, "Fecha de Ingreso: " + str(FechaDeIngreso))
        c.drawString(100, 560, "Fecha de Salida: " + str(FechaDeSalida))
        c.drawString(100, 540, " ------ Cabañas Bosque Sur ------ ")

        c.save()
        messagebox.showinfo("Operacion Exitosa", "Se ha generado el pdf y enviado el correo correctamente")
        
        
        
                                        ###################
                                        ## Boton Ingreso ##
                                        ###################
def BotonIngreso():
    
    return [submit(), EnviarMail()]
        
        
                                        ###################
                                        ## FUNCION CLEAR ##
                                        ###################
def clear():
    name_entry.delete(0, END)
    identification_entry.delete(0, END)
    CorreoElectronico_entry.delete(0, END)
    PlacaPatente_entry.delete(0, END)
    Cabana_entry.delete(0, END)
    NumeroPasajeros_entry.delete(0, END)  
    nacionalidad_entry.delete(0, END)
    direccion_entry.delete(0, END)
    ciudad_entry.delete(0, END)
    telefono_entry.delete(0, END)
    FechaIngreso_entry.delete(0, END)
    FechaSalida_entry.delete(0, END)
    control.set(0)

### Titulo ###

title_label = customtkinter.CTkLabel(app, font=font1, text="Ingreso Pasajeros - Cabañas BosqueSur", text_color="black", bg_color="#ebebeb")
title_label.place(x=30, y=30)

                                        #########################
                                        ## Lado Izquierdo izq. ##
                                        #########################


### NombreCompleto ###
name_label = customtkinter.CTkLabel(app, font=font2, text="Nombre completo / Full name", text_color="black", bg_color="#ebebeb" )
name_label.place(x=30, y=80)

name_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius= 16, width = 250)
name_entry.place(x=30, y=120)

### DocumentoDeIdentidad ###
identification_label = customtkinter.CTkLabel(app, font=font2, text="Documento de Identidad / Passport Number", text_color="black", bg_color="#ebebeb")
identification_label.place(x=30, y=160)

identification_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius= 16, width = 250)
identification_entry.place(x=30, y=200)


## CorreoElectronico ###
CorreoElectronico_label = customtkinter.CTkLabel(app, font=font2, text="Correo Electronico / email", text_color="black", bg_color="#ebebeb" )
CorreoElectronico_label.place(x=30, y=240)

CorreoElectronico_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius= 16, width = 250)
CorreoElectronico_entry.place(x=30, y=280)

## PlacaPatente ##
PlacaPatente_label = customtkinter.CTkLabel(app, font=font2, text="Placa Patente / Patent plate", text_color="black", bg_color="#ebebeb")
PlacaPatente_label.place(x=30, y=320)

PlacaPatente_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius= 16, width = 250)
PlacaPatente_entry.place(x=30, y=360)

## NumeroCabana ##
Cabana_label = customtkinter.CTkLabel(app, font=font2, text="Numero de Cabaña / Cabin number", text_color="black", bg_color="#ebebeb")
Cabana_label.place(x=30, y=400)

Cabana_entry = customtkinter.CTkEntry(app , font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius= 16, width = 250)
Cabana_entry.place(x=30, y=440)



## NumeroPasajeros##
NumeroPasajeros_label = customtkinter.CTkLabel(app, font=font2, text="Numero de pasajeros / Number of passengers", text_color="black", bg_color="#ebebeb")
NumeroPasajeros_label.place(x=30, y=480)

NumeroPasajeros_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius= 16, width = 250)
NumeroPasajeros_entry.place(x=30, y=520)

## Check de conformidad ##
CheckConformidad_label = customtkinter.CTkLabel(app, font=font2, text="Acepto todos los términos anteriormente descritos", text_color="black", bg_color="#ebebeb")
CheckConformidad_label.place(x=30, y=560)

control = IntVar()

CheckConformidad_entry = Checkbutton(app, font=font2, text="Acepto", variable = control)
CheckConformidad_entry.place(x=30, y=600)


                                        #########################
                                        ## Lado Izquierdo der. ##
                                        #########################
### Nacionalidad ###    
nacionalidad_label = customtkinter.CTkLabel(app, font=font2, text="Pais de origen / Country of Origin", text_color="black", bg_color="#ebebeb")
nacionalidad_label.place(x=330, y=80)

nacionalidad_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius= 16, width = 250)
nacionalidad_entry.place(x=330, y=120)


## Direccion ##
direccion_label = customtkinter.CTkLabel(app, font=font2, text="Direccion / Address", text_color="black", bg_color="#ebebeb")
direccion_label.place(x=330, y=160)

direccion_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius=16, width= 250)
direccion_entry.place(x=330, y=200)

## Ciudad ##
ciudad_label = customtkinter.CTkLabel(app, font=font2, text="Ciudad / City", text_color="black", bg_color="#ebebeb")
ciudad_label.place(x=330, y=240)

ciudad_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius=16, width =250)	
ciudad_entry.place(x=330, y=280)

## Telefono ##
telefono_label = customtkinter.CTkLabel(app, font=font2, text="Telefono / Phone number", text_color="black", bg_color="#ebebeb")
telefono_label.place(x=330, y=320)

telefono_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius= 16, width = 250)
telefono_entry.place(x=330, y=360)  

## FechaIngreso ##
FechaIngreso_label = customtkinter.CTkLabel(app, font=font2, text="Fecha de Ingreso / Check in date", text_color="black", bg_color="#ebebeb")
FechaIngreso_label.place(x=330, y=400)

FechaIngreso_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius= 16, width = 250)    
FechaIngreso_entry.place(x=330, y=440)  

## FechaSalida ##
FechaSalida_label = customtkinter.CTkLabel(app, font=font2, text="Fecha de Salida / Check out date", text_color="black", bg_color="#ebebeb")
FechaSalida_label.place(x=330, y=480)

FechaSalida_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", fg_color="#fff", border_color="#B2016C", corner_radius=16, width = 250)
FechaSalida_entry.place(x=330, y=520)

                                            ##################
                                            ## Lado Derecho ##
                                            ##################
## Horarios ##
Line1_label = customtkinter.CTkLabel(app, font=font2, text="[HORARIOS]", text_color="black", bg_color="#ebebeb")
Line1_label.place(x=683, y=30)

Line2_label = customtkinter.CTkLabel(app, font=font2, text="El horario de ingreso es a partir de las 15:00 hrs", text_color="black", bg_color="#ebebeb")
Line2_label.place(x=683, y=55)

Line3_label = customtkinter.CTkLabel(app, font=font2, text="La salida debe realizarse antes de las 11:00 am.", text_color="black", bg_color="#ebebeb")
Line3_label.place(x=683, y=80)

## Aseo Diario ##
Line4_label = customtkinter.CTkLabel(app, font=font2, text="[ASEO DIARIO]", text_color="black", bg_color="#ebebeb")
Line4_label.place(x=683, y=105)

Line5_label = customtkinter.CTkLabel(app, font=font2, text="Incluimos servicio de aseo diario de 11:00 a 15:00 hrs", text_color="black", bg_color="#ebebeb")
Line5_label.place(x=683, y=130)

Line6_label = customtkinter.CTkLabel(app, font=font2, text="siempre que las cabañas estén desocupadas", text_color="black", bg_color="#ebebeb")
Line6_label.place(x=683, y=155)
## Prohibicion de fumar ##
Line7_label = customtkinter.CTkLabel(app, font=font2, text="[PROHIBICIÓN DE FUMAR DENTRO DE LAS CABAÑAS]", text_color="black", bg_color="#ebebeb")
Line7_label.place(x=683, y=180)

Line8_label = customtkinter.CTkLabel(app, font=font2, text="Solicitamos no fumar en el interior de las cabañas.", text_color="black", bg_color="#ebebeb")
Line8_label.place(x=683, y=205)

Line9_label = customtkinter.CTkLabel(app, font=font2, text="Contamos con detectores de humo que emiten un fuerte sonido", text_color="black", bg_color="#ebebeb")
Line9_label.place(x=683, y=230)

Line10_label = customtkinter.CTkLabel(app, font=font2, text="lo cual puede resultar molesto para usted y los demás pasajeros.", text_color="black", bg_color="#ebebeb")
Line10_label.place(x=683, y=255)
##Prohibicion de ruidos ##
Line11_label = customtkinter.CTkLabel(app, font=font2, text="[PROHIBICIÓN DE RUIDOS MOLESTOS]", text_color="black", bg_color="#ebebeb")
Line11_label.place(x=683, y=280)

Line12_label = customtkinter.CTkLabel(app, font=font2, text="Somos cabañas de descanso y siempre buscamos mantener la tranquilidad.", text_color="black", bg_color="#ebebeb")
Line12_label.place(x=683, y=305)

Line13_label = customtkinter.CTkLabel(app, font=font2, text="Evite música fuerte y gritos.", text_color="black", bg_color ="#ebebeb")
Line13_label.place(x=683, y=330)
## Calefaccion ##
Line14_label = customtkinter.CTkLabel(app, font=font2, text="[CALEFACCIÓN]", text_color="black", bg_color="#ebebeb")
Line14_label.place(x=683, y=355)

Line15_label = customtkinter.CTkLabel(app, font=font2, text="Todas las cabañas cuentan con calefacción de aire acondicionado.", text_color="black", bg_color="#ebebeb")
Line15_label.place(x=683, y=380)

Line16_label = customtkinter.CTkLabel(app, font=font2, text="Los departamentos tipo estudio disponen de calefacción eléctrica.", text_color="black", bg_color="#ebebeb")
Line16_label.place(x=683, y=405)
## Al momento del Check Out ##
Line17_label = customtkinter.CTkLabel(app, font=font2, text="[AL MOMENTO DEL CHECK OUT]", text_color="black", bg_color="#ebebeb")
Line17_label.place(x=683, y=430)

Line18_label = customtkinter.CTkLabel(app, font=font2, text="El día de su salida, le solicitamos dejar las llaves en recepción.", text_color="black", bg_color="#ebebeb")
Line18_label.place(x=683, y=455)
## Comunicacion ##
Line19_label = customtkinter.CTkLabel(app, font=font2, text="[COMUNICACION]", text_color="black", bg_color="#ebebeb")
Line19_label.place(x=683, y=480)

Line20_label = customtkinter.CTkLabel(app, font=font2, text="Es importante mantener una buena comunicación.", text_color="black", bg_color="#ebebeb")
Line20_label.place(x=683, y=505)

Line21_label = customtkinter.CTkLabel(app, font=font2, text="Estamos siempre disponibles a través del número de celular y/o WhatsApp", text_color="black", bg_color="#ebebeb")
Line21_label.place(x=683, y=530)

Line22_label = customtkinter.CTkLabel(app, font=font2, text="+56 9 98115213, el cual se encuentra en el llavero y tazones.", text_color="black", bg_color="#ebebeb")
Line22_label.place(x=683, y=555)
                    
                                            #####################
                                            ## Botones a  usar ##
                                            #####################

                                        ### Boton de Ingreso de datos ###   


submit_button = customtkinter.CTkButton(app, command = BotonIngreso, font=font2, text="Ingresar", text_color="#fff", bg_color = "#131A32")
submit_button.place(x=420, y=650)

                                        ### Boton de Limpiar datos ###


clear_button = customtkinter.CTkButton(app, command=clear, font=font2, text="Limpiar Datos", text_color="#fff", bg_color = "#131A32")
clear_button.place(x=620, y=650)


registro_porton_button = customtkinter.CTkButton(app, command=EnviarSMS, font=font2, text="Registrar Telefono", text_color="#fff", bg_color = "#131A32")
registro_porton_button.place(x=820, y=650)

app.mainloop() # <-- Run the application
