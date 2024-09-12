import magic
import os

# Function to extract metadata from a file
def extract_metadata(file_path):
    if not os.path.exists(file_path):
        return "File not found."

    try:
        # Extract metadata using python-magic
        file_type = magic.from_file(file_path)
        file_size = os.path.getsize(file_path)

        return {
            "File Type": file_type,
            "File Size": f"{file_size / 1024:.2f} KB",
            "File Path": file_path
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    file_path = input("Enter file path to extract metadata: ")
    metadata = extract_metadata(file_path)
    print(metadata)
