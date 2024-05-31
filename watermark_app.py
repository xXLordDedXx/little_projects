import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self,window):
        self.window = window
        self.create_buttons()

    def create_buttons(self):
        self.picture = tk.Canvas(self.window, width=600, height=400, bg="dim gray", highlightthickness=0)
        self.picture.pack(pady=20)

        self.upload_btn = tk.Button(self.window, text="Upload", command=self.upload_button, bg="navajo white", fg="dim gray")
        self.upload_btn.pack(padx=20)

        self.add_text_label = tk.Label(self.window, text="Add Watermark Text:", bg="peach puff", fg="dim gray")
        self.add_text_label.pack()
        self.add_text = tk.Entry(self.window)
        self.add_text.pack(pady=3)

        self.add_text_button = tk.Button(self.window, text="Add", command=self.add_watermark, bg="navajo white", fg="dim gray")
        self.add_text_button.pack(pady=3)

        self.save_pic_button = tk.Button(self.window, text="Save Image", command=self.save_button, bg="navajo white", fg="dim gray")
        self.save_pic_button.pack(pady=3)

    def upload_button(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.image = self.image.resize((600, 400))
            self.display_image(self.image)

    def display_image(self, image):
        self.picture.image = ImageTk.PhotoImage(image)
        self.picture.create_image(0, 0, anchor="nw", image=self.picture.image)
    
    def add_watermark(self):
        watermark = self.add_text.get()
        if self.image and watermark:
            self.watermarked_image = self.image.copy()
            draw = ImageDraw.Draw(self.watermarked_image)
            font = ImageFont.truetype("arial.ttf", 36)
            width, height = self.watermarked_image.size
            _, _, text_width, text_height = draw.textbbox((0,0), text=watermark, font=font)
            x = width - text_width - 10
            y = height - text_height - 10
            draw.text((x, y), watermark, font=font, fill="white")
            self.display_image(self.watermarked_image)

    def save_button(self):
        if self.watermarked_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                self.watermarked_image.save(save_path)
                messagebox.showinfo("Image Saved", f"Image saved to {save_path}")

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Watermark App")
    window.configure(background='peach puff')
    window.geometry("1000x800")
    app = WatermarkApp(window)
    window.mainloop()
