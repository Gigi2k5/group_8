import tkinter as tk
from os import pipe
import customtkinter
from tkinter.messagebox import showwarning
from PIL import Image, ImageTk


customtkinter.set_default_color_theme("dark-blue")


def resize_image(image_path, new_size):
    image = Image.open(image_path)
    resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


def generate_image():
    # récupération de la description
    prompt = description_var.get()
    if prompt == "":
        showwarning('ATTENTION', 'Veuillez entrer une description')
    else:
        loading_spinner.start()
        image_generate = pipe(prompt).images[0]
        image_generate.save("generated_image.png")
        loading_spinner.stop()

        # Affichage de l'image générée
        img = Image.open("generated_image.png")
        img_tk = ImageTk.PhotoImage(img)

        image_label.config(image=img_tk)
        image_label.image = img_tk


image_path = "chatbot.png"
app = tk.Tk()
app.title('générateur d\'images')
app.geometry('600x670')
app.resizable(False, False)
app.iconbitmap("chatbot.ico")
app.configure(bg="#24384B")

new_size = (80, 80)
image = resize_image(image_path, new_size)
image_label = tk.Label(app, bg="#24384B", image=image)
image_label.image = image
image_label.pack()
image_label.place(x=250, y=70)

my_label = customtkinter.CTkLabel(app, text="Générateur d'images", font=("Arial", 16, "bold"), text_color="white")
my_label.pack()
my_label.place(x=230, y=30)

description = customtkinter.CTkLabel(app, text="Description :", text_color="white")
description.pack()
description.place(x=20, y=160)

description_var = tk.StringVar()
generate_entry = customtkinter.CTkEntry(app, placeholder_text="Décrivez votre image", textvariable=description_var)
generate_entry.configure(width=555, text_color="black")
generate_entry.pack()
generate_entry.place(x=20, y=190)

loading_spinner = customtkinter.CTkProgressBar(app, mode="indeterminate")
loading_spinner.pack()
loading_spinner.place(x=20, y=260)
# Pas besoin d'arrêter le spinner au départ si vous voulez qu'il tourne indéfiniment

my_button = customtkinter.CTkButton(app, text="Générer", command=generate_image)
my_button.pack()
my_button.place(x=20, y=225)

canvas = tk.Canvas(app, width=400, height=350, highlightthickness=2, highlightbackground="black")
canvas.pack()
canvas.place(x=100, y=280)

texte = canvas.create_text(200, 180, text="L'image sera affichée ici", font=("Helvetica", 10))

app.mainloop()
