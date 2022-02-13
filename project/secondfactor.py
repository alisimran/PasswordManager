import os
import random
import math
import smtplib
import string
import getpass


def generateOTP():
    OTP = ""
    gen = random.randrange(99999, 1000000)
    OTP += str(gen)
    return OTP

def sendOTP(email, passwd):
    OTP = generateOTP()
    msg = f"OTP for verification is {OTP}"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, passwd)
    s.sendmail('&&&&&&&', email, msg)
    otp_given = getpass.getpass("Enter your OTP: ")
    if otp_given == OTP:
        return True
    return False
     
