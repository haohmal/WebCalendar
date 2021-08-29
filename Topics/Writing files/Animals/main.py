# read animals.txt
# and write animals_new.txt
animal_string = ""
in_file = open("animals.txt", "r", encoding='utf-8')
for line in in_file:
    animal_string += line.strip() + " "

in_file.close()

out_file = open("animals_new.txt", "w", encoding='utf-8')
out_file.write(animal_string.strip())
out_file.close()