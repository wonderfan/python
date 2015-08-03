ansible all -i "localhost," -c local -m shell -a 'echo hello world'

ansible-playbook -i "localhost," -c local helloworld.yml
