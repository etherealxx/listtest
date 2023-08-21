import streamlit as st
import os
import wget
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from chromedriver_py import binary_path
# import chromedriver_autoinstaller

# chromedriver_autoinstaller.install()

def list_files_recursive(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        st.write(f"{indent}[{os.path.basename(root)}/]")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            st.write(f"{sub_indent}{file}")

def scrape_data(url):
    chromedriver_path = '/mount/src/listtest/chromedriver-linux64/chromedriver'
    
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.binary_location = '/usr/bin/google-chrome'  # Path to Chrome binary on the server
    
    # service = Service(chromedriver_path)  # Set the path to Chrome WebDriver executable
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get(url)
    
    data = driver.find_element_by_xpath('/html/body/div/main/div[2]/div[2]/div[1]/h2/p').text
    # Scraping logic here
    
    driver.quit()
    return data

st.title('test')
os.makedirs('/mount/src/listtest', exist_ok=True)
chromedriver_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip"
zip_path = "/mount/src/listtest/chromedriver.zip"  # Set the desired path on the server
wget.download(chromedriver_url, zip_path)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    # Extract all contents to the target directory
    zip_ref.extractall('/mount/src/listtest')

# list_files_recursive('/mount/src/listtest')
os.chmod('/mount/src/listtest/chromedriver-linux64/chromedriver', 0o775)

# url = "https://psyteam-fc61f.web.app/"  # URL to the website you want to scrape
# data = scrape_data(url)

# st.write("Scraped Data:")
# st.write(data)

# os.system("apt-get install -y libglib2.0-0=2.50.3-2 libnss3=2:3.26.2-1.1+deb9u1 libgconf-2-4=3.2.6-4+b1 libfontconfig1=2.11.0-6.7+b1")

# Path to the ChromeDriver executable
chromedriver_path = "/mount/src/listtest/chromedriver-linux64/chromedriver"

# Set up Chrome options (you can add more options as needed)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Initialize ChromeDriver
# service = Service(binary_path)
# driver = webdriver.Chrome(service=service, options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open a website
    url = "https://github.com/lushan88a/google_trans_new"  # Replace with the URL you want to open
    driver.get(url)

    # Print the title of the webpage
    st.write("Page title:", driver.title)

finally:
    # Close the browser window
    driver.quit()