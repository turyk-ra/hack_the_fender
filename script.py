# Are you there? We’ve opened up a communications link to The Fender‘s secret computer. We need you to write a program that will read in the compromised usernames and passwords that are stored in a file called "passwords.csv".
#
# First import the CSV module, since we’ll be needing it to parse the data.
import csv

# We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable compromised_users.
compromised_users = []
# Next we’ll need you to open up the file itself. Store it in a file object called password_file.
with open("passwords.csv","r") as password_file:
# Pass the password_file object holder to our CSV reader for parsing. Save the parsed csv.DictReader object as password_csv.
    password_csv = csv.DictReader(password_file)