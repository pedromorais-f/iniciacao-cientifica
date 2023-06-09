import pandas as pd
import csv
import os


def file_path(extension):
    name_file = input("Put the file's name:")

    name_file_split = name_file.split(".")

    if extension != name_file_split[1]:
        print("ERROR: The File's extension is incorrect\n")
        return

    return name_file


def write_file():
    name_file = file_path("txt")

    data_list = []
    flag = True

    while flag:
        validation = input("\nDo you wanna add information to the file? (yes or no):")

        if validation == "yes":
            while True:
                str = input("Write the information (write \"done\" when you finished):")
                data_list.append(str)

                if str == "done":
                    break
        elif validation == "no":
            flag = False
        else:
            print("Please, put a valid answer\n")

    with open(name_file, "w") as f:
        for data in data_list:
            f.write(f"{data}\n")

    f.close()


def read_file():
    name_file = file_path("txt")

    try:
        with open(name_file, "r") as f:
            file_lines = f.readlines()

            for i, file_line in enumerate(file_lines):
                file_line = file_line.replace("\n", "")
                print(f"{i + 1}| {file_line}")
        f.close()
    except FileNotFoundError as error:
        print(error)


def write_file_csv():
    name_file = file_path("csv")

    data_list = [["NAME", "EMAIL", "DATE OF BIRTH"]]

    while True:
        validation = input("\nDo you wanna add information to the file? (yes or no):")

        if validation == "yes":
            while True:
                name = input("\nWrite the name (write \"done\" when you finished):")
                if name == "done":
                    break

                email = input("Write the email:")
                date_of_birth = input("Write the date of birth:")

                data_list_info = [name, email, date_of_birth]
                data_list.append(data_list_info)
        elif validation == "no":
            break
        else:
            print("Please, put a valid answer\n")

        with open(name_file, "w") as f:
            data_writer = csv.writer(f)
            for row in data_list:
                data_writer.writerow(row)
        f.close()


def read_file_csv():
    name_file = file_path("csv")

    try:
        # with open(name_file, "r") as f:
        # f_csv = csv.reader(f)
        # for row in f_csv:
        # print(row)
        # f.close()

        f_csv = pd.read_csv(name_file)
        print(f_csv)
    except FileNotFoundError as error:
        print(error)


def list_of_files():
    name_dir = input("Write the path of directory:")

    for name_dir, name_files, f_file in os.walk(name_dir):
        print(f_file)
