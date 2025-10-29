import customtkinter as ctk

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("500x500")
app.title("SafeNet v1.0")

def changeTxt(labelX,textX):
    labelX.configure(text="")
    app.after(1000, lambda: labelX.configure(text= textX))

bannerSafeNet= ctk.CTkLabel(app,text="SafeNet v1.0",text_color="blue",font=("Arial",20)).pack()
mainText= ctk.CTkLabel(app,text="Hoşgeldiniz!",font=("Arial",15)).pack()
app.after(3000,changeTxt(mainText,"sometimes i dream about saving the world..."))

app.mainloop()