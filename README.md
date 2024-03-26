# monitor_process

    Функция monitor_process принимает следующие параметры:
        command: Команда для запуска процесса
        log_file: Путь к файлу для записи вывода
        restart: Перезапускать ли процесс при падении
        timeout: Максимальное время работы процесса в секундах
        
    Функция запускает процесс, используя subprocess.Popen, и записывает его stdout и stderr в файл log_file.
    Если restart установлен в True, функция будет перезапускать процесс, если он падает.
    Если timeout установлен, функция будет убивать процесс, если он работает дольше timeout секунд.

#Пример использования:

python monitor_process.py python my_script.py log.txt --restart --timeout 300

Этот пример:

    Запускает python my_script.py.
    Записывает stdout и stderr в log.txt.
    Перезапускает my_script.py, если он падает.
    Убивает my_script.py, если он работает дольше 300 секунд.
