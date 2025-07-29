import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

def read_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Error: Unable to read image.")
    return image

def save_image(image, path):
    cv2.imwrite(path, image)
    print(f"Image saved at {path}")

def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_gaussian_blur(image, ksize=(15, 15)):
    return cv2.GaussianBlur(image, ksize, cv2.BORDER_DEFAULT)

def detect_edges(image, threshold1, threshold2):
    return cv2.Canny(image, threshold1, threshold2)

def dilate_image(image, kernel_size=(7, 7), iterations=2):
    kernel = np.ones(kernel_size, np.uint8)
    return cv2.dilate(image, kernel, iterations=iterations)

def erode_image(image, kernel_size=(7, 7), iterations=2):
    kernel = np.ones(kernel_size, np.uint8)
    return cv2.erode(image, kernel, iterations=iterations)

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rot_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, rot_matrix, (w, h))

def apply_averaging_blur(image, ksize=(15, 15)):
    return cv2.blur(image, ksize)

def crop_image(image, x, y, w, h):
    return image[y:y+h, x:x+w]

def translate_image(image, tx, ty):
    (h, w) = image.shape[:2]
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, translation_matrix, (w, h))

def apply_bilateral_filter(image, d=15, sigma_color=200, sigma_space=200):
    return cv2.bilateralFilter(image, d, sigma_color, sigma_space)

def calculate_histogram_color(image):
    if image is None:
        print("Error: Imaginea nu este valida pentru histograma.")
        return None

    colors = ('b', 'g', 'r')  
    plt.figure()
    plt.title("Histogramă de culoare")
    plt.xlabel("Bins") 
    plt.ylabel("Număr de pixeli") 
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.legend(["Albastru", "Verde", "Roșu"])
    plt.grid()
    plt.show(block=False)  

def process_image(effect, image):
    if effect == "Grayscale":
        return convert_to_grayscale(image)
    elif effect == "Gaussian Blur":
        return apply_gaussian_blur(image)
    elif effect == "Canny Edges":
        return detect_edges(image, 100, 200)
    elif effect == "Dilate":
        return dilate_image(image)
    elif effect == "Erode":
        return erode_image(image)
    elif effect == "Rotate 45°":
        return rotate_image(image, 45)
    elif effect == "Averaging Blur":
        return apply_averaging_blur(image)
    elif effect == "Crop":
        return crop_image(image, 50, 50, 200, 200)  
    elif effect == "Translate":
        return translate_image(image, 50, 50) 
    elif effect == "Bilateral Filter":
        return apply_bilateral_filter(image)
    elif effect == "Color Histogram":
        calculate_histogram_color(image)
        return image
    else:
        return image

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing Application")

        self.image = None
        self.processed_image = None

        # UI Elements
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.select_button = tk.Button(self.frame, text="Selecteaza imaginea", command=self.select_image)
        self.select_button.grid(row=0, column=0, padx=5, pady=5)

        self.effects = [
            "Grayscale", "Gaussian Blur", "Canny Edges", "Dilate", "Erode", "Rotate 45°", "Averaging Blur",
            "Crop", "Translate", "Bilateral Filter", "Color Histogram"
        ]
        self.effect_var = tk.StringVar(value=self.effects[0])

        self.effect_menu = ttk.Combobox(self.frame, textvariable=self.effect_var, values=self.effects, state="readonly")
        self.effect_menu.grid(row=0, column=1, padx=5, pady=5)

        self.apply_button = tk.Button(self.frame, text="Aplica efect", command=self.apply_effect)
        self.apply_button.grid(row=0, column=2, padx=5, pady=5)

        self.save_button = tk.Button(self.frame, text="Salveaza", command=self.save_image, state=tk.DISABLED)
        self.save_button.grid(row=0, column=3, padx=5, pady=5)

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Selecteaza o imagine", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")])
        if not file_path:
            print("No file selected.")
            return

        self.image = read_image(file_path)
        if self.image is not None:
            resized_image = resize_image(self.image, 400, 300)  # Resize for display
            self.display_image_with_tkinter(resized_image, "Imagine originala")

    def apply_effect(self):
        if self.image is None:
            print("No image selected.")
            return

        selected_effect = self.effect_var.get()
        if selected_effect == "Color Histogram":
            calculate_histogram_color(self.image)
        else:
            self.processed_image = process_image(selected_effect, self.image)

            if self.processed_image is not None:
                resized_processed_image = resize_image(self.processed_image, 400, 300)  # Resize for display
                self.display_image_with_tkinter(resized_processed_image, "Imagine procesata")
                self.save_button.config(state=tk.NORMAL)

    def display_image_with_tkinter(self, image, title):
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)
        tk_image = ImageTk.PhotoImage(pil_image)

        top = tk.Toplevel(self.root)
        top.title(title)
        label = tk.Label(top, image=tk_image)
        label.image = tk_image 
        label.pack()

    def save_image(self):
        if self.processed_image is None:
            print("No processed image to save.")
            return

        file_path = filedialog.asksaveasfilename(
            title="Save Image",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Bitmap", "*.bmp")]
        )
        if file_path:
            save_image(self.processed_image, file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
