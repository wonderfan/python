import scrapy
from scrapy.selector import Selector
from scrapy.mail import MailSender

class MySpider(scrapy.Spider):
    name = 'yahoo.com'
    allowed_domains = ['yahoo.com']
    start_urls = ['http://www.yahoo.com']

    def parse(self,response):
        self.log("A response is from msn site")
#        selector = Selector(response=response)
#        print selector.xpath('//a/@href').extract()
        self.send_mail(response.body,'Finane News')
        self.log('send the email successfully')
    
    def send_mail(self, message,subject):
        print "Sending mail..........."
        import smtplib
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText
        from email.MIMEBase import MIMEBase
        from email import Encoders
        
        gmailUser = 'TBD'
        gmailPassword = 'TBD'
        recipient = 'TBD'

        msg = MIMEMultipart()
        msg['From'] = gmailUser
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText('This is the latest news'))
        
        part = MIMEBase('application', "octet-stream")
        part.set_payload(message)
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % 'finance.html')
        msg.attach(part)
        

        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmailUser, gmailPassword)
        mailServer.sendmail(gmailUser, recipient, msg.as_string())
        mailServer.close()
        print "Mail sent"
  
