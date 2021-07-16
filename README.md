# Проект предоставляет простой способ изменить размер всех изображений в каталоге с сохранением внутренней структуры иерархии папок.

### В основе лежит библиотека Python - Pillow.
### Исходные файлы не будут изменены.
### Все посторонние файлы в обрабатываемом каталоге, которые не являются изображениями или не поддерживаются библиотекой, будут пропущены и не попадут в результирующий каталог.
### При обработке изображения указываются его максимальная ширина и высота в пикселях. Изображение будет приведено к этим параметрам таким образом, чтобы ширина и высота обработанного изображения не превышали указанные размеры, при этом пропорции изображения будут сохранены.
#### Для работы понадобится:
* Интерпритатор языка программирования [Python](https://www.python.org/downloads/) не ниже версии 3.6;
* После установки интерпритатора, открыть терминал и перейти в каталог проекта и создать виртуальное окружение. Команды для работы с venv могут отличаться в зависимости от вашей ОС, за подробной информацией по работе с виртуальным окружением обращайтесь к [первоисточнику](https://docs.python.org/3/library/venv.html).
```text
python -m venv ./venv    
```
* Активировать виртуальное окружение. Так для Ubuntu и ей подобным системам это будет выглядеть так:
```text
source ./venv/bin/activate
```
* Установить зависимости:
```text
pip install -r requirements.txt
```
* Положить папку с изображениями подлежащими обработке в каталог ./src.
* Запустить скрипт обработки с желаемыми параметрами максимальной ширины и высоты, или без них, тогда будут использованы значения по умолчания - для ширины: 1024px, для высоты: 768px. Примеры использования:
```text
python resize_images.py
```
или с указанием ширины и высоты соответственно:
```text
python resize_images.py 800 600
```
Результат работы будет в каталоге ./copies.