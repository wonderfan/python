import envoy

def main():
    repo = 'git@github.com:wonderfan/python.git'
    envoy.run('git clone '+ repo)
    cwd = "python"
    envoy.run("rm -f wonderfan.py",cwd=cwd)
    envoy.run("git add * ",cwd=cwd)
    envoy.run('git commit -m "this is test"',cwd=cwd)
    envoy.run("git push origin master")
    

if __name__ == '__main__':
    main()
