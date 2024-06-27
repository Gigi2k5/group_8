import tkinter as tk
from tkinter import ttk
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageTk

#Fonction pour créer une nouvelle fenêtre
def image_generate_window():
    image_window = tk.Toplevel(main_window)
    image_window.title("Image generator")
    image_window.geometry("600x400")
    image_window.resizable(True, True)
    style = ttk.Style()
    style.theme_use("clam")
#Creation du frame principale
    main_frame = ttk.Frame(image_window, padding="10")
#disposition du Frame
    main_frame.pack(fill=tk.BOTH, expand=True)
#Creation du label
    title_label = ttk.Label(main_frame, text="Welcome to our interface!!!", font=("Arial", 16))
#Positionnement du label
    title_label.pack(pady=10)
#Creation du label de Description
    description_label = ttk.Label(main_frame, text="Description:")
#Disposition du Label
    description_label.pack(anchor="w")
#Champs de saisie de la description
    description_var = tk.StringVar()
    description_entry = ttk.Entry(main_frame, textvariable=description_var, width=50)
#disposition du champs de saisie
    description_entry.pack(fill=tk.X, pady=5)
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=10)
#bar de progression, ne marche plus , à revoir
    spinner = ttk.Progressbar(button_frame, mode="determinate", length=50)
#Zone d'affichage de l'image
    image_frame = ttk.LabelFrame(main_frame, text="Image Display Area", padding="10")
#Chargement du modèle de génération de l'image
    pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
#Fonction pour générer l'image
    def generate_image():
#récupération de la description
        prompt = description_var.get()
        if prompt == "":
            pass
        else:
            spinner.start()
            image_generate = pipe(prompt).images[0]
            image_generate.save("img/generated_image.png")
            spinner.stop()
#Affichage de l'image générée
            img = Image.open("img/generated_image.png")
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk
#Bouton pour générer l'image
    generate_button = ttk.Button(button_frame, text="Generate Image", command=generate_image)
    generate_button.pack(side=tk.LEFT)
    spinner.pack(side=tk.RIGHT, padx=10)
    image_frame.pack(fill=tk.BOTH, expand=True)
#Label pour afficher l'image
    image_label = ttk.Label(image_frame, text="Image will be displayed here")
    image_label.pack(expand=True)
    image_window.mainloop()

#Création de la fenêtre principale
main_window = tk.Tk()
main_window.geometry('600x400')
main_window.title('Image generator')
main_window['bg'] = 'white'
main_window.resizable(height=False, width=False)

#Chargement et affichage de l'image principale
main_window_photo = tk.PhotoImage(file='img/home.png')
label = tk.Label(main_window, image=main_window_photo)
label.place(x=130, y=20)
#logo de l'app
logo = tk.PhotoImage(file='img/logo.png')
logo_label = tk.Label(main_window, image=logo, bg='white')
logo_label.place(x=120, y=90) 
# Chargement de l'image du bouton
BouttonImg = tk.PhotoImage(file='img/button.png')
#Création du boutton qui ouvre la fenêtre de génération d'image
bouton = tk.Button(main_window, image=BouttonImg, borderwidth=0, highlightthickness=0, command=image_generate_window)
bouton.place(x=210, y=335)
# Boucle principale de la fenêtre
main_window.mainloop()
