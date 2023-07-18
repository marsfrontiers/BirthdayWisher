import datetime as dt
import pandas
import random
import smtplib

########################## Birthday wisher project ######################################
MY_EMAIL = "marsfrontiers@gmail.com"
PASSWORD = "jnazanlhjetwjpva"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

################################## Send Quotes Project###################################

# MY_EMAIL = "marsfrontiers@gmail.com"
# PASSWORD = "jnazanlhjetwjpva"
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 4:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="yusuf.8786@gmail.com",
#             msg=f"Subject:Today's Motivation!\n\n{quote}"
#         )

######################### how to use smtp #########################
# import smtplib
#
# my_email = "marsfrontiers@gmail.com"
# password = "jnazanlhjetwjpva"
#
# with smtplib.SMTP("smtp.gmail.com") as connect:
#     connect.starttls()
#     connect.login(user=my_email, password=password)
#     connect.sendmail(
#         from_addr=my_email,
#         to_addrs="yusuf.8786@gmail.com",
#         msg="Subject:Hello\n\nThis is the example!"
#     )
##################################### how to use datetime ##############################3
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# week = now.weekday()
# day = now.day
# hour = now.hour
# dob = dt.datetime(year=1998, month=12, day=24, hour=11)
# print(month)
