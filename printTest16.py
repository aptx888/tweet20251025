#定时尝试
import pandas as pd
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 配置并启动 WebDriver
def start_driver():
    driver_path = ChromeDriverManager().install()  # 自动获取 ChromeDriver 路径
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

def start_printing(tweet_url, output_file='output.csv'):
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

    # 将数据保存到 CSV 文件
    save_to_csv(collected_text, output_file)

def save_to_csv(data, output_file):
    # 如果文件存在，打开并读取数据
    try:
        # 读取现有的数据
        df = pd.read_csv(output_file)
    except FileNotFoundError:
        # 如果文件不存在，创建一个新的 DataFrame
        df = pd.DataFrame(columns=["Extracted Data"])

    # 将新数据添加到 DataFrame 中
    new_row = pd.DataFrame({"Extracted Data": [data]})
    df = pd.concat([df, new_row], ignore_index=True)

    # 将更新后的数据保存回 CSV 文件
    df.to_csv(output_file, index=False)

    print(f"数据已保存到 {output_file}")

# 设置定时任务，每隔 30 分钟运行一次
def job():
    tweet_url = 'https://x.com/dramaDIVE_ytv/status/1981567801405161653'  # 填入目标推文 URL
    start_printing(tweet_url, output_file='output.csv')

# 每 30 分钟运行一次任务
schedule.every(30).minutes.do(job)

# 让程序一直运行以便执行定时任务
while True:
    schedule.run_pending()  # 执行所有待处理的任务
    time.sleep(1)  # 每秒钟检查一次任务是否到期
