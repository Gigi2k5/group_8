import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Python Task 3")
root.geometry("600x400")
root.resizable(True, True)

style = ttk.Style()
style.theme_use("clam")

# Creation du frame principale
main_frame = ttk.Frame(root, padding="10")
# disposition du Frame
main_frame.pack(fill=tk.BOTH, expand=True)

# Creation du label
title_label = ttk.Label(main_frame, text="Python Task 3", font=("Arial", 16, "bold"))
# Positionnement du label
title_label.pack(pady=10)

# Creation du label de Description
description_label = ttk.Label(main_frame, text="Description:")
# Disposition du Label
description_label.pack(anchor="w")

# Champs de saisie de la description et variable de récupération de la description
description_var = tk.StringVar()
description_entry = ttk.Entry(main_frame, textvariable=description_var, width=50)
# disposition du champs de saisie
description_entry.pack(fill=tk.X, pady=5)

button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=10)

spinner = ttk.Progressbar(button_frame, mode="determinate", length=50)
# Zone d'affichage de l'image
image_frame = ttk.LabelFrame(main_frame, text="Image Display Area", padding="10")

# Chargement du modèle de génération de l'image
pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")

# Fonction pour générer l'image
def generate_image():
    # récupération de la description
    prompt = description_var.get()
    if prompt == "":
        showwarning('ATTENTION', 'Veuillez entrez une description')
    else:
        spinner.start()
        image_generate = pipe(prompt).images[0]
        image_generate.save("generated_image.png")
        spinner.stop()
        
        # Affichage de l'image générée
        img = Image.open("generated_image.png")
        img_tk = ImageTk.PhotoImage(img)
        
        image_label.config(image=img_tk)
        image_label.image = img_tk

# Bouton pour générer l'image
generate_button = ttk.Button(button_frame, text="Generate Image", command=generate_image)
generate_button.pack(side=tk.LEFT)

spinner.pack(side=tk.RIGHT, padx=10)

image_frame.pack(fill=tk.BOTH, expand=True)

# Label pour afficher l'image
image_label = ttk.Label(image_frame, text="Image will be displayed here")
image_label.pack(expand=True)

root.mainloop()
