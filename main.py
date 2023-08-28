import os.path

from fpdf import FPDF
from datetime import datetime

date_now = datetime.now()
pdf = FPDF()

# Ingreso de info doc
INSTITUTION = ""
DESCRIPTION = ""
CAREER = ""
NAME = ""
CARNE = ""
URL_LOGO_INSTITUTION = ""
FOLDER_IMG = "./img/"

course = input("Ingrese el curso -> ")
nameWork = input("Ingrese el nombre de la tarea -> ")

list_of_images = []

if os.path.exists(FOLDER_IMG) and os.path.isdir("./img"):
    contend = os.listdir("./img")
    if contend:
        print("========== Contend of the folder img ==========")
        for index, img in enumerate(contend):
            if img != "logo":
                print(f"{index+1} - {img}")
                list_of_images.append(img)
        print("=================================================")
    else:
        print("folder is empty")

pdf.add_page()
pdf.set_font("Arial", size=10)

# Encabezados de la tabla
pdf.cell(40, 40, "")
pdf.image(URL_LOGO_INSTITUTION, 10, 10, 40, 35)  # Ajustar posición y tamaño

pdf.set_fill_color(255, 255, 255)
pdf.set_font("Arial", "B", size=10)  # Cambiar a negrita
pdf.cell(150, 5, INSTITUTION, border=1, ln=True, align='C', fill=True)
pdf.set_font("Arial", size=10)
pdf.cell(40, 40, "")
pdf.cell(150, 5, DESCRIPTION, border=1, ln=True, align='C', fill=True)

# Datos de la tabla
pdf.set_fill_color(255, 255, 255)  # Restablecer el color de relleno
pdf.cell(40, 40, "")
pdf.cell(75, 5, CAREER, 1)
pdf.cell(75, 5, "Curso: " + course, 1, ln=True)
pdf.cell(40, 40, "")
pdf.cell(75, 5, nameWork, 1)
pdf.cell(75, 5, "Fecha: " + date_now.strftime('%d-%m-%Y'), 1, ln=True)
pdf.cell(40, 40, "")
pdf.cell(150, 5, "Nombre: " + NAME, border=1, ln=True, align='L', fill=True)
pdf.cell(40, 40, "")
pdf.cell(150, 5, "Carnet: " + CARNE, border=1, ln=True, align='L', fill=True)
pdf.ln()
pdf.ln()


# Agregar la primera imagen después de la tabla
pdf.image(FOLDER_IMG+list_of_images[0], pdf.x, pdf.y, pdf.w-30, pdf.h)

# Agregar el resto de las imágenes
for image in list_of_images[1:]:
    pdf.add_page()
    image_path = FOLDER_IMG+image
    pdf.image(image_path, pdf.x, pdf.y, pdf.w-30, pdf.h)

name_doc_input = input("Ingrese el nombre del Documento -> ")
name_doc_output = name_doc_input + " - ("+CARNE+").pdf"
pdf.output(name_doc_output)
