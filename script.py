import subprocess

class VPNAPI:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        # Connect to VPN server
        subprocess.run(["openvpn", "--remote", self.host, "--port", str(self.port), "--auth-user-pass", f"{self.username}\n{self.password}"])

    def disconnect(self):
        # Disconnect from VPN server
        subprocess.run(["pkill", "openvpn"])
