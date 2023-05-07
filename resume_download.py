import requests # HTTP library to send HTTP request
import os # Module to use operating system dependent functionality
def resume_download(file_url, file_name):
	file_byte = os.path.getsize(file_url) # Get the size of file downloading to get continuation location
	resume_download_header = {'Range':'bytes='+file_byte+'-'} # The Range HTTP request header indicates the part of a document that the server should return Range: <unit>=<range-start>-
	open(file_name,'ab').write(requests.get(file_url,headers=resume_download_header, stream= True).content) # create the file, append to it binary from the url, stream=true means write directly, headers specify additional data for requests

def start_resume():
	file_url_input2 = input('Enter the file www url: ')
	file_name_input2 = input('Enter the file name in local storage: ')
	download_new_file(file_url_input2, file_name_input2)

i = 0
while True: # Run loop until everything is right
	i+=1 # increase everytime
	if i != 3: 
		try:
			start_resume() # do it
		except:
			start_resume() # if error resume from here
	if i ==3:
		print('3 times failed')
		break # after 3 try end program