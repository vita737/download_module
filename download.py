import requests # HTTP library to send HTTP request
import os # Module to use operating system dependent functionality
import time
print('Akshat Command Line Tool\nUse this tool to download files')

def download_new_file(file_url, file_name):
	print('Downloading a new file')

	open_file_to_write_bin=open(file_name,'wb')
	try:
		response = requests.get(file_url, stream=True) # get headers and prepare file to download we accessed
	except requests.exceptions.ConnectionError: # if net error from start
		print("Network error, you may not have internet")
	except requests.exceptions.ChunkedEncodingError: # if net not working at middle
		print('Network suddenly stoped working')
	else:
		for x in response.iter_content(chunk_size=1024): # loop after 1024 bytes
			open_file_to_write_bin.write(x) # create the file, write to it binary from the url, stream=true meanswrite directly
			
		print("successfully downloaded !")


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
	download_new_file(file_url_input2, file_name_input2)

in1=int(input("Enter 1 or 2 for download or resume: "))
if in1 == 1:
	start_download() # do it
if in1==2:
	start_resume()
