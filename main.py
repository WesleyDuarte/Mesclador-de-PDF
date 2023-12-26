import PyPDF2
import os

merger = PyPDF2.PdfMerger()

listaDeArquivos = os.listdir('arquivos')
listaDeArquivos.sort()

for arquivo in listaDeArquivos:
    if '.pdf' in arquivo:
        merger.append(f'arquivos/{arquivo}')

merger.write('PdfMesclado.pdf')        