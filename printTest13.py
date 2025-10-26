#重改。只打印第一次出现 件の表示 及其之后的30个字符
#这次输出的内容精简多了


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 配置并启动 WebDriver
def start_driver():
    driver_path = ChromeDriverManager().install()  # 自动获取 ChromeDriver 路径
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

def start_printing(tweet_url):
    # 启动浏览器并打开页面
    driver = start_driver()

    # 打开推文页面
    driver.get(tweet_url)

    # 等待页面加载完成
    time.sleep(5)  # 可以根据网络情况调整等待时间

    # 初始化数据收集变量
    start_printing = False
    collected_text = ""

    try:
        # 遍历页面上的所有 div 和 span 元素
        all_elements = driver.find_elements(By.XPATH, "//div | //span")

        for element in all_elements:
            text = element.text.strip()

            # 查找第一次出现 "件の表示"
            if "件の表示" in text and not start_printing:
                start_printing = True
                # 截取 "件の表示" 后的30个字符
                start_index = text.index("件の表示")
                collected_text = text[start_index:start_index + 30]

            # 如果已经找到并收集了内容，就停止继续遍历
            if start_printing and collected_text:
                break

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭浏览器
        driver.quit()

    # 打印收集到的内容
    print("=== 开始打印相关文本 ===")
    print(collected_text)
    print("=== 达到终止条件，停止打印 ===")


# 例如你调用的推文 URL
tweet_url = "https://x.com/dramaDIVE_ytv/status/1981567801405161653"  # 请替换为实际链接
start_printing(tweet_url)