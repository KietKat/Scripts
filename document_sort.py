import os
import shutil

# Define path to documents folder
document_file = r'C:\Users\KietN\Downloads\documents'

# document type list
document_type = {
	'pdf' : ['pdf'],
	'doc' : ['doc', 'docx', 'txt'],
	'csv' : ['csv', 'xls', 'xlsx']
}

# Join forlders of different type
for doc in document_type.keys():
	doc_path = os.path.join(document_file, doc)
	if not os.path.exists(doc_path):
		os.makedirs(doc_path)

def classify_type(file_path):
	_, ext = os.path.splitext(file_path)
	ext = ext.lower().strip('.')
	for folder, extensions in document_type.items():
		if ext in extensions:
			dest_folder = os.path.join(document_file, folder)
			shutil.move(file_path, dest_folder)
			print(f"Move {file_path} to {dest_folder}")
			break

def sort_existing_file():
	for file in os.listdir(document_file):
		file_path = os.path.join(document_file, file)
		if os.path.isfile(file_path):
			classify_type(file_path)


if __name__ == '__main__':
	sort_existing_file()