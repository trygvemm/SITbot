import  pyautogui
import time
import smtplib
from email.mime.text import MIMEText

previous_color = None
def send_email():
        fromaddr = 'trygvisbot@gmail.com'
        toaddrs  = 'tehenri@gmail.com'
        msg = MIMEText('Få opp farten og bestill!')
        msg['Subject'] = 'SIT ledig'
        msg['From'] = fromaddr
        msg['to'] = toaddrs

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('trygvisbot@gmail.com', 'tyewxvltcqdsktzm') # Dont look here. Private password
            smtp.sendmail(fromaddr, toaddrs, msg.as_string())
            print('sent')
    
while True:
    pyautogui.click(86, 84)
    time.sleep(60*5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((438,545))
    
    if previous_color != None and pixel_color != previous_color:
        print('SIT ledig')
        send_email()
    
    previous_color = pixel_color
    


    