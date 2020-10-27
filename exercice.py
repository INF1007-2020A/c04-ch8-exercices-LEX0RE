#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def compare_file(title1, title2):
    if title1 != title2:
        with open(title1, encoding="utf-8") as file1, open(title2, encoding="utf-8") as file2:
            for line1 in file1:
                line2 = file2.readline()
                if line1 != line2:
                    print(f"Dif : {line1} and {line2}")
                    break

                
def triple_space(input_file, output_file):
    with open(input_file, encoding="utf-8") as file1, open(output_file, "w", encoding="utf-8") as file2:
        for line in file1:
            file2.write(line.replace(" ", "   "))

def attribute_letter(input_file, output_file):
    with open(input_file, encoding="utf-8") as in_file, open(output_file, "w", encoding="utf-8") as out_file:
        for line in in_file:
            for letter, notes in PERCENTAGE_TO_LETTER.items():
                note = int(line.strip())
                if notes[1] > note >= notes[0]:
                    out_file.write(str(note) + " " + letter + "\n")
                    break

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #compare_file("exemple.txt", "notes.txt")
    #triple_space("exemple.txt", "test.txt")
    attribute_letter("notes.txt", "notes_result.txt")
    pass
