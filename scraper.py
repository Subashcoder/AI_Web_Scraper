import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def scrape_website(website):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    chrome_driver_path = 'chromedriver.exe'
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
    
    try:
        driver.get(website)
        url = driver.page_source
        time.sleep(10)
        return url
    finally:
        driver.quit()
        
def extract_body(body):
    soup = BeautifulSoup(body, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""
        
def body_text(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(['script','style']):
        script_or_style.extract()
        
    body_content = soup.get_text(separator='\n')
    cleaned_content = '\n'.join(line.strip() for line in body_content.splitlines() if line.strip())
    return cleaned_content

def split_dom_content(dom_content, max_length = 6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
        
        
    
    
        
        
