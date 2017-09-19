# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

#print(name_from_email("elek.viz@exam.com"))
import re

def name_extracter():
    email = input("Please type in your E-mail address: ")
    input_data = re.findall(r"[\w']+|[.,!?;]", email)
    first_name = input_data[0]
    second_name = input_data[2]
    print(second_name.capitalize() , first_name.capitalize())

name_extracter()