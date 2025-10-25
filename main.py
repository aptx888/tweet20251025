from scraper import get_retweet_count
from data_handler import save_data, read_data, plot_retweet_trend
import time


def main():
    # 这里指定你要抓取的推特推文网址
    tweet_url = "https://x.com/dramaDIVE_ytv/status/1981567801405161653"  # 请替换为实际的推特 URL

    # 读取历史数据（如果有）
    retweet_data = read_data()

    # 手动测试，抓取一次数据
    retweet_count = get_retweet_count(tweet_url)  # 调用爬虫抓取转发数
    timestamp = time.time()
    retweet_data.append([timestamp, retweet_count])
    save_data([[timestamp, retweet_count]])  # 保存当前数据到文件
    print(f"抓取成功！转发数：{retweet_count}")

    # 绘制并保存趋势图
    plot_retweet_trend(retweet_data)

    # 如果你要定期抓取数据，可以恢复以下部分
    # 每隔30分钟（1800秒）抓取一次转发数，持续1小时
    # start_time = time.time()
    # while time.time() - start_time < 3600:  # 3600秒=1小时
    #     retweet_count = get_retweet_count(tweet_url)  # 调用爬虫抓取转发数
    #     timestamp = time.time()
    #     retweet_data.append([timestamp, retweet_count])
    #     save_data([[timestamp, retweet_count]])  # 保存当前数据到文件
    #     print(f"抓取成功！转发数：{retweet_count}")  # 打印转发数
    #     time.sleep(1800)  # 每30分钟抓取一次


if __name__ == "__main__":
    main()
