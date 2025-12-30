import hashlib

# text = "Hello World!"
# hash_object = hashlib.sha256(text.encode())
# hash_digest = hash_object.hexdigest()
# print("SHA Hash of ", text, " is ", hash_digest)

def hash_file(file_path):
	h = hashlib.new("sha256")
	with open(file_path, "rb") as file:
		while True:
			chunk = file.read(1024)
			if chunk == b"":
				break
			h.update(chunk)
	return h.hexdigest()
	
def verify_integrity(file1, file2):
	hash1 = hash_file(file1)
	hash2 = hash_file(file2)
	print("\nChecking integrity between ", file1, " and ", file2)
	if hash1 == hash2:
		return "File is intact. No modifications have been made."
	return "File has been modified. Possibly unsafe."
	
if __name__ == "__main__":
	print("SHA hash of file is: ", hash_file(""))# To test, put the file path of the file inside the empty string
	print(verify_integrity("", ""))# To test, put the file paths of the files inside the empty strings
	print(verify_integrity("", ""))# To test, put the file paths of the files inside the empty strings
