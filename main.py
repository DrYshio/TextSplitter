from docx import Document
import os


ans = input("Нужно ли собирать файлы из папки text? y/n")
if ans == 'y':
    #Collector





sum_file = Document('input.docx')


def create_new_docx():
    document = Document()
    return document


list_of_output = []
num = 0
i = 0
list_of_output.append(create_new_docx())

for paragraph in sum_file.paragraphs:
    list_of_output[i].add_paragraph(paragraph.text)
    num += len(paragraph.text)

    if num >= 56792:
        num = 0
        list_of_output[i].save(str(i) + '.docx')
        i += 1
        list_of_output.append(create_new_docx())

list_of_output[i].save(str(i) + '.docx')








