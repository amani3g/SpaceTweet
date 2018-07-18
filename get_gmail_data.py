'''
Get data from body of an email

Works With Python Version 2.7
Use with command "Python get_gmail_data.py" on this machine
'''
import smtplib
import time
import imaplib
import email



ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "birst2018summer" + ORG_EMAIL
FROM_PWD = "Birst2018"
SMTP_SERVER = "imap.gmail.com" #use smtp.gmail.com if you are trying to send mail
SMTP_PORT = 993


    
mail = imaplib.IMAP4_SSL(SMTP_SERVER) #using imap to connect to the SMTP server over SSL
mail.login(FROM_EMAIL, FROM_PWD) #logging into the email account
mail.select('inbox') #select the inbox label to read the email


#Searching mails in inbox
type, data = mail.search(None, 'ALL')  
mail_ids = data[0] #return a list of ids for each email in the account
id_list = mail_ids.split()

#Using the first email id and last email id,
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])
#iterate through the email list and fetch each email's subject and header

for i in range(latest_email_id, first_email_id, -1):
            
    #iterate through the email and fetch the email with a particular id
    #fetch the email using RFC822 protocol
    typ, data = mail.fetch(i, '(RFC822)') # i is the email id
    #print('Message %s\n%s\n' % (i,data[0][1]))
    

    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            email_subject = msg['subject']
            email_from = msg['from']
            email_body = msg['body']
            
            print('From : ' + email_from + '\n')
            print('Subject : ' + email_subject + '\n')
            print('Body : ' + email_body + '\n')

#this all works! Now we just need to be able to search for emails with the RockBlock subject, get the body of the email, and parse it.

