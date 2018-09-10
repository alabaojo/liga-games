from fabric import Connection, task

def deploy():
    c = Connection(host='web1', user='deploy', port=2202);


	