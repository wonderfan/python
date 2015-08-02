import envoy
from selenium import webdriver

def main():
    repo = 'git@github.com:wonderfan/python.git'
    envoy.run('git clone '+ repo)
    cwd = "python"
    envoy.run("rm -f wonderfan.py",cwd=cwd)
    envoy.run("git add * ",cwd=cwd)
    envoy.run('git commit -m "submit the changes"',cwd=cwd)
    envoy.run("git push origin master")

def get_screenshot():
    driver = webdriver.Firefox()
    driver.get("http://www.msn.com")
    driver.save_screenshot("test.png")
    driver.close()

if __name__ == '__main__':
    main()
