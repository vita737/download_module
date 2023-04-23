import sys
import requests
def main(link,name):
	response = requests.get(link, stream=True)
	total_length = response.headers.get('content-length')
	dl = 0
	total_length = int(total_length)
	f=open("new.zip",'wb')
	for data in response.iter_content(chunk_size=4096):
		dl += len(data)
		f.write(data)
		done = int(100 * dl / total_length)
	print(done)
	
in1=input('link:')
in2=input("name")

main(in1,in2)