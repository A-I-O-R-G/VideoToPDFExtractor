
### Documentação Detalhada

#### 1. Introdução
Este software é um gerador de PDF que extrai frames de um vídeo e utiliza reconhecimento óptico de caracteres (OCR) para extrair texto desses frames. Os resultados (imagens e textos) são organizados em um arquivo PDF, permitindo a documentação do conteúdo visual e textual do vídeo.

#### 2. Instalação
Para instalar as bibliotecas necessárias, utilize o seguinte comando:
```bash
pip install opencv-python pytesseract fpdf
```
Além disso, você precisa ter o Tesseract-OCR instalado no seu sistema. Você pode encontrar instruções de instalação no [repositório do Tesseract](https://github.com/tesseract-ocr/tesseract).

#### 3. Uso
- Altere a variável `video_path` para o caminho do vídeo que deseja processar.
- Execute o script. O PDF resultante será salvo como `Extracted_Content.pdf`.

Exemplo de como rodar o script:
```bash
python script.py
```

#### 4. Referência de API
- **PDFGenerator**: Classe responsável pela criação de PDFs.
  - `__init__(self, title)`: Inicializa o PDF com um título.
  - `add_image(self, image_path)`: Adiciona uma imagem ao PDF.
  - `add_text(self, text)`: Adiciona texto ao PDF.
  - `save(self, filename)`: Salva o PDF com o nome especificado.

- `extract_frames(video_path)`: Extrai frames de um vídeo. Retorna uma lista de frames processados.
  - Parâmetro: `video_path` (str): Caminho do arquivo de vídeo.

- `extract_text_from_frames(frames)`: Extrai texto dos frames utilizando Tesseract. Retorna uma lista de textos extraídos.
  - Parâmetro: `frames` (list): Lista de frames de vídeo.

#### 5. Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para fazer fork do repositório e enviar as suas melhorias.

#### 6. Licença
Este projeto é licenciado sob a MIT License. Veja o arquivo LICENSE para mais informações.