#2025/10/26
#保留 pandas 的默认索引（即不加 index=False），
#并确保时间和数据列都写入

#功能如下：
#自动打开推文页面并抓取 “件の表示” 开始的内容（30个字符以内）
#自动记录当前时间
#每次运行都将数据 追加写入 CSV 文件
#A列 = 编号（自动累积，不覆盖）
#B列 = 时间戳
#C列 = 抓取到的内容



import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import os


# 启动 Chrome WebDriver
def start_driver():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    return driver


# 抓取推文中 “件の表示” 开始的部分
def start_printing(tweet_url, output_file='data.csv'):
    driver = start_driver()
    driver.get(tweet_url)
    time.sleep(5)  # 等待网页加载完毕，可根据网速调整

    start_printing = False
    collected_text = ""

    try:
        # 遍历页面上的所有 div 和 span
        all_elements = driver.find_elements(By.XPATH, "//div | //span")

        for element in all_elements:
            text = element.text.strip()

            # 找到 “件の表示” 作为锚点
            if "件の表示" in text and not start_printing:
                start_printing = True
                start_index = text.index("件の表示")
                collected_text = text[start_index:start_index + 30]

            if start_printing and collected_text:
                break

    except Exception as e:
        print(f"❌ 发生错误: {e}")
    finally:
        driver.quit()

    print("=== 开始打印相关文本 ===")
    print(collected_text)
    print("=== 达到终止条件，停止打印 ===")

    # 保存结果到 CSV
    save_to_csv(collected_text, output_file)


# 保存数据到 CSV 文件（带时间、自动编号、可追加）
def save_to_csv(data, output_file):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_row = {"Time": timestamp, "Data": data}

    if os.path.exists(output_file):
        # 读取已有文件并追加
        df = pd.read_csv(output_file, encoding='utf-8-sig')
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        # 第一次创建
        df = pd.DataFrame([new_row])

    # 索引从 1 开始
    df.index += 1

    # 写入 CSV（保留索引，不覆盖）
    df.to_csv(output_file, index=True, encoding='utf-8-sig')

    print(f"✅ 数据已保存到 {output_file}")


# 示例运行（你可以换成你自己的推文URL）
if __name__ == "__main__":
    tweet_url = "https://x.com/dramaDIVE_ytv/status/1981567801405161653"  # ← 这里换成真实推文链接
    start_printing(tweet_url)
