import gmail 

def main():
    mail = gmail.login('account', 'password')
    emails = mail.inbox().mail(unread=True)
    print len(emails)
    mail.logout()
    pass

if __name__ == '__main__':
    main()
