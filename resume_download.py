import requests # HTTP library to send HTTP request
import os # Module to use operating system dependent functionality

def resume_download(file_url, file_name):
	file_byte = os.path.getsize(file_name) # Get the size of file downloading to get continuation location
	resume_download_header = {'Range':'bytes='+str(file_byte)+'-'} # The Range HTTP request header indicates the part of a document that the server should return Range: <unit>=<range-start>-
	try:
		response =requests.get(file_url, headers=resume_download_header, stream= True)
		for x in response.iter_content(chunk_size=1024): #  iterate over each bit in response.content, chunk_size tells how much to put in memory at once 
			open(file_name,'ab').write(x) # create the file, append to it binary from the url, stream=true means write directly, headers specify additional data for requests
			if file_byte == response.headers['Content-Length']: # check lenght
				print("Downloaded successfully")
			else:
				print("Failed for some reason")
	except Exception as error:
		if type(error).__name__ == 'SSLError': # check error name
			print('SSLError: Possibly because network is not being distributed properly, try closing all your network consuming software.')

def start_resume():
	file_url_input2 = input('Enter the file www url: ')
	file_name_input2 = input('Enter the file name in local storage: ')
	resume_download(file_url_input2, file_name_input2)

start_resume()