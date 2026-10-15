import os
import time

def test_disk_speed(file_name="test_speed_file.bin", file_size_mb=1024, block_size_kb=1024):
    file_size_bytes = file_size_mb * 1024 * 1024
    block_size_bytes = block_size_kb * 1024
    
    # Генерируем случайный блок данных, чтобы диск не мог схитрить за счет сжатия
    data_block = os.urandom(block_size_bytes)
    
    print(f"Подготовка файла размером {file_size_mb} МБ...")
    
    # 1. Тест ЗАПИСИ
    start_time = time.perf_counter()
    with open(file_name, "wb") as f:
        written = 0
        while written < file_size_bytes:
            f.write(data_block)
            written += block_size_bytes
    # Принудительно сбрасываем буферы на диск
    os.sync() if hasattr(os, 'sync') else None
    write_duration = time.perf_counter() - start_time
    write_speed = file_size_mb / write_duration
    
    # 2. Тест ЧТЕНИЯ
    start_time = time.perf_counter()
    with open(file_name, "rb") as f:
        while True:
            chunk = f.read(block_size_bytes)
            if not chunk:
                break
    read_duration = time.perf_counter() - start_time
    read_speed = file_size_mb / read_duration
    
    # 3. Очистка
    if os.path.exists(file_name):
        os.remove(file_name)
        
    print("\nРезультаты теста диска:")
    print(f"  - Скорость ЗАПИСИ: {write_speed:.2f} МБ/сек (Время: {write_duration:.3f} сек)")
    print(f"  - Скорость ЧТЕНИЯ: {read_speed:.2f} МБ/сек (Время: {read_duration:.3f} сек)")

if __name__ == "__main__":
    test_disk_speed()

