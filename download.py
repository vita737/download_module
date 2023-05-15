import requests # HTTP library to send HTTP request
import os # Module to use operating system dependent functionality

print('Akshat Command Line Tool\nUse this tool to download files')

def download_new_file(file_url, file_name):
	print('Downloading a new file')
	try:
		open(file_name,'wb').write(requests.get(file_url, stream = True).content) # create the file, write to it binary from the url, stream=true meanswrite directly
	except requests.exceptions.ConnectionError: # if net error from start
		print("Network error, you may not have internet")
	except requests.exceptions.ChunkedEncodingError:
		print('Network suddenly stoped working')
		resume_download(file_url_input, file_name_input)
	else:
		print("successfully downloaded !")

def start_download():
	global file_url_input, file_name_input
	file_url_input = input('Enter the file www url: ')
	file_name_input = input('Enter the file name in local storage: ')
	download_new_file(file_url_input, file_name_input)

def resume_download(file_url, file_name):
	file_byte = os.path.getsize(file_name) # Get the size of file downloading to get continuation location
	resume_download_header = {'Range':'bytes='+file_byte+'-'} # The Range HTTP request header indicates the part of a document that the server should return Range: <unit>=<range-start>-
	open(file_name,'ab').write(requests.get(file_url,headers=resume_download_header, stream = True).content) # headers specify additional data for requests
def start_resume():
	file_url_input2 = input('Enter the file www url: ')
	file_name_input2 = input('Enter the file name in local storage: ')
	download_new_file(file_url_input2, file_name_input2)


start_download() # do it
