# mail service
import smtplib


def send_email(my_mail, my_password, receiver, title, text):

    #TODO:should format this part with f-string, and test it!!!
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (my_mail, ", ".join(receiver), title, text)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(my_mail, my_password)
        smtp_server.sendmail(my_mail, receiver, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….", ex)



def alarma(my_mail, my_password, client_email):
    #TODO:implement handling of out of control spending!
    send_email(my_mail, my_password, client_email, "Prejebo si ga", "You are over the limit")
