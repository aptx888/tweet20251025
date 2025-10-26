#功能清单：
#用 Selenium 抓取网页数据（取“件の表示”首次出现及其后30个字符）。
#获取抓取时的当前时间。
#追加写入 Excel 文件（保留已有数据，索引在 A 列，时间在 B 列，抓取数据在 C 列）。
#数据保存成 Excel 表格（可以在 Excel 中修改，图表自动更新）。
#横轴使用时间列，折线图可显示非固定时间间隔的数据变化。




import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import os

# -----------------------
# 配置并启动 WebDriver
# -----------------------
def start_driver():
    driver_path = ChromeDriverManager().install()  # 自动获取 ChromeDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

# -----------------------
# 抓取网页数据
# -----------------------
def fetch_data(tweet_url):
    driver = start_driver()
    driver.get(tweet_url)
    time.sleep(5)  # 等待页面加载，可根据网络情况调整

    collected_text = ""
    try:
        all_elements = driver.find_elements(By.XPATH, "//div | //span")
        for element in all_elements:
            text = element.text.strip()
            if "件の表示" in text:
                start_index = text.index("件の表示")
                collected_text = text[start_index:start_index + 30]
                break
    except Exception as e:
        print(f"抓取错误: {e}")
    finally:
        driver.quit()

    return collected_text

# -----------------------
# 保存数据到 Excel
# -----------------------
def save_to_excel(data, output_file='output.xlsx'):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_row = {"Time": now, "Data": data}

    # 如果文件存在，则读取已有数据并追加
    if os.path.exists(output_file):
        df = pd.read_excel(output_file, engine='openpyxl')
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])

    # 保存为 Excel，索引作为编号（A列）
    df.to_excel(output_file, index=True, index_label="Index", engine='openpyxl')
    print(f"数据已保存到 {output_file}")

# -----------------------
# 主函数
# -----------------------
def main():
    tweet_url = "https://x.com/dramaDIVE_ytv/status/1981567801405161653"  # 输入推文网址
    if not tweet_url:
        print("未输入网址，程序退出")
        return

    data = fetch_data(tweet_url)
    if data:
        print("=== 抓取到的数据 ===")
        print(data)
        print("=====================")
        save_to_excel(data)
    else:
        print("未抓取到数据")

# -----------------------
# 执行入口
# -----------------------
if __name__ == "__main__":
    main()
