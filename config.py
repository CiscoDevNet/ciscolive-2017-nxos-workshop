import os

f = os.popen('mv -f /bootflash/autoconfig/adriani/running.latest /home/guestshell/ciscolive-2017-nxos-workshop/running')
who = f.read()
f.close
print "Result:", who
f = os.popen('cd /home/guestshell/ciscolive-2017-nxos-workshop; git add running')
who = f.read()
f.close
print "Result:", who
f = os.popen('cd /home/guestshell/ciscolive-2017-nxos-workshop; git commit -m "Latest change"')
who = f.read()
f.close
print "Result:", who
f = os.popen('cd /home/guestshell/ciscolive-2017-nxos-workshop; chvrf management git push')
who = f.read()
f.close
print "Result:", who
