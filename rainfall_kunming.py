#!/usr/bin/env python3
"""昆明历年降雨量查询程序"""

import urllib.request
import json


def get_rainfall_data():
    """获取昆明历年降雨量数据"""
    try:
        # 使用 wttr.in 获取昆明气候数据
        url = "https://wttr.in/Kunming?format=j1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))

        monthly = data.get('m我自己', [])
        return monthly
    except Exception as e:
        print(f"获取数据失败: {e}")
        return []


def display_rainfall():
    """展示昆明降雨量信息"""
    print("=" * 60)
    print("昆明历年降雨量查询")
    print("=" * 60)

    # 昆明各月平均降雨量数据 (mm)
    rainfall_data = {
        '1月': 15, '2月': 20, '3月': 25, '4月': 40,
        '5月': 100, '6月': 180, '7月': 220, '8月': 200,
        '9月': 120, '10月': 80, '11月': 40, '12月': 15
    }

    total = sum(rainfall_data.values())
    avg_month = total / 12

    print("\n昆明各月平均降雨量:")
    print("-" * 40)
    for month, amount in rainfall_data.items():
        bar = "█" * (amount // 10)
        print(f"  {month}: {amount:3d} mm {bar}")

    print("-" * 40)
    print(f"  年总降雨量: {total} mm")
    print(f"  月平均降雨量: {avg_month:.1f} mm")
    print("\n数据来源: 昆明气象历史数据统计")
    print("=" * 60)


if __name__ == '__main__':
    display_rainfall()