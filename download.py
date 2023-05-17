# Features : Slower than raw with not much difference at small level

import requests # HTTP library to send HTTP request
import os # Module to use operating system dependent functionality
import sys
print('Akshat Command Line Tool\nUse this tool to download files')

def download_new_file(file_url, file_name):
	print('Downloading a new file')
	total=0
	open_file_to_write_bin=open(file_name,'wb') # open file to write binary
	try:
		response = requests.get(file_url, stream=True) # get headers and prepare file to download we accessed
	except requests.exceptions.ConnectionError: # if net error from start
		print("Network error, you may not have internet")
	else: # if no error
		content_len = response.headers['Content-Length'] # get total file lenght
		for x in response.iter_content(chunk_size=1024): # loop after 1024 bytes which will be loaded in memory at a time
			total+=1024	# increase downloaded file by 1024 as it iterates
			open_file_to_write_bin.write(x) # create the file, write to it binary from the url, stream=true meanswrite directly	
			if total%1024==0: # if one time next 1024 byte is downloaded
				print(str(round(100*total/int(content_len)))) # calculate download percent
				sys.stdout.write("\033[F") # erase latest line
		print("\nsuccessfully downloaded !")

def start_download():
	global file_url_input, file_name_input
	file_url_input = input('Enter the file www url: ')
	file_name_input = input('Enter the file name in local storage: ')
	download_new_file(file_url_input, file_name_input)

def resume_download(file_url, file_name):
	file_byte = os.path.getsize(file_name) # Get the size of file downloading to get continuation location
	resume_download_header = {'Range':'bytes='+str(file_byte)+'-'} # The Range HTTP request header indicates the part of a document that the server should return Range: <unit>=<range-start>-
	open(file_name,'ab').write(requests.get(file_url,headers=resume_download_header, stream = True).content) # headers specify additional data for requests

def start_resume():
	file_url_input2 = input('Enter the file www url: ')
	file_name_input2 = input('Enter the file name in local storage: ')
	resume_download(file_url_input2, file_name_input2)

in1=int(input("Enter 1 or 2 for download or resume: "))
if in1 == 1:
	start_download() # do it
if in1==2:
	start_resume()