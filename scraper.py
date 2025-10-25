from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def get_retweet_count(tweet_url):
    # 设置正确的 ChromeDriver 路径
    driver_path = r"C:\Users\cat\Downloads\chromedriver-win64\chromedriver.exe"  # 请确保路径正确

    # 创建 Service 对象
    service = Service(driver_path)

    # 初始化 WebDriver
    driver = webdriver.Chrome(service=service)

    # 打开指定的 Twitter URL
    driver.get(tweet_url)

    # 等待页面加载
    time.sleep(3)

    retweet_count = None  # 初始化 retweet_count

    try:
        # 定位到转发数的元素（请根据需要调整 XPATH）
        retweet_element = driver.find_element(By.XPATH, '//div[@data-testid="retweet"]//span')
        retweet_count = retweet_element.text  # 获取转发数
        print(f"转发数: {retweet_count}")
    except Exception as e:
        print(f"获取转发数时发生错误: {e}")
        retweet_count = "无法获取转发数"  # 错误时赋予默认值

    # 关闭浏览器
    driver.quit()

    return retweet_count
