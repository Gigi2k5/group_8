import tkinter as tk
from tkinter import *
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageTk

# Création de la fenêtre principale
fenetre = Tk()
fenetre.geometry('600x600')
fenetre.title('OrdiRoutier - Tkinter generateImage')
fenetre['bg'] = 'white'
fenetre.resizable(height=False, width=False)

# Chargement et affichage de l'image principale
photo = PhotoImage(file='home1.png')
label = Label(fenetre, image=photo)
label.place(x=120, y=90)

message_photo = PhotoImage(file='message3.png')
message_label = Label(fenetre, image=message_photo, bg='white')  # Utilisez bg='white' si nécessaire
message_label.place(x=120, y=90) 

# Fonction pour créer une nouvelle fenêtre
def nouvelle_fenetre():
    Nfenetre = Toplevel(fenetre)  # Utiliser Toplevel pour éviter plusieurs instances de Tk()
    Nfenetre.geometry('500x500')
    Nfenetre.title('OrdiRoutier - Nouvelle Fenêtre')
    Nfenetre['bg'] = 'white'
    Nfenetre.resizable(height=False, width=False)
    
    ma_variable = StringVar()  
    label = Label(Nfenetre, text="Que voulez-vous créer ?",font=("Bartender and Cocktail",10) ,fg='black', bg='white')
    label.place(x=20, y=10)
    entree = Entry(Nfenetre, textvariable=ma_variable)
    entree.place(x=20, y=35, width=300)
    # Création d'un conteneur pour les images générées avec un fond gris
    image_frame = Frame(Nfenetre, bg='gray', width=460, height=400)
    image_frame.place(x=20, y=80)
    def image_generate():
        pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
        prompt = ma_variable.get()
        image = pipe(prompt).images[0]
        image.save("generated_image.png")
        
        # Charger et afficher l'image générée
        generated_image = Image.open("generated_image.png")
        generated_image = generated_image.resize((460, 400), Image.ANTIALIAS)  # Redimensionner si nécessaire
        photo = ImageTk.PhotoImage(generated_image)
        image_label = Label(image_frame, image=photo)
        image_label.image = photo  # Conserver une référence à l'image
        image_label.pack()
    bouton = Button(Nfenetre, text="Generate", command=image_generate, bg='black', fg='white',font=("Bartender and Cocktail",15,"italic"))
    bouton.place(x=330, y=30)




# Chargement de l'image du bouton
BouttonImg = PhotoImage(file='button.png')
# Création du bouton avec l'image et la commande
bouton = Button(fenetre, image=BouttonImg, borderwidth=0, highlightthickness=0, command=nouvelle_fenetre)
bouton.place(x='10', y='395')

# Boucle principale de la fenêtre
fenetre.mainloop()
