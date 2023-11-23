import paramiko

DEFAULT_TIMEOUT = 20 * 60


class SSHPool(object):

    def __init__(self):
        self.pool = {}

    def connect(self, ip, port, username, password):
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, password)
        return ssh

    def get(self, ip, port, username, password):
        for ssh_ip, ssh_client in self.pool.items():
            if ssh_ip == ip:
                if ssh_client.get_transport() and ssh_client.get_transport(
                ).is_alive():
                    return ssh_client
                else:
                    break
            else:
                continue
        ssh = self.connect(ip, port, username, password)
        self.pool[ip] = ssh
        return ssh


class SSHClient(paramiko.SSHClient):

    def exec_command(self, command, timeout=DEFAULT_TIMEOUT):
        return super().exec_command(command, timeout=timeout)


ssh_pool = SSHPool()
