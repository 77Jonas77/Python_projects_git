import pandas as pd
import datetime as dt
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
MY_EMAIL = "jonasz.sojkaa@gmail.com"
PASSWORD = "yoei vfrg nodd fmdq"
birthdays = {}


def load_birthdays():
    global birthdays
    df = pd.read_csv("birthdays.csv")
    birthdays = df.to_dict(orient="records")


def prepare_birthday_wishes(birthday):
    with open("letter_templates/letter_3.txt", "r") as birthday_file:
        bf_text = birthday_file.read()
        return bf_text.replace("[NAME]", birthday["name"])


def check_birthdays():
    global birthdays
    for birthday in birthdays:
        if (birthday["month"] == dt.datetime.now().month
                and birthday["day"] == dt.datetime.now().day):
            send_mail(prepare_birthday_wishes(birthday))


def send_mail(text):
    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(user=MY_EMAIL, password=PASSWORD)
        con.sendmail(from_addr=MY_EMAIL,
                     to_addrs="sssjonasz4@gmail.com",
                     msg=f"Subject:WSZYSTKIEGO NAJLEPSZEGO!\n\n{text}")


if __name__ == "__main__":
    load_birthdays()
    check_birthdays()
