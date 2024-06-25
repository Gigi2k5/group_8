import tkinter as tk
from tkinter import ttk

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

# Creation du lable de Description
description_label = ttk.Label(main_frame, text="Description:")
# Disposition du Label
description_label.pack(anchor="w")
# Champs de saisir de la description
description_entry = ttk.Entry(main_frame, width=50)
# disposition du champs de saisi
description_entry.pack(fill=tk.X, pady=5)

# Je vais faire le reste plus tard t'as compris le plus important
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=10)

generate_button = ttk.Button(button_frame, text="Generate Image")
generate_button.pack(side=tk.LEFT)

spinner = ttk.Progressbar(button_frame, mode="indeterminate", length=30)
spinner.pack(side=tk.RIGHT, padx=10)

# Zone d'affichage de l'image
image_frame = ttk.LabelFrame(main_frame, text="Image Display Area", padding="10")
image_frame.pack(fill=tk.BOTH, expand=True)

image_label = ttk.Label(image_frame, text="Image will be displayed here")
image_label.pack(expand=True)

root.mainloop()
