import os
import tkinter as t
from paramiko import client
import urllib.request as urllib2
import json
import codecs
from tkinter import filedialog
# import matplotlib as plt


class SSH:
    client = None

    def __init__(self, address, username):
        print("connecting")
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
                    print(str(all_data, "utf8"))
        else:
            print("connection not open")


class MyFirstGUI:

    def __init__(self, master):
        self.master = master
        master.minsize(width=600, height=400)
        master.title("Traffic Pi Data Analysis")
        self.path = "/Users/SSLGhost/Desktop/Test3/School/"
        self.user = "pi@"
        self.ip = "10.0.0.200"

        self.label = t.Label(master, text="Choose an option")
        self.label.pack()

        self.dir_button = t.Button(master, text='Browse', command=self.check_directory)
        self.dir_button.pack()

        self.displayLab = t.Label(master, text=self.path)
        self.displayLab.pack()

        self.greet_button = t.Button(master, text="Get Data", command=self.greet)
        self.greet_button.pack()

        self.process_button = t.Button(master, text="Analyze", command=self.process)
        self.process_button.pack()

        self.vendor_button = t.Button(master, text="Vendor", command=self.vendor)
        self.vendor_button.pack()

        self.match_button = t.Button(master, text="Match", command=self.match)
        self.match_button.pack()

        self.close_button = t.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        # x = os.popen("/sbin/ifconfig en0 | grep -w inet | awk '{print $2}'").read()
        battery = "/home/pi/Project/Battery/battery.log"
        button = "/home/pi/Project/Buttons/button.log"
        probe = "/home/pi/Project/probe-finder/output.log"
        temp = "/home/pi/Project/Temperature/cputemp.log"
        os.system('scp "%s%s:%s " "%s"' % (self.user, self.ip, battery, self.path))
        os.system('scp "%s%s:%s " "%s"' % (self.user, self.ip, button, self.path))
        os.system('scp "%s%s:%s " "%s"' % (self.user, self.ip, probe, self.path))
        os.system('scp "%s%s:%s " "%s"' % (self.user, self.ip, temp, self.path))
        conn = SSH(self.ip, "pi")
        conn.send_command("rm " + battery)
        conn.send_command("rm " + button)
        conn.send_command("rm " + probe)
        conn.send_command("rm " + temp)

    def process(self):
        file = open(self.path+"output.log", "r")
        y = file.readlines()
        mac_list = [i.split('\t')[1] for i in y]
        projection = set(mac_list)
        print(len(projection))
        file.close()
        # file = open("temp.txt", "a")
        # for item in projection:
        #     file.write("%s\n" % item)
        file = open(self.path+"filter1.txt", "w")
        for element in projection:
            if element[0]+element[1]+element[2]+element[3]+element[4]+element[5]+element[6]+element[7] != "":
                file.write("%s\n" % element.upper())

    def vendor(self):
        url = "http://macvendors.co/api/"
        file = open(self.path+"filter1.txt", "r")
        i = 0
        for element in file:
            mac_address = element
            request = urllib2.Request(url + mac_address, headers={'User-Agent': "API Browser"})
            response = urllib2.urlopen(request)
            reader = codecs.getreader("utf-8")
            obj = json.load(reader(response))
            try:
                print(obj['result']['company'])
                i += 1
            except KeyError:
                print("not known")
        print(i)

    def match(self):
        file = open("/Users/SSLGhost/Desktop/Test2/School/"+"filter1.txt", "r")
        file1 = file.readlines()
        file.close()
        file = open("/Users/SSLGhost/Desktop/Test2/nearRound/"+"filter1.txt", "r")
        file2 = file.readlines()
        file.close()
        i = 0
        for element in file1:
            for element1 in file2:
                if element == element1:
                    print(element)
                    i += 1
        print(i)

    def check_directory(self):

        self.filename = filedialog.askdirectory()
        self.path = self.filename
        print(self.path)
        try:
            if os.listdir(self.path):
                print("yes")
            else:
                print("no")
        except EnvironmentError:
            print("Directory Not Found")

    def graph(self):
        print("hello")


root = t.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
