#✅ 完整可运行版本：
#支持自动定时抓取 + 自动追加保存 + A列编号 + UTF-8 编码 + Windows/Excel兼容


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import os


# === 启动 Chrome WebDriver ===
def start_driver():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    return driver


# === 抓取推文中 “件の表示” 开始的内容 ===
def scrape_tweet(tweet_url):
    driver = start_driver()
    driver.get(tweet_url)
    time.sleep(5)  # 等待网页加载完毕，可根据网速调整

    start_printing = False
    collected_text = ""

    try:
        all_elements = driver.find_elements(By.XPATH, "//div | //span")
        for element in all_elements:
            text = element.text.strip()
            if "件の表示" in text and not start_printing:
                start_printing = True
                start_index = text.index("件の表示")
                collected_text = text[start_index:start_index + 30]
            if start_printing and collected_text:
                break
    except Exception as e:
        print(f"❌ 抓取时出错: {e}")
    finally:
        driver.quit()

    return collected_text


# === 保存数据到 CSV ===
def save_to_csv(data, output_file='data.csv'):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_row = {"Time": timestamp, "Data": data}

    if os.path.exists(output_file):
        df = pd.read_csv(output_file, encoding='utf-8-sig')
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])

    # 自动编号（索引从1开始）
    df.index += 1
    df.to_csv(output_file, index=True, encoding='utf-8-sig')
    print(f"✅ 数据已保存到 {output_file}")


# === 主循环：每隔30分钟自动运行一次 ===
def auto_run(tweet_url, interval_minutes=30, output_file='data.csv'):
    print(f"🚀 启动自动抓取程序，每隔 {interval_minutes} 分钟运行一次。")
    print("按 Ctrl + C 可手动停止。")

    while True:
        print("\n=== 开始抓取数据 ===")
        data = scrape_tweet(tweet_url)
        if data:
            print(f"抓取结果: {data}")
            save_to_csv(data, output_file)
        else:
            print("⚠️ 没有抓取到内容，可能是网络或页面加载问题。")

        print(f"⏰ 等待 {interval_minutes} 分钟后再次运行...\n")
        time.sleep(interval_minutes * 60)  # 转换为秒


# === 主程序入口 ===
if __name__ == "__main__":
    tweet_url = "https://x.com/dramaDIVE_ytv/status/1981567801405161653"  # ← 换成真实推文链接
    auto_run(tweet_url, interval_minutes=30)
