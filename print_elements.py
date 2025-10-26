from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# 配置并启动 WebDriver
def start_driver():
    # 使用 webdriver-manager 自动下载并管理 ChromeDriver
    driver_path = ChromeDriverManager().install()  # 自动获取 ChromeDriver 路径
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    return driver


# 打印页面中所有的 div 和 span 元素
def print_elements(tweet_url):
    # 启动浏览器并打开页面
    driver = start_driver()

    # 打开推特推文页面
    driver.get(tweet_url)

    # 等待页面加载完成（根据需要增加等待时间）
    time.sleep(5)  # 等待5秒钟确保页面完全加载

    try:
        # 打印所有 div 元素的文本
        div_elements = driver.find_elements(By.TAG_NAME, 'div')
        print("=== 打印所有 div 元素的文本 ===")
        for div in div_elements:
            print(div.text)

        # 打印所有 span 元素的文本
        span_elements = driver.find_elements(By.TAG_NAME, 'span')
        print("=== 打印所有 span 元素的文本 ===")
        for span in span_elements:
            print(span.text)

    except Exception as e:
        print(f"发生错误: {e}")

    finally:
        # 关闭浏览器
        driver.quit()


# 请替换成你要检查的推特推文的 URL
if __name__ == "__main__":
    tweet_url = "https://x.com/dramaDIVE_ytv/status/1981567801405161653"  # 在这里输入你要检查的推文链接
    print_elements(tweet_url)
