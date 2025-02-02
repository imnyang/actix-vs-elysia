import matplotlib.pyplot as plt

# 서버 이름 변경
servers = ["Elysia 1.2.11 (bun 1.2.2)", "Actix 4.9 (cargo 1.84.1)"]

# 요청 처리 속도 (Requests/sec)
reqs_avg = [49289.75, 48399.96]
reqs_max = [65348.36, 97313.91]

# 응답 시간 (Latency in ms)
latency_avg = [4.06, 4.05]
latency_max = [39.69, 1650]

# 총 처리량 (Throughput in MB/s)
throughput = [10.34, 8.36]

# 그래프 설정
fig, axes = plt.subplots(3, 1, figsize=(8, 12))
fig.suptitle("Simple Get Request with Params, Query")  # Add this line to set the title

# 요청 처리 속도 그래프
axes[0].bar(servers, reqs_avg, color=['blue', 'orange'], alpha=0.7, label="Avg Requests/s")
axes[0].bar(servers, reqs_max, color=['blue', 'orange'], alpha=0.3, label="Max Requests/s")
axes[0].set_title("Requests per Second (Biggest is better)")
axes[0].set_ylabel("Requests/sec")
axes[0].legend()

# 응답 시간 그래프
axes[1].bar(servers, latency_avg, color=['green', 'red'], alpha=0.7, label="Avg Latency (ms)")
axes[1].bar(servers, latency_max, color=['green', 'red'], alpha=0.3, label="Max Latency (ms)")
axes[1].set_title("Latency (ms) (Smallest is better)")
axes[1].set_ylabel("Milliseconds")
axes[1].legend()

# 총 처리량 그래프
axes[2].bar(servers, throughput, color=['purple', 'cyan'], alpha=0.7)
axes[2].set_title("Throughput (MB/s) (Biggest is better)")
axes[2].set_ylabel("MB/s")

# 레이아웃 정리 및 이미지 저장
plt.tight_layout()
plt.savefig("benchmark_comparison_get2.png", dpi=300)
print("이미지가 'benchmark_comparison.png' 파일로 저장되었습니다.")
