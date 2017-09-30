* if ls ~/.ssh is empty run below command</br>
ssh-keygen -t rsa -C "RPi 0"


* else just add the key to the raspberry pi</br>
*make sure the pi has an /.ssh directory</br>
cd ~</br>
install -d -m 700 ~/.ssh

* Now just copy the key into authorized keys</bar>
cat ~/.ssh/id_rsa.pub | ssh pi@10.0.0.201 'cat >> .ssh/authorized_keys'