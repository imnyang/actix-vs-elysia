import matplotlib.pyplot as plt
import pandas as pd

# 데이터를 읽어오는 함수
def read_memory_usage(file_path):
    data = {'PM': [], 'WS': []}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(' - ')
            if len(parts) > 1:
                memory_data = parts[1].split(', ')
                pm = float(memory_data[0].split(': ')[1].replace(' MB', ''))
                ws = float(memory_data[1].split(': ')[1].replace(' MB', ''))
                data['PM'].append(pm)
                data['WS'].append(ws)
    return data

# 두 파일에서 데이터 읽기
bun_data = read_memory_usage('bun_memory_usage.txt')
actix_data = read_memory_usage('actix_memory_usage.txt')

# PM과 WS 값 합산
bun_total = [bun_data['PM'][i] + bun_data['WS'][i] for i in range(len(bun_data['PM']))]
actix_total = [actix_data['PM'][i] + actix_data['WS'][i] for i in range(len(actix_data['PM']))]

# 그래프 생성
plt.figure(figsize=(10, 6))

# Bun의 PM과 WS 합산된 값 플로팅
plt.plot(bun_total, label='Elysia Total (PM + WS)', color='blue')

# Actix의 PM과 WS 합산된 값 플로팅
plt.plot(actix_total, label='Actix Total (PM + WS)', color='red')

# 그래프 설정
plt.xlabel('Data Points')
plt.ylabel('Memory Usage (MB)')
plt.title('Total Memory Usage Comparison (Bun vs Actix)')
plt.legend()

# 그래프 표시
plt.tight_layout()
plt.savefig("benchmark_comparison_memory.png", dpi=300)
print("이미지가 'benchmark_comparison_memory.png' 파일로 저장되었습니다.")

