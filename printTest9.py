#这个好多了，没重复的了，但是还是有多余的字



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
    time.sleep(5)  # 可以调整根据网络情况

    # 初始化数据收集变量
    start_printing = False
    collected_lines = []

    try:
        # 遍历页面上的所有 div 和 span 元素
        all_elements = driver.find_elements(By.XPATH, "//div | //span")

        for element in all_elements:
            text = element.text.strip()

            # 开始打印的条件：包含 "件の表示"
            if "件の表示" in text and not start_printing:
                start_printing = True
                collected_lines.append(f"=== 开始打印相关文本 ===")

            # 如果满足开始打印条件且符合文本内容，继续收集
            if start_printing:
                collected_lines.append(text)

            # 终止条件：包含 "Xを使ってみよう"
            if "Xを使ってみよう" in text and start_printing:
                collected_lines.append(f"=== 达到终止条件，停止打印 ===")
                break

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭浏览器
        driver.quit()

    # 打印所有符合条件的内容
    for line in collected_lines:
        print(line)


# 例如你调用的推文 URL
tweet_url = "https://x.com/dramaDIVE_ytv/status/1981567801405161653"  # 请替换为实际链接
start_printing(tweet_url)
