import os
import zipfile
import time

# указываем ЧТО архивировать
source = input("Введите путь к каталогу, который нужно архивировать: ")
# указываем КУДА архивировать
target_dir = input("Введите путь к каталогу, где будет храниться архив: ")

# имя для подкаталога с текущей датой
today = target_dir + os.sep + time.strftime('%Y%m%d')
# имя для архива с текущим временем
now = time.strftime('%H%M%S')

# комментарий к архиву, который будет записан в конце имени архива
comment = input("Введите комментарий --> ")
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

# переход к указанному каталогу
os.chdir(target_dir)

# создание подкаталога
if not os.path.exists(today):
    os.mkdir(today)
    print("Каталог успешно создан", today)

# создание архива
zip_file = zipfile.ZipFile(target, 'w')

for root, dirs, files in os.walk(source):
    for file in files:
        zip_file.write(os.path.join(root, file))

zip_file.close()

# проверка созданного архива на наличие в конечном каталоге
if zipfile.is_zipfile(target) == 1:
    print("Резервная копия успешно создана в", target)
else:
    print("Создание резервной копии НЕ УДАЛОСЬ")
