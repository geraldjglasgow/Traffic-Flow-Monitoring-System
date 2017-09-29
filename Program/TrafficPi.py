from tkinter import Tk, Label, Button
import os
from paramiko import client

class ssh:
    client = None

    def __init__(self, address, username, password):
        print ("connecting")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(address, username=username, look_for_keys=True)

    def send_command(self, command):
        if self.client:
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                if stdout.channel.recv_ready():
                    all_data = stdout.channel.recv(1024)
                    prev_data = b"1"
                    while prev_data:
                        prev_data = stdout.channel.recv(1024)
                        all_data += prev_data
                    print (str(all_data, "utf8"))
        else:
            print ("connection not open")

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.minsize(width=600, height=400)
        master.title("A simple GUI")

        self.label = Label(master, text="Traffic Pi")
        self.label.pack()

        self.greet_button = Button(master, text="Get Data", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        #x = os.popen("/sbin/ifconfig en0 | grep -w inet | awk '{print $2}'").read()
        #print(type(x))
        #print(x == "192.168.1.106")
        device = "pi@10.0.0.200"
        hostdir = "/Users/SSLGhost/Desktop"
        battery = "/home/pi/Project/Battery/battery.log"
        button = "/home/pi/Project/Buttons/button.log"
        probe = "/home/pi/Project/probe-finder/output.log"
        temp = "/home/pi/Project/Temperature/cputemp.log"
        os.system('scp "%s:%s " "%s"' % (device, battery, hostdir))
        os.system('scp "%s:%s " "%s"' % (device, button, hostdir))
        os.system('scp "%s:%s " "%s"' % (device, probe, hostdir))
        os.system('scp "%s:%s " "%s"' % (device, temp, hostdir))
        conn = ssh("10.0.0.200", "pi", "")
        conn.send_command("rm " + battery)
        conn.send_command("rm " + button)
        conn.send_command("rm " + probe)
        conn.send_command("rm " + temp)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()