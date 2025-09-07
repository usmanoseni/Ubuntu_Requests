import requests
import os
import uuid
from urllib.parse import urlparse

# funtion code to get the image url


def image_url():
    print(f"Welcome user to our program instruction:")
    img_url = input("Enter the URL of you image : ")

    # create a directory to save images if it doesn't exist
    os.makedirs("images", exist_ok=True)
    try:
        response = requests.get(img_url)
        response.raise_for_status()  # Check if the request was successful

        # Extract the file extension from the URL
        parsed_url = urlparse(img_url)
        file_name = os.path.basename(parsed_url.path)
        file_extension = os.path.splitext(file_name)[1]

        if not file_extension:
            file_extension = '.jpg'  # Default to .jpg if no extension found

        # Generate a unique filename using UUID
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join("images", unique_filename)

        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Image successfully downloaded and saved as {unique_filename}")
        print(f"Image successfully downloaded and saved in {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image. Error: {e}")


if __name__ == "__main__":
    image_url()
