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

# 打印包含 "件の表示" 到 "Xを使ってみよう" 的文本
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

        # 标志位，指示是否开始打印
        start_printing = False
        printed_content = set()  # 用于避免重复打印内容

        print("=== 开始打印相关文本 ===")

        # 遍历 div 元素
        for div in div_elements:
            div_text = div.text
            # 判断是否包含 "件の表示" 开始打印
            if "件の表示" in div_text and div_text not in printed_content:
                start_printing = True  # 开始打印
                printed_content.add(div_text)  # 添加已打印内容
                print(div_text)  # 打印第一次出现的内容
                break  # 找到 "件の表示" 后退出，避免重复

        # 遍历 span 元素
        for span in span_elements:
            span_text = span.text
            # 如果开始打印且该内容未打印过，则继续打印相关内容
            if start_printing and span_text not in printed_content:
                print(span_text)  # 打印每个元素的文本
                printed_content.add(span_text)  # 添加已打印内容

            # 一旦遇到 "Xを使ってみよう"，停止打印
            if "Xを使ってみよう" in span_text:
                print("=== 达到终止条件，停止打印 ===")
                break  # 找到终止条件后停止打印

    except Exception as e:
        print(f"发生错误: {e}")

    finally:
        # 关闭浏览器
        driver.quit()

# 示例推文 URL，请替换为实际推文链接
tweet_url = "https://x.com/dramaDIVE_ytv/status/1981567801405161653"  # 替换为实际的推文链接
print_elements(tweet_url)
