import requests # HTTP library to send HTTP request
import os # Module to use operating system dependent functionality
import sys


def download_new_file(file_url, file_name):
	print('Downloading a new file')
	try:
		response = requests.get(file_url, stream=True)
		for x in response.iter_content(chunk_size=1024): #  iterate over each bit in response.content, chunk_size tells how much to put in memory at once 
			open(file_name,'ab').write(x) # create the file, write to it binary from the url, stream=true meanswrite directly	
		if sys.getsizeof(open(file_name,'rb').read()) == response.headers['Content-Length']: # if full file is downloaded
			print("\nsuccessfully downloaded !")
		else:
			print("Failed, Possibly because the network has gone.")			
	except Exception as error:
		if type(error).__name__ == 'SSLError': # check error name
			print('SSLError: Possibly because network is not being distributed properly, try closing all your network consuming software.')


def start_download():
	global file_url_input, file_name_input
	file_url_input = input('Enter the file www url: ')
	file_name_input = input('Enter the file name in local storage: ')
	download_new_file(file_url_input, file_name_input)

start_download() # do it
