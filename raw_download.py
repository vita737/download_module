# Features : Faster than featured download, don't show file progress anyway, downloads actual content when failed

import requests, time
s=time.time()
r=requests.get('http://212.183.159.230/100MB.zip',stream=True)
op=open('new.zip','wb')
for i in r.iter_content(chunk_size=1024):
    op.write(i)
e=time.time()
print(e-s)
