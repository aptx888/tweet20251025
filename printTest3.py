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

# 打印包含 "件の表示" 的文本及其周围内容
def print_elements(tweet_url):
    # 启动浏览器并打开页面
    driver = start_driver()

    # 打开推特推文页面
    driver.get(tweet_url)

    # 等待页面加载完成（根据需要增加等待时间）
    time.sleep(5)  # 等待5秒钟确保页面完全加载

    try:
        # 获取所有 div 和 span 元素
        div_elements = driver.find_elements(By.TAG_NAME, 'div')
        span_elements = driver.find_elements(By.TAG_NAME, 'span')

        # 查找包含 "件の表示" 的元素
        print("=== 查找并打印包含 '件の表示' 的内容 ===")

        # 先查找 div 元素中是否包含 "件の表示"
        for div in div_elements:
            if "件の表示" in div.text:
                print("=== 找到的 div 元素 ===")
                print(div.text)

        # 查找 span 元素中是否包含 "件の表示"
        for span in span_elements:
            if "件の表示" in span.text:
                print("=== 找到的 span 元素 ===")
                print(span.text)

    except Exception as e:
        print(f"发生错误: {e}")

    finally:
        # 关闭浏览器
        driver.quit()

# 示例推文 URL，请替换为实际推文链接
tweet_url = "https://x.com/dramaDIVE_ytv/status/1981567801405161653"  # 替换为实际的推文链接
print_elements(tweet_url)
