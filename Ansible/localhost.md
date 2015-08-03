ansible all -i "localhost," -c local -m shell -a 'echo hello world'

ansible-playbook -i "localhost," -c local helloworld.yml

/etc/ansible/hosts => localhost ansible_connection=local

ansible-playbook -i inventory vim.yml
