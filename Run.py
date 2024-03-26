import subprocess
import time
import sys
import os

def monitor_process(command, log_file, restart=False, timeout=None):
    """
    Функция для мониторинга процесса

    Args:
        command: Команда для запуска процесса
        log_file: Путь к файлу для записи вывода
        restart: Перезапускать ли процесс при падении
        timeout: Максимальное время работы процесса в секундах

    Returns:
        None
    """

    with open(log_file, 'a') as log:
        process = subprocess.Popen(command, shell=True, stdout=log, stderr=log)
        start_time = time.time()

        while True:
            if timeout and (time.time() - start_time) > timeout:
                print(f"Превышен таймаут ({timeout} секунд), процесс {process.pid} будет убит.")
                process.kill()
                break

            process.poll()

            if process.returncode is not None:
                if restart:
                    print(f"Процесс {process.pid} упал, перезапускаем...")
                    process = subprocess.Popen(command, shell=True, stdout=log, stderr=log)
                else:
                    print(f"Процесс {process.pid} завершен с кодом {process.returncode}.")
                    break

            time.sleep(1)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python monitor_process.py <command> <log_file> [--restart] [--timeout <seconds>]")
        sys.exit(1)

    command = sys.argv[1]
    log_file = sys.argv[2]
    restart = False
    timeout = None

    if '--restart' in sys.argv:
        restart = True

    if '--timeout' in sys.argv:
        try:
            timeout = int(sys.argv[sys.argv.index('--timeout') + 1])
        except ValueError:
            print("Неверный формат параметра --timeout.")
            sys.exit(1)

    monitor_process(command, log_file, restart, timeout)
