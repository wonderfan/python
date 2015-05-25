#! /usr/bin/env python

import smtplib

if __name__ == '__main__':

	print "It is is here"

	server = smtplib.SMTP_SSL('smtp.126.com', 465)
	server.set_debuglevel(1)
	#server.connect()
	print " stmp server"
	server.login("lingyun_xiang", "xiaowen198675")
	print "Log in the email"

	#Send the mail
	msg = "\nHello!" # The /n separates the message from the headers
	server.sendmail("lingyun_xiang@126.com", "xiangly@cn.ibm.com", msg)
	print "done"
	server.close()
