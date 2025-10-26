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
        # 使用集合(set)去重文本
        div_texts = set()  # 存储 div 元素的文本
        span_texts = set()  # 存储 span 元素的文本

        # 获取所有 div 元素的文本
        div_elements = driver.find_elements(By.TAG_NAME, 'div')
        for div in div_elements:
            div_texts.add(div.text)

        # 获取所有 span 元素的文本
        span_elements = driver.find_elements(By.TAG_NAME, 'span')
        for span in span_elements:
            span_texts.add(span.text)

        # 打印去重后的 div 和 span 元素的文本
        print("=== 打印去重后的 div 元素的文本 ===")
        for text in div_texts:
            print(text)

        print("=== 打印去重后的 span 元素的文本 ===")
        for text in span_texts:
            print(text)

    except Exception as e:
        print(f"发生错误: {e}")

    finally:
        # 关闭浏览器
        driver.quit()

# 示例推文 URL，请替换为实际推文链接
tweet_url = "https://x.com/dramaDIVE_ytv/status/1981567801405161653"  # 替换为实际的推文链接
print_elements(tweet_url)
