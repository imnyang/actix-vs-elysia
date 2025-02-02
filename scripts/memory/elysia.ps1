# 로그 파일 설정
$outputFile = "bun_memory_usage.txt"

# 프로세스가 존재하는 동안 반복
while ($true) {
    # 프로세스 정보 가져오기 (여러 개일 경우 첫 번째만 선택)
    $process = Get-Process -Name "bun" -ErrorAction SilentlyContinue | Select-Object -First 1
    
    if ($process) {
        # 메모리 값을 MB 단위로 변환 후 기록
        $pm = [math]::Round($process.PrivateMemorySize64 / 1MB, 2)  # Private Memory (MB)
        $ws = [math]::Round($process.WorkingSet64 / 1MB, 2)  # Working Set (MB)

        "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - PM: $pm MB, WS: $ws MB" | Out-File -Append $outputFile
    } else {
        break  # 프로세스가 종료되면 루프 중단
    }

    # 1초 대기 후 다시 체크
    Start-Sleep -Seconds 1
}
