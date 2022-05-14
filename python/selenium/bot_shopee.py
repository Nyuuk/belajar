from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def SetupSelenium():
    ### Inisialisasi awal
    binary = FirefoxBinary('/usr/lib/firefox/firefox-bin')
    selenium=f'/usr/lib/firefox/geckodriver'
    ### Setup Profile
    firefox_profile = webdriver.FirefoxProfile('/home/adnan/.firefox/profile')
    browser = webdriver.Firefox(executable_path=selenium,firefox_binary=binary,firefox_profile=firefox_profile)
    ### clear cache & cookie
    #browser.delete_all_cookies()
    return browser

def InputData():
    global link_produk
    link_produk=input('(#) Link produk shopee : ')


def Click(browser, element_css):
    WebDriverWait(browser, 60).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, element_css))
        )
    WebDriverWait(browser, 60).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, element_css))
        )
    browser.find_element_by_css_selector(element_css).click()


InputData()
browser=SetupSelenium()
wait = WebDriverWait(browser, 60)
# cek udh login
browser.get("https://shopee.co.id/buyer/login")
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.shopee-avatar')))
# ke Link pembelian
browser.get(link_produk)
# tombol Beli Sekarang
click(browser, 'button.btn--l:nth-child(2)')
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.action-toast'))
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.action-toast'))
           )
# Checkout
Click(browser, '._3zK-FN')
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.loading-spinner-popup')))
# Payment
Click(browser, '.checkout-payment-setting__payment-methods-tab > span:nth-child(3) > button:nth-child(1)')
Click(browser, '.stardust-radio--checked > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
