import envoy
from selenium import webdriver
import time

def main():
    repo = 'git@github.com:wonderfan/wonderfan.github.io.git'
    envoy.run('git clone '+ repo)
    cwd = "wonderfan.github.io"
    get_screenshot()
    envoy.run("git add --all ",cwd=cwd)
    envoy.run('git commit -m "submit the changes"',cwd=cwd)
    envoy.run("git push origin master")

def get_screenshot():
    driver = webdriver.Firefox()
    driver.get("http://www.msn.com")
    file_name = "".join(["test-",str(int(time.time())),'.png'])
    driver.save_screenshot("wonderfan.github.io/"+file_name)
    driver.close()

if __name__ == '__main__':
    main()
