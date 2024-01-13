"""! @ru_brief Интерфейс SMTP электропочты

 @section libs imports:
  - smtplib 
  - email.mime.text 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

# Import necessary modules

import smtplib
from email.mime.text import MIMEText

#
#
#TODO: перенести все пароли в venv
#
#from global_settings import connection_ftp as _connection

#_connection: dict = {'server': connection_ftp['server'],
#                     'port': connection_ftp['server'],
#                     'user': connection_ftp['server'],
#                     'password': connection_ftp['password']}



def send(subject: str = '', body: str = '', to='one.last.bit@gmail.com'):
    """!
    @ru_brief Функция отправляет электронное письмо, используя SMTP-сервер.

    @en_details 
    This function sends an email using the SMTP server specified in the 
    _connection dictionary. The email subject, body and recipient can be 
    customized. If an error occurs, it is logged to the logger and False 
    is returned.
    
    @param
    - subject `str`  :  the subject line of the email (default: '')
    - body `str`  :  the body of the email (default: '')
    - to `str`  :  the email address of the recipient (default: 'one.last.bit@gmail.com')
    
    @returns
    - bool: True if the email was sent successfully, False otherwise
    """
    try:
        # Create an instance of the SMTP class and connect to the server
        smtp = smtplib.SMTP(_connection['server'], _connection['port'])
    except Exception as ex:
        # Log the error and return False if a connection couldn't be established
        logger.error(f'''
    ------------------------------------------------
        Ошибка отправки почты
        subject = {subject}
       -------
        body = {body}
       -----------------
       {ex.with_traceback(ex.__traceback__)}
    -----------------------------------------------
        ''')
        return False

    # Start the SMTP connection
    smtp.ehlo()

    # Enable encryption
    tls = smtp.starttls()
    logger.info(tls)

    # Login to the SMTP server using the specified credentials
    smtp.login(_connection['user'], _connection['password'])

    # Create a MIME message with the specified subject, body and recipient
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = _connection['user']
    message["To"] = _connection['receiver']

    # Send the email and quit the SMTP connection
    smtp.sendmail(_connection['user'], to, message.as_string())
    smtp.quit()

    # Return True to indicate success
    return True
