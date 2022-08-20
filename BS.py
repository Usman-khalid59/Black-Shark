import requests as rt
target=input('enter')
url="https://raw.githubusercontent.com/maurosoria/dirsearch/master/db/dicc.txt"
data=rt.get(url)
r=data.text
li=r.split('\n')
for i in li:
    final=target+"/"+i
    req=rt.get(final)
    scode=req.status_code
    if scode !=404:
        print(final,f"[status: {scode}]")
    if i == li[-1]:
        print('finished')
