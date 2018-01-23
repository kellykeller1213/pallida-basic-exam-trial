# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

#print(name_from_email("elek.viz@exam.com"))
import re


email = input("Please type in your E-mail address: ")


def name_extracter(data):
    input_data = re.findall(r"[\w']+|[.,!?;]", data)
    first_name, last_name = input_data[0], input_data[2]
    return last_name.capitalize() + " " + first_name.capitalize()


print(name_extracter(email))
