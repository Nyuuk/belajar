from selenium.webdriver.common.action_chains import ActionChains
# from argparse import Action
import pickle
import selenium
# from genericpath import exists
from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# import json
import time
from datetime import datetime
import datetime as dt
import pytz
import json
start_time = time.perf_counter()


def SetupSelenium():
    global browser
    global wait
    # Inisialisasi awal
    binary = '/home/nyuuk/Documents/project/selenium/geckodriver'
    # browser = webdriver.Firefox(executable_path=binary)
    browser = webdriver.Firefox()
    # browser.delete_all_cookies()
    # browser = SetupSelenium()
    browser.get("https://shopee.co.id/buyer/login")
    # wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.shopee-avatar')))
    Load_Cookie(browser)
    wait = WebDriverWait(browser, 160)


def InputData():
    global link_produk
    global waktu_beli
    # waktu_beli = input('(#) Waktu membeli : ')
    with open('link.json', 'r') as link:
        data = json.load(link)
        # link_produk=input('(#) Link produk shopee : ')
        link_produk = data['link']
        waktu_beli = data['time']


def Click(browser, element_css):
    WebDriverWait(browser, 60).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, element_css))
    )
    WebDriverWait(browser, 60).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, element_css))
    )
    browser.find_element(By.CSS_SELECTOR, element_css).click()


def Load_Cookie(browser):
    # if exists('cookies.pxl'):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        try:
            browser.add_cookie(cookie)
        except selenium.common.exceptions.InvalidCookieDomainException as e:
            print(e)

def InCart(browser):
    start_time = time.perf_counter()
    # ke Link pembelian
    browser.get(link_produk)
    # tombol Beli Sekarang
    # Click(browser, 'button.btn--l:nth-child(2)')
    # tombol keranjang
    Click(browser, '#main > div > div:nth-child(3) > div._3A8xof > div > div.page-product > div > div.product-briefing.flex.card._1j7uGn > div.flex.flex-auto._3qq4y7 > div > div:nth-child(5) > div > div > button.btn.btn-tinted.btn--l.rvHxix._3t_iHy')
    wait.until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, '.action-toast')))
    time_final = round(time.perf_counter()-start_time, 2)
    print('Memasukan product ke keranjang membutuhkan waktu sekitar')
    print("--- %s seconds ---" % (time_final))

def CheckOut(browser):
    global start_time
    start_time = time.perf_counter()
    browser.get('https://shopee.co.id/cart')
    # wait.until(ec.visibility_of_element_located(
        # (By.CSS_SELECTOR, '#cart_drawer_target_id > svg')
    # ))
    # Click(browser, '#cart_drawer_target_id > svg')
    # Click centang produk paling awal
    el = WebDriverWait(browser, 60).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, '._1Lgvsy > label:nth-child(1) > div:nth-child(2)')))
    browser.execute_script("arguments[0].click();", el)
    # Click(browser, '#main > div > div:nth-child(3) > div._3ojYn- > div > div:nth-child(3) > div._2REryK > div._1K9yK1 > div._1glehh > div > div > div._1Lgvsy > label > div')
    # Click Checkout
    Click(browser, '#main > div > div:nth-child(3) > div._3ojYn- > div > div:nth-child(3) > div._2qn3bA._1F9REl > div.CsNHbu.-Gs_Ma > button.shopee-button-solid.shopee-button-solid--primary')
    # wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '.loading-spinner-popup')))
    # wait.until(ec.visibility_of_element_located(
        # (By.CSS_SELECTOR, '.loading-spinner-popup')))
    # Payment
    # Click ubah metode pembayaran
    # print('Click dengan script')
    try:
        el = WebDriverWait(browser, 30).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, '._1n5Ut6')))
    except:
        # if 'document has been refreshed' in f:
        ClickPayment(browser)
    else:
        browser.execute_script("arguments[0].click();", el)
        ClickPayment(browser)
        
def ClickPayment(browser):
    global time_final
    try:
        browser.find_element(By.CSS_SELECTOR, '.loading-spinner-popup')
    except:
        print('Skip loading spinner')
    else:
        wait.until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, '.loading-spinner-popup')
            ))
    # COD
    # Click(browser, '.checkout-payment-setting__payment-methods-tab > span:nth-child(3) > button:nth-child(1)')
    # Click(browser, '.stardust-radio--checked > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
    # BCA
    print('Click bca method')
    try:
        elemnt = browser.find_element(By.CSS_SELECTOR, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div.checkout-payment-method-view__current.checkout-payment-setting > div.checkout-payment-setting__payment-methods-tab > span:nth-child(3) > button')
    except:
        print('Continue Ubah method')
    else:
        scroll_shim(browser, elemnt)
        Click(browser, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div.checkout-payment-method-view__current.checkout-payment-setting > div.checkout-payment-setting__payment-methods-tab > span:nth-child(3) > button')
    # elemnt = browser.find_element(By.CSS_SELECTOR, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div.checkout-payment-setting__payment-method-options > div:nth-child(1) > div.bank-transfer-category__body > div:nth-child(2) > div > div.stardust-radio-button > div')
    # scroll_shim(browser, elemnt)
    try:
        elemnt = browser.find_element(By.CSS_SELECTOR, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div.checkout-payment-setting__payment-method-options > div:nth-child(1) > div.bank-transfer-category__body > div:nth-child(2) > div > div.stardust-radio-button > div')
    except:
        print('Continue Centang BCA')
    else:
        scroll_shim(browser, elemnt)
        Click(browser, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div.checkout-payment-setting__payment-method-options > div:nth-child(1) > div.bank-transfer-category__body > div:nth-child(2) > div > div.stardust-radio-button > div')
    # Buat Pesanan
    elemnt = browser.find_element(By.CSS_SELECTOR, 'button.stardust-button:nth-child(2)')
    scroll_shim(browser, elemnt)
    # browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[4]/div[2]/div[9]/button').click()
    Click(browser, 'button.stardust-button:nth-child(2)')
    wait.until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, '#main > div > div:nth-child(3) > div.payment-safe-page > div > div.B6yp6Z > div._3_AQqC > div._2bBG9X > img')
        ))
    time_final = str(time.perf_counter()-start_time)[:9]
    print('CheckOut membutuhkan waktu sekitar')
    print("--- %s seconds ---" % (time_final))

def CancelLastOrder(browser):
    start_time = time.perf_counter()
    browser.get('https://shopee.co.id/user/purchase/list?type=9')
    wait.until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, '#main > div > div._193wCc > div.container._1QwuCJ > div._3D9BVC > div > div:nth-child(4) > div > div._1Qn42s > div._23TzMz._2d5VsN > div:nth-child(3) > div > div._24DixQ')
        ))
    # element = browser.find_element(By.CSS_SELECTOR, '#main > div > div._193wCc > div.container._1QwuCJ > div._3D9BVC > div > div:nth-child(4) > div > div._1Qn42s > div._23TzMz._2d5VsN > div:nth-child(3) > div > div._24DixQ')
    element = browser.find_element(By.CSS_SELECTOR, '.hONkWV')
    scroll_shim(browser, element)
    action = ActionChains(browser)
    action.move_to_element(element).perform()
    # action.move_to_element(element).click().perform()
    action.move_to_element(browser.find_element(By.CSS_SELECTOR, '#main > div > div._193wCc > div.container._1QwuCJ > div._3D9BVC > div > div:nth-child(4) > div > div._1Qn42s > div._23TzMz._2d5VsN > div:nth-child(3) > div > div._1yAmQW > button:nth-child(2)')).click().perform()
    Click(browser, '#modal > div._2IJN-0 > div._1lzg0h > div > div > div.shopee-popup-form__main > div > div:nth-child(2) > div:nth-child(7) > div.stardust-radio-button > div')
    Click(browser, '#modal > div._2IJN-0 > div._1lzg0h > div > div > div.shopee-popup-form__footer > button.btn.btn-solid-primary.btn--s.btn--inline._1wSE68')
    wait.until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, '#main > div > div._193wCc > div.container._1QwuCJ > div._3D9BVC > div > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div > div.WqnWb- > div._1lE6Rh > div')
    ))
    time_final = round(time.perf_counter()-start_time, 6)
    print('Cancel Order membutuhkan waktu sekitar')
    print("--- %s seconds ---" % (time_final))

def countdownTimer(total_second):
    while total_second:
        mins, secs = divmod(total_second, 60)
        hours, mins = divmod(mins, 60)
        print(f'{hours:02d}:{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
    print("Done!")

def waitTimeNow(browser):
    #time_final="10.45"
    tz = pytz.timezone('Asia/Jakarta')
    now = datetime.now(tz)
    deptraction_time = dt.timedelta(seconds=float(time_final))
    n_waktu_beli = datetime.strptime('%s-%s-%s %s.000000' % (now.year, now.month, now.day, waktu_beli), '%Y-%m-%d %H:%M:%S.%f')
    hasil = n_waktu_beli-deptraction_time
    InCart(browser)
    print("jumlah total waktu yang di butuhkam untuk checkout dan waktu beli adalah %s" % (hasil.strftime('%H:%M:%S.%f')))
    print('waktu sekarang adalah')
    while True:
        now = datetime.now()
        print('%s' %(now.strftime('%H:%M:%S.%f')), end='\r')
        if now >= hasil:
            CheckOut(browser)
            break

def scroll_shim(passed_in_driver, object):
        x = object.location['x']
        y = object.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
        passed_in_driver.execute_script(scroll_by_coord)
        passed_in_driver.execute_script(scroll_nav_out_of_way)

def start():
    global link_produk
    SetupSelenium()
    input('Tekan enter untuk lanjutkan')
    link_produk="https://shopee.co.id/product/21977839/6425495725?smtt=0.691695138-1645685021.10"
    InCart(browser)
    # Test hasil detik checkout
    CheckOut(browser)
    # Menghapus last Order
    CancelLastOrder(browser)
    InputData()
    waitTimeNow(browser)
    print('Berhasil')
        
# browser.quit()
# if __name__ == '__main__':
#     start()
