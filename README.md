# TeamSpeag_CS2_GSI
## 1. Установка конфига ##
Перемистить файл gamestate_integration_GSI.cfg в папку cfg по пути ```...steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg```
## 2. запустить сервер ##
В файлу runserver убедиться что host и port совпадают с uri в файле gamestate_integration_GSI.cfg\
В Строках
```python
  os.system('cd "C:\Program Files (x86)\Steam\steamapps\common\Soundpad" & Soundpad -rc DoPlaySoundFromCategory(-1,2)')
  os.system('cd "C:\Program Files (x86)\Steam\steamapps\common\Soundpad" & Soundpad -rc DoPlaySoundFromCategory(-1,1)')
```
нужно указать свою директорию для Soundpad и в параметрах ```DoPlaySoundFromCategory(-1,2)``` указать свои значения где первый отвечает за номер категории, а второй за номер звука
## 3. скачать кабель ##
Так же понадобиться скачать [Virtual Audio Channel](https://www.4shared.com/rar/anJA4ww-/virtual_audio_cable_410_-_vac4.html)
В настройках саундпада нужно поставить галочку на Line1 (Настройки -> Устройства)
## 4. Настройка TeamSpeak ##
  1. Нажмите на ярлык правой кнопокй мыши и откройте свойства ярлыка, в поле Объект(Цель) вставте -nosingleinstance
  2. Откройте TS зайдите Инструменты -> Параметры -> Запись и во вкладке устройство записи поставьте Line1
  3. Выйдите из своего канала и создайте новую "Идентификацию" (нажав Control + I)
  4. Создайте новое подключение (Закладка) к вашему серверу и нажмите "больше", чтобы добавить свою новую идентификацию. Выберите свою новую идентификацию и выберите воспроизведение и захват, которые вы создали (например, MusicBot, если вы назвали их так)
