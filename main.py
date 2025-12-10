import time
from datetime import datetime, timedelta
from typing import List, Dict


class WeatherSimulator:
    """天气模拟器 - 随机生成天气数据"""
    
    WEATHER_TYPES = ["晴天", "多云", "阴天", "小雨", "中雨", "大雨", "雷雨", "雪"]
    CITIES = ["北京", "上海", "深圳", "杭州", "成都", "西安", "广州", "南京"]
    
    def __init__(self):
        self.data: List[Dict] = []
    
    def generate_weather(self, days: int = 7) -> List[Dict]:
        """生成指定天数的天气数据"""
        self.data = []
        base_date = datetime.now()
        
        for i in range(days):
            date = base_date + timedelta(days=i)
            city = random.choice(self.CITIES)
            weather = random.choice(self.WEATHER_TYPES)
            temp_high = random.randint(15, 35)
            temp_low = random.randint(5, temp_high)
            humidity = random.randint(30, 90)
            
            record = {
                "日期": date.strftime("%Y-%m-%d"),
                "城市": city,
                "天气": weather,
                "最高温": f"{temp_high}°C",
                "最低温": f"{temp_low}°C",
                "湿度": f"{humidity}%"
            }
            self.data.append(record)
        
        return self.data
