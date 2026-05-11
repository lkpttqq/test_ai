#!/usr/bin/env python3
"""获取昆明当天天气信息"""

import urllib.request
import json


def get_weather():
    try:
        url = "https://wttr.in/Kunming?format=j1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))

        current = data['current_condition'][0]
        print("=" * 50)
        print("昆明当天天气")
        print("=" * 50)
        print(f"  温度: {current['temp_C']}°C")
        print(f"  天气: {current['weatherDesc'][0]['value']}")
        print(f"  体感温度: {current['FeelsLikeC']}°C")
        print(f"  湿度: {current['humidity']}%")
        print(f"  风速: {current['windspeedKmph']} km/h")
        print(f"  风向: {current['winddir16Point']}")
        print(f"  能见度: {current['visibility']} km")
        print(f"  气压: {current['pressure']} mb")
        print("=" * 50)

        return True
    except Exception as e:
        print(f"获取天气失败: {e}")
        return False


if __name__ == '__main__':
    get_weather()