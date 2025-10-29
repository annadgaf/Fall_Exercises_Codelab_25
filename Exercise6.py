import tkinter as tk 

# Window
root = tk.Tk()
root.title("Movie Details")
root.geometry("600x400")
root.configure (bg = "#e88da7")

# Title
title_label = tk.Label(
    root, 
    text = "Howl's Moving Castle", 
    font = ("Georgia", 20, "bold"), 
    bg = "#e88da7", 
    fg = "#782c2c"
    )
title_label.place(
    x = 50, 
    y = 20, 
    width = 500, 
    height = 40
    )

# Release Date
release_label1 = tk.Label(
    root, 
    text = "Release Date:", 
    font = ("Georgia", 12, "bold"), 
    bg = "#e88da7", 
    fg = "#5c949c"
    )
release_label1.place(
    x = 50, 
    y = 80
    )
release_label2 = tk.Label(
    root, 
    text = "20 November, 2004", 
    font = ("Georgia", 12), 
    bg = "#e88da7", 
    fg = "#eac41a"
    )
release_label2.place(
    x = 200, 
    y = 80
    )

# Director
director_label1 = tk.Label(
    root, 
    text = "Director:", 
    font = ("Georgia", 12, "bold"), 
    bg = "#e88da7", 
    fg = "#5c949c"
    )
director_label1.place(
    x = 50, 
    y = 110
    )
director_label2 = tk.Label(
    root, 
    text = "Hayao Miyazaki", 
    font = ("Georgia", 12), 
    bg = "#e88da7", 
    fg = "#eac41a"
    )
director_label2.place(
    x = 200, 
    y = 110
    )

# Character
character_label1 = tk.Label(
    root, 
    text = "Main Character:", 
    font = ("Georgia", 12, "bold"), 
    bg = "#e88da7", 
    fg = "#5c949c"
    )
character_label1.place(
    x = 50, 
    y = 140
    )
character_label2 = tk.Label(
    root, 
    text = "Wizard Howl, Sophie Hatter", 
    font = ("Georgia", 12), 
    bg = "#e88da7", 
    fg = "#eac41a"
    )
character_label2.place(
    x = 200, 
    y = 140
    )

# Genre
genre_label1 = tk.Label(
    root, 
    text = "Genre:", 
    font = ("Georgia", 12, "bold"), 
    bg = "#e88da7", 
    fg = "#5c949c"
    )
genre_label1.place(
    x = 50, 
    y = 170
    )
genre_label2 = tk.Label(
    root, 
    text = "Anime, Fantasy, Drama", 
    font = ("Georgia", 12), 
    bg = "#e88da7", 
    fg = "#eac41a"
    )
genre_label2.place(
    x = 200, 
    y = 170
    )

# Runtime
runtime_label1 = tk.Label(
    root, 
    text = "Runtime:", 
    font = ("Georgia", 12, "bold"), 
    bg = "#e88da7", 
    fg = "#5c949c"
    )
runtime_label1.place(
    x = 50, 
    y = 200
    )
runtime_label2 = tk.Label(
    root, 
    text = "119 minutes", 
    font = ("Georgia", 12), 
    bg = "#e88da7", 
    fg = "#eac41a"
    )
runtime_label2.place(
    x=200, 
    y = 200
    )

# Short Description
desc_label1 = tk.Label(
    root, text = "Sypnosis:", 
    font = ("Georgia", 12, "bold"), 
    bg = "#e88da7", 
    fg = "#5c949c"
    )
desc_label1.place(
    x = 50, 
    y = 230
    )
desc_text = (
    "Howl's Moving Castle follows Sophie, a young hat maker cursed into an old woman by a jealous witch."
             "She takes refuge in wizard Howl’s magical castle, where she teams up with a fire demon named Calcifer to break her spell."
              "As she learns more about Howl, Sophie realizes he’s not as heartless as he seems, and together they face their fears during a looming war."
              )
desc_label2 = tk.Label(
    root, 
    text = desc_text, 
    wraplength = 500, 
    justify = "left", 
    font = ("Georgia", 12), 
    bg = "#e88da7", 
    fg = "#eac41a"
    )
desc_label2.place(
    x = 50, 
    y = 260
    )

# Exit Button
exit_button = tk.Button(
    root, 
    text = "Close", 
    font = ("Georgia", 12), 
    command = root.destroy, 
    bg = "#3c5159", 
    fg = "#e88da7"
    )
exit_button.place(
    x = 260, 
    y = 340, 
    width = 80, 
    height = 30
    )

# Run window
root.mainloop()