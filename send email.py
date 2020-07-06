def sentmail(message):
	import smtplib 

	from_addr = '810096@stu.nknush.kh.edu.tw'
	to_addr = '810096@stu.nknush.kh.edu.tw'

	smtpssl=smtplib.SMTP_SSL("smtp.gmail.com", 465) 
	smtpssl.login(from_addr, "XXXXXXXXX")

	msg = 'Subject:Python Sent Mail \n'
	msg += message

	smtpssl.sendmail(from_addr, to_addr, msg, mail_options=(), rcpt_options=())
	smtpssl.quit()

	
import requests, json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time


while True:
    response = requests.get('https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json', verify=False)


    sites = response.json()
    for site in sites:
        if site['Site'] == '關山':
           sentmail('PM2.5='+site['PM25'])
           break
    time.sleep(10)
