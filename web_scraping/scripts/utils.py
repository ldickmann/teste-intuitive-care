import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def setup_logging():
    """Configura o logging."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def setup_driver():
    """Configura o driver do Selenium."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


def extract_pdf_links(driver):
    """Extrai os links dos PDFs das páginas acessadas pelo Selenium."""
    pdf_links = []
    pdf_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")

    for element in pdf_elements:
        link = element.get_attribute("href")
        if "anexo" in link.lower():
            pdf_links.append(link)

    return pdf_links
