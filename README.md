# Python Image Processor

A simple desktop application built with Python, Tkinter, and OpenCV to apply various filters and effects to images.

![Application Screenshot](https://private-user-images.githubusercontent.com/82108871/472015408-bb06047a-5d20-4e85-8bd0-562eebc813eb.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTM3OTU4MjAsIm5iZiI6MTc1Mzc5NTUyMCwicGF0aCI6Ii84MjEwODg3MS80NzIwMTU0MDgtYmIwNjA0N2EtNWQyMC00ZTg1LThiZDAtNTYyZWViYzgxM2ViLlBORz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzI5VDEzMjUyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFkZjk4MWZhMGFjMTZlZjliYzI3ZmI1MjAyZjM0ZDNiYTYwMzEzMmFkOGNhMmQwZjJjYjg3OTdmMjhjOGRmZmYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.0OTPiMmYtwYJiWKZ5zT_WhJPQDHiGAgjXc3cH1rLKLE)

---

### ✨ Features

*   **Load Images:** Open local image files (`.jpg`, `.png`, `.bmp`).
*   **Apply Effects:** A wide variety of image processing filters are available:
    *   **Color:** Grayscale Conversion.
    *   **Blurring:** Gaussian, Averaging, and Bilateral filters.
    *   **Detection:** Canny Edge Detection.
    *   **Morphology:** Dilation and Erosion.
    *   **Transforms:** Rotate, Crop, and Translate the image.
*   **Analysis:** Generate and display a color histogram using Matplotlib.
*   **Save:** Save the processed image to a new file on your disk.

---

### 🛠️ Tech Stack

*   **Python:** Core programming language.
*   **OpenCV:** For all image processing functionalities.
*   **Tkinter:** For the graphical user interface (GUI).
*   **Pillow (PIL):** To bridge OpenCV images with the Tkinter UI.
*   **Matplotlib:** To generate and display the color histogram.
*   **NumPy:** For numerical operations and matrix manipulations.

---

### 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

#### Prerequisites

*   You need to have [Python](https://www.python.org/downloads/) installed on your system.

#### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/oanacristina21/Python-Image-Processor.git
    ```
    *(Remember to replace the URL if your username or repository name is different.)*

2.  **Navigate to the project directory:**
    ```sh
    cd Python-Image-Processor
    ```

3.  **Install the required dependencies from `requirements.txt`:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```sh
    python app.py
    ```

---
