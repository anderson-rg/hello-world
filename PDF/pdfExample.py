filename = 'Mypdf.pdf'
documentTitle = 'Teste'
title = 'Projeto Teste'
subTitle = 'Teste 2'

testLines = [
    'escreva um texto aqui'

]









from reportlab.pdfgen import canvas
pdf = canvas.Canvas(filename)

pdf.save()
