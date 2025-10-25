import csv
import os
import matplotlib.pyplot as plt
import time

# 保存数据到 CSV 文件
def save_data(data, filename="data.csv"):
    file_exists = os.path.exists(filename)
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'Retweet Count'])  # 写入表头
        for row in data:
            writer.writerow(row)

# 从 CSV 文件读取数据
def read_data(filename="data.csv"):
    data = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # 跳过表头
            for row in reader:
                # 将字符串转化为合适的数据类型
                data.append([float(row[0]), int(row[1])])
    return data

# 绘制转发数趋势图
def plot_retweet_trend(retweet_data):
    timestamps = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item[0])) for item in retweet_data]
    retweet_counts = [item[1] for item in retweet_data]

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, retweet_counts, marker='o', color='b')
    plt.xlabel('时间')
    plt.ylabel('转发数')
    plt.title('推文转发趋势')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('retweet_trend.png')  # 保存为图片
    plt.show()  # 显示图表
