from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup  

#Here we are using BrightData to handel the Website Captions and other issues

AUTH = 'brd-customer-hl_5be43c60-zone-ai_scraper:m11piw14702z' #brightdata link
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_website(website):
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
    return html

if __name__ == '__main__':
    website_url = 'https://example.com'
    scrape_website(website_url)

# Extracting the body content from the url and returning it and also parsing
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

#cleaning the body content by removing the script and style text
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,"html.parser")
    
    for script_or_style in soup(["script","styles"]):
        script_or_style.extract()
        
    cleaned_content = soup.get_text(separator="\n") # seperating the lines with \n caracter
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip() # if a whole line only has \n then remove it
    )
    return cleaned_content

def split_dom_content(dom_content,max_length = 6000): #splitting the cntent of max 6000 characters
    return  [
        dom_content[i:i+max_length] for i in range(0,len(dom_content),max_length)
    ]