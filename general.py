import os 
def create_project_dir(directory):
	if not os.path.exists(directory):
		print("Creating Project", directory)
		os.makedirs(directory)

def create_data_files(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')


def write_file(path, data):
	with open(path, 'w') as f:
		f.write(data)

create_data_files("celtics", "https://www.basketball-reference.com/teams/BOS/2018.html")