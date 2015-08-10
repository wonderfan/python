import shutil,os

def main():    
    base_dir = 'C:\zenith\monitor\Deployment and Automation\chef_stuff\chef_repo\cookbooks\sce'
    os.chdir(base_dir)
    file_name = shutil.make_archive('monitor','zip',os.curdir,os.curdir+os.path.sep+'monitor')
    shutil.move(file_name,'C:\Users\IBM_ADMIN\Downloads')   

if __name__ == '__main__':
    main()
