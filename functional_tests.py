from selenium import webdriver  # (1)

browser = webdriver.Chrome()  # (2)
browser.get('http://localhost:8000')  # (3)

assert 'Django' in browser.page_source  # (4)
