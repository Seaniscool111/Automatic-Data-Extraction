# Brocks Club Data Extraction
This project is a Python-based web scraper that collects club information from the Brock University BUSU clubs website. It uses BeautifulSoup to parse HTML content and extracts relevant data such as club names, emails, and club page URLs, which are then stored in an Excel file.

## Description
The script scrapes the Brock BUSU clubs directory and automatically visits each club’s page to gather available contact information. The extracted data is saved into an Excel (.xlsx) file, with built-in duplicate protection and autosaving to prevent data loss during long runs.

This project demonstrates practical web scraping, data cleaning, and file handling using Python.

## Features
Scrapes all Brock BUSU club pages
Extracts:
- Club name
- Contact email (if available)
- Club page URL
- Saves results to an Excel file (BrockClubs.xlsx)
- Prevents duplicate entries

## Technologies Used
- Python
- BeautifulSoup
- Requests
- OpenPyXL
