import smtplib
import filemanager

def main():
    sender = "mhoow6@gmail.com"
    receiver = "mhoow6@gmail.com"
    username = "mhoow6"
    password = ""

    log = open(filemanager.getlogfilepath(filemanager.getlogfilename()), mode='r', encoding='utf-8').read().encode()

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username, password)
    # sender가 receiver에게 log 전송
    server.sendmail(sender, receiver, log)
    server.quit()

# https://www.youtube.com/watch?v=BkMtK-cyyEE&list=WL&index=3&t=4s