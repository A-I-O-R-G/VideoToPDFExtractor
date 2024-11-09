import cv2
import numpy as np
import os
import pytesseract
from fpdf import FPDF

class PDFGenerator:
    def __init__(self, title):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(0, 10, title, 0, 1, 'C')
        self.pdf.set_font("Arial", size=12)

    def add_image(self, image_path):
        self.pdf.add_page()
        self.pdf.image(image_path, x=10, y=10, w=180)
    
    def add_text(self, text):
        self.pdf.multi_cell(0, 10, txt=text)
    
    def save(self, filename):
        self.pdf.output(filename)

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    if not cap.isOpened():
        print("Error: Unable to open video.")
        return frames

    current_frame = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process every 30 frames for efficiency
        if current_frame % 30 == 0:
            frames.append(frame)
        
        current_frame += 1

    cap.release()
    return frames

def extract_text_from_frames(frames):
    texts = []
    for frame in frames:
        # Convert the frame to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(gray)
        texts.append(text.strip())
    return texts

def main():
    video_path = 'path_to_your_video.mp4'  # Substitua com o caminho do seu vídeo
    output_pdf = 'Extracted_Content.pdf'
    
    # Extrair quadros do vídeo
    frames = extract_frames(video_path)
    if not frames:
        print("No frames extracted. Exiting.")
        return

    # Extrair texto dos quadros
    extracted_texts = extract_text_from_frames(frames)

    # Criação do gerador de PDF
    pdf = PDFGenerator(title="Conteúdo Extraído do Vídeo")

    # Adicionar imagens e textos ao PDF
    for i, frame in enumerate(frames):
        image_path = f"frame_{i}.png"
        cv2.imwrite(image_path, frame)  # Salvar o frame como imagem
        pdf.add_image(image_path)  # Adicionar imagem ao PDF
        pdf.add_text(extracted_texts[i])  # Adicionar texto extraído ao PDF

        # Remover imagem salva para economizar espaço
        os.remove(image_path)

    # Salvar o PDF
    pdf.save(output_pdf)
    print(f"PDF '{output_pdf}' gerado com sucesso!")

if __name__ == '__main__':
    main()