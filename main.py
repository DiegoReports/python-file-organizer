import os 
from tkinter.filedialog import askdirectory

# ABRIR POP SELECIONAR
caminho = askdirectory(title="Selecione uma pasta")

# IDENTIFICANDO FILES
lista_arquivos = os.listdir(caminho)

# DICIONARIO DE FILES
locais ={
  "imagens": [".png", ".jpg", ".bmp"],
  "planilhas": [".xlsx", ".csv"],
  "jwLibraryFiles": [".jwpub"],
  "documentosWord": [".doc", ".docx"],
  "compactados": [".zip", ".rar"],
  "musicas": [".mp3"]
}

# PERCORRENDO LISTA DE FILES
for arquivo in lista_arquivos:
  #extraindo extensão do file
  nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
  for pasta in locais:
    if extensao in locais[pasta]:
      #verf se existe pasta no caminho
      if not os.path.exists(f"{caminho}/{pasta}"):
        #criando a pasta
        os.mkdir(f"{caminho}/{pasta}")
        #reorganizando os arquivos
      os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")