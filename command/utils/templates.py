import os

def get_template_path(path):
	file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
	print(file_path)
	if not os.path.isfile(file_path):
		raise Exception("The file does not exist")
	return file_path

def get_template_plain():
	file_path = get_template_path("templates/email.txt")
	return open(file_path).read()

def render_context_plain(context):
	return get_template_plain().format(**context)

