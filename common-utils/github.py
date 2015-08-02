from github3 import login

def main():
    gh = login('account','password')
    issue = gh.issue('wonderfan', 'python', 1)
    print issue.body_html

if __name__ == '__main__':
    main()
