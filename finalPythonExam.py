import requests
from bs4 import BeautifulSoup
import os

# Function to get website content using Requests
# Parameters:
#   - url (str): The URL of the website to retrieve content from.
# Returns:
#   - str: The HTML content of the website if the request is successful.
#   - None: If an error occurs during the request.
def get_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve content from {url}: {e}")
        return None

# Function to list all paths on the website
# Parameters:
#   - html_content (str): The HTML content of the website.
#   - base_url (str): The base URL of the website to validate relative links.
# Returns:
#   - list: A list of all paths found on the website that start with the base URL or "/".
def list_paths(html_content, base_url):
    if html_content is None:
        return []  # Return an empty list if content is None
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    paths = []
    for link in links:
        href = link.get('href')
        if href and (href.startswith(base_url) or href.startswith('/')):
            paths.append(href)
    return paths

# Function to list all links on the website
# Parameters:
#   - html_content (str): The HTML content of the website.
#   - base_url (str): The base URL of the website to filter and print links.
# Prints:
#   - Links on the website that start with the base URL.
def list_links(html_content, base_url):
    if html_content is None:
        return
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href and href.startswith(base_url):
            print(href)

# Function to download files from the website
# Parameters:
#   - url (str): The URL of the file to download.
#   - save_folder (str): The folder to save the downloaded file.
# Downloads:
#   - Saves the file to the specified folder if the request is successful.
# Prints:
#   - Success message with the file name if downloaded.
#   - Error message if the download fails.
def download_files(url, save_folder):
    if url is None:
        return
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        file_name = os.path.join(save_folder, url.split("/")[-1])
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        
        print(f"Downloaded: {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file from {url}: {e}")

# URL of the website you want to scan
website_url = 'https://www.ecomschool.co.il/'
base_url = website_url.rstrip('/')  # Remove trailing slash

# Perform actions on the website
html_content = get_website_content(website_url)

if html_content:
    # a. List paths on the website
    print("Paths on the website:")
    paths = list_paths(html_content, base_url)
    for path in paths:
        print(path)

    # b. List all links on the website
    print("\nLinks on the website:")
    list_links(html_content, base_url)

    # c. Download files from the website (modify the URL as needed)
    file_url = 'https://www.ecomschool.co.il/somefile.pdf'
    download_folder = './downloads'  # Specify the folder to save downloaded files
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    download_files(file_url, download_folder)
