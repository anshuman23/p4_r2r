import re
import os

output = os.popen('sudo docker ps -a| grep "p4app_"').read()

re1='.*?'
re2='(?:[a-z][a-z0-9_]*)'
re3='.*?'
re4='(?:[a-z][a-z0-9_]*)'
re5='.*?'
re6='(?:[a-z][a-z0-9_]*)'
re7='.*?'
re8='(?:[a-z][a-z0-9_]*)'
re9='.*?'
re10='(?:[a-z][a-z0-9_]*)'
re11='.*?'
re12='(?:[a-z][a-z0-9_]*)'
re13='.*?'
re14='(?:[a-z][a-z0-9_]*)'
re15='.*?'
re16='(?:[a-z][a-z0-9_]*)'
re17='.*?'
re18='(?:[a-z][a-z0-9_]*)'
re19='.*?'
re20='(?:[a-z][a-z0-9_]*)'
re21='.*?'
re22='(?:[a-z][a-z0-9_]*)'
re23='.*?'
re24='((?:[a-z][a-z0-9_]*))'


container_name = ''

rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22+re23+re24,re.IGNORECASE|re.DOTALL)
m = rg.search(output)
if m:
    container_name = str(m.group(1))

else:
    print "[ERROR] Run this script only after you have run the p4app for scrambler.p4app"

os.system('sudo docker cp docker/scripts/send.py ' + container_name + '://scripts/') 
os.system('sudo docker cp docker/scripts/receive.py ' + container_name + '://scripts/')

print "Operation successful"
