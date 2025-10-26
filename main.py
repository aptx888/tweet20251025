import time
from scraper import get_retweet_count_and_timestamp
import csv


# 保存数据到 CSV
def save_data_to_csv(data, filename='data.csv'):
    # 打开 CSV 文件并写入数据
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # 如果文件为空，写入标题
        if file.tell() == 0:
            writer.writerow(['Timestamp', 'Retweet Count'])

        # 写入数据
        writer.writerows(data)
        print(f"数据已保存到 {filename}")


# 主函数：循环抓取数据并保存
def main():
    # 直接在这里指定你的推文 URL
    tweet_url = 'https://x.com/dramaDIVE_ytv/status/1981567801405161653'  # 请替换为你自己的推文 URL

    start_time = time.time()
    data = []

    # 持续抓取指定时间（默认1小时）
    while time.time() - start_time < 3600:  # 持续抓取1小时
        timestamp, retweet_count = get_retweet_count_and_timestamp(tweet_url)

        # 获取当前时间戳并保存数据
        timestamp_float = time.time()
        data.append([timestamp, retweet_count])

        # 每次抓取后保存到 CSV
        save_data_to_csv([[timestamp, retweet_count]])

        # 每30分钟抓取一次
        time.sleep(30 * 60)  # 以分钟为单位


# 运行主函数
if __name__ == '__main__':
    main()
