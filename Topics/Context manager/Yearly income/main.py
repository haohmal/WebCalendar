with open("salary.txt", "r", encoding="utf-8") as in_file, open("salary_year.txt", "w", encoding="utf-8") as out_file:
    for line in in_file:
        out_file.writelines(str(int(line.strip()) * 12) + "\n")

