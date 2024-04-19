import smtplib
import datetime as dt
import random as rnd

MY_EMAIL = "jonasz.sojkaa@gmail.com"
PASSWORD = "yoei vfrg nodd fmdq"

quotes = []


def load_quotes():
    with open('quotes.txt', 'r') as f:
        for line in f:
            quotes.append(line)
        # quotes = f.readlines()


def send_mail(quote):
    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(user=MY_EMAIL, password=PASSWORD)
        con.sendmail(from_addr=MY_EMAIL, to_addrs="sssjonasz4@gmail.com",
                     msg=f"Subject:temacik cnie\n\n{quote}")


# if dt.datetime.weekday() == 0:
if __name__ == '__main__':
    load_quotes()
    send_mail(rnd.choice(quotes))
