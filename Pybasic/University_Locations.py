## Use GAODE API

import requests
import json
import time

base_url = 'https://restapi.amap.com/v3/geocode/geo'
key = '5680a1f1296e2266413cf77a2bb35e3e'

universities = [
    "北京大学",
    "中国人民大学",
    "清华大学",
    "北京航空航天大学",
    "北京理工大学",
    "中国农业大学",
    "北京师范大学",
    "中央民族大学",
    "南开大学",
    "天津大学",
    "大连理工大学",
    "东北大学",
    "吉林大学",
    "哈尔滨工业大学",
    "复旦大学",
    "同济大学",
    "上海交通大学",
    "华东师范大学",
    "南京大学",
    "东南大学",
    "浙江大学",
    "中国科学技术大学",
    "厦门大学",
    "山东大学",
    "中国海洋大学",
    "武汉大学",
    "华中科技大学",
    "湖南大学",
    "中南大学",
    "国防科学技术大学",
    "中山大学",
    "华南理工大学",
    "四川大学",
    "电子科技大学",
    "重庆大学",
    "西安交通大学",
    "西北工业大学",
    "西北农林科技大学",
    "兰州大学"]

universities_info = []

start_time = time.time()  # 记录开始时间

for i, university in enumerate(universities, 1):
    url = f'{base_url}?address={university}&output=JSON&key={key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        universities_info.append(data)
        print(f"收集进度：{i}/{len(universities)} - {university} 完成")
    else:
        print(f"Error ({response.status_code}): 收集 {university} 失败")

end_time = time.time()  # 记录结束时间
elapsed_time = end_time - start_time
print(f"总时间：{elapsed_time:.2f} 秒")

# universities_info 现在包含了每个大学的地理信息字典
# 可以将 universities_info 存储到文件中，比如保存为 JSON 文件
import json
with open('universities_info.json', 'w', encoding='utf-8') as f:
    json.dump(universities_info, f, ensure_ascii=False, indent=2)

import pandas as pd
# 加载 universities_info.json 的内容
with open('universities_info.json', 'r', encoding='utf-8') as json_file:
    universities_info = json.load(json_file)
# 提取地理编码信息
geocodes = universities_info.get("geocodes", [])
# 将数据转换为 Pandas DataFrame
df = pd.json_normalize(geocodes)
# 将 DataFrame 保存为 CSV 文件
csv_filename = 'universities_info.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8')
print(f"大学信息已保存至 {csv_filename}")
