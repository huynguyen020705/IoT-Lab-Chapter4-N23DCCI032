import psutil

# Bước 2: Đọc CPU usage
cpu_list = psutil.cpu_percent(interval=1, percpu=True)
cpu_avg = sum(cpu_list) / len(cpu_list)  # Tính trung bình các nhân
print(f"CPU List: {cpu_list}")
print(f"CPU Average: {cpu_avg}%")
