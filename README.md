# Web Scraper and File Downloader

This project is a web scraper built with Python that retrieves HTML content from a given website, lists all paths and links, and can download specified files from the website.

## Features

- **Fetch Website Content**: Downloads the HTML content of a website using the `requests` library.
- **List Paths**: Extracts and lists URL paths from the website.
- **List Links**: Prints full links that match the base URL of the website.
- **Download Files**: Downloads a file from a URL and saves it to a specified folder.

## Requirements

Before running the project, ensure you have the following dependencies installed:

- `requests`
- `beautifulsoup4`

You can install them using `pip`:

```bash
pip install requests beautifulsoup4
