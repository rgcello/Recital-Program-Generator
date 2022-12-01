import csv
from datetime import datetime
import glob
from venv import create


def Convert_to_list(string):
    li = list(string.split("+"))
    return li


def convert_to_sub_list(string):
    li = list(string.split("@"))
    return li


def recitalCSV_to_HTML(filepath, file):

    file_name = file.split(".")
    new_html = open("outbox/" + file_name[0] + '.html', 'w+')
    new_html.write('<!DOCTYPE html><html lang="en"><head><link rel="stylesheet" href="../css/recital.css"><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><div id="printPage">')
    with open(filepath, 'r') as csvfile:

        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0] == "Headers":
                new_html.write('<div class="header"><h2>' + row[1] + '</h2></div><div class="header"><h1>' + row[2] +
                               '</h1></div><div class="header"><h3>' + row[3] + '</h3></div><div class="header"><h4>' + row[4] + '</h4></div><div class="header"><h5>' + row[5] + '</h5></div>')
                footer = row[6]
                new_html.write('<table style="width: 100%">')
            if row[0] != "Headers":
                students = Convert_to_list(row[0])
                pieces = Convert_to_list(row[1])
                composers = Convert_to_list(row[2])
                new_html.write("<tr><td colspan='2' class='spacer'><tr><td>")
                for index, piece in enumerate(pieces):
                    new_html.write(
                        "<tr><td colspan='2'><table width='100%'><tr><td>")
                    sublist = convert_to_sub_list(piece)
                    title = sublist.pop(0)
                    mvts = sublist
                    new_html.write(
                        "<div class='piece-title'>" + title + "</div>")
                    if len(mvts) > 0:
                        new_html.write('<ol class="mvt">')
                        for mvt in mvts:
                            new_html.write("<li>" + mvt + "</li>")
                    new_html.write(
                        "</ol> </td><td style='text-align:right;'>")
                    try:
                        new_html.write(composers[index])
                    except:
                        new_html.write(' ')
                    new_html.write("</td></tr></table></td></tr>")
                #new_html.write('</td><td style="text-align:right;">')
                # for composer in composers:
                #     new_html.write("<div class='composer'>" +
                #                    composer + "</div>")
                new_html.write(
                    '</td></tr><td colspan="2" style="text-align:center">')
                for student in students:
                    new_html.write("<div class='performer'>" +
                                   student + "</div>")
                new_html.write('</td></tr>')
    new_html.write('<tr><td colspan="2" class="footer">' +
                   footer + '</td></tr></table></div></body></html>')
    new_html.close()


csv_files = glob.glob("inbox/*.csv")
print(csv_files)
for csv_file_path in csv_files:
    print("we got here!")
    filename = csv_file_path.split("/")
    recitalCSV_to_HTML(csv_file_path, filename[1])
