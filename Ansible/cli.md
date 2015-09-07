ansible localhost --check --connection=local --inventory-file=hosts --list-hosts --module-name=setup

ansible-playbook --check --inventory-file=hosts task.yml
