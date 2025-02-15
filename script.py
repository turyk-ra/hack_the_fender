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
# Now we’ll want to iterate through each of the lines in the CSV.
#
# Create a for loop and save each row of the CSV into the temporary variable password_row.
    for password_row in password_csv:
# Inside your for loop, print out password_row['Username']. This is the username of the person whose password was compromised.
#
# Run your code, do you see a list of usernames?
#         print(password_row['Username'])
# Remove the print statement. We want to add each username to the list of compromised_users. Use the list’s .append() method to add the username to compromised_users instead of printing them.
        compromised_users.append(password_row['Username'])
# Exit out of your with block for "passwords.csv". We have all the data we need from that file.
#
# Start a new with block, opening a file called compromised_users.txt. Open this file in write-mode, saving the file object as compromised_user_file.
with open("compromised_users.txt", "w") as compromised_user_file:
