import pygame
import sys
import calendar
import speech_recognition as sr


def frame():
    global screen
    pygame.draw.line(screen, (0, 0, 0), (10, 10), (990, 10), 3)
    pygame.draw.line(screen, (0, 0, 0), (10, 10), (10, 640), 3)
    pygame.draw.line(screen, (0, 0, 0), (10, 640), (990, 640), 3)
    pygame.draw.line(screen, (0, 0, 0), (990, 10), (990, 640), 3)
    pattern = pygame.image.load('pattern.png')
    pattern = pygame.transform.rotate(pattern, 90)
    screen.blit(pattern, (735, 30))
    pattern = pygame.transform.flip(pattern, False, True)
    screen.blit(pattern, (735, 435))
    pattern = pygame.transform.flip(pattern, True, False)
    screen.blit(pattern, (30, 435))
    pattern = pygame.transform.flip(pattern, False, True)
    screen.blit(pattern, (30, 30))
    text(20, 'Minsk 2022 SPK Version 1.05', (400, 600), (0, 0, 205))


def text(size, content, point, color_content):
    global screen
    txt = pygame.font.SysFont('serif', size)
    text_1 = txt.render(content, True, color_content)
    screen.blit(text_1, point)


def button(x, y, length, h, title):
    global screen
    pygame.draw.rect(screen, (0, 255, 0), (x, y, length, h), 0)
    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + length, y), 3)
    pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + h), 3)
    pygame.draw.line(screen, (0, 0, 0), (x, y + h), (x + length, y + h), 3)
    pygame.draw.line(screen, (0, 0, 0), (x + length, y), (x + length, y + h), 3)
    el = pygame.font.SysFont('serif', 20)
    text_1 = el.render(title, True, (0, 0, 0))
    screen.blit(text_1, (x + 7, y + 7))


def error_input():
    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
    smail_def = pygame.image.load('smail5.png')
    screen.blit(smail_def, (410, 80))
    button(300, 420, 120, 35, '<<< Назад')
    text(30, 'Я подозревал что ты ИДИОТ !', (310, 290), (0, 0, 205))


def input_year(number_year):
    global work_data, flag_error, flag_input_month
    if number_year.isdigit():
        if len(number_year) == 2:
            number_year = '20' + number_year
        if len(number_year) == 4:
            if int(number_year) in range(2000, 2100):
                work_data.append(number_year)
                flag_input_month = True
            else:
                error_input()
                text(30, 'Введи правильно год !!!', (350, 350), (0, 0, 205))
                pygame.display.update((100, 85, 800, 480))
                flag_error = True
        else:
            error_input()
            text(30, 'Введи правильно год !!!', (350, 350), (0, 0, 205))
            pygame.display.update((100, 85, 800, 480))
            flag_error = True
    else:
        error_input()
        text(30, 'Введи правильно год !!!', (350, 350), (0, 0, 205))
        pygame.display.update((100, 85, 800, 480))
        flag_error = True


def input_month(month_name):
    global work_data, flag_error, flag_input_day
    month = {'январь': '01', 'февраль': '02', 'март': '03', 'апрель': '04', 'май': '05', 'июнь': '06',
             'июль': '07', 'август': '08', 'сентябрь': '09', 'октябрь': '10', 'ноябрь': '11', 'декабрь': '12'}
    if month_name in month:
        work_data.append(month[month_name])
        flag_input_day = True
    else:
        error_input()
        text(30, 'Введи правильно месяц !!!', (350, 350), (0, 0, 205))
        pygame.display.update((100, 85, 800, 480))
        flag_error = True


def input_day(number_day):
    global work_data, flag_error, flag_input_data
    leap_year = [2000, 2020, 2040, 2060, 2080, 2004, 2024, 2044, 2064, 2084, 2008, 2028, 2048, 2068,
                 2088, 2012, 2032, 2052, 2072, 2092, 2016, 2036, 2056, 2076, 2096]
    if int(work_data[0]) in leap_year:
        examination = {'01': '31', '02': '29', '03': '31', '04': '30', '05': '31', '06': '30',
                       '07': '31', '08': '31', '09': '30', '10': '31', '11': '30', '12': '31'}
    else:
        examination = {'01': '31', '02': '28', '03': '31', '04': '30', '05': '31', '06': '30',
                       '07': '31', '08': '31', '09': '30', '10': '31', '11': '30', '12': '31'}
    col_day_month = list(range(int(examination[work_data[1]]) + 1))
    if number_day.isdigit():
        if int(number_day) in col_day_month:
            work_data.append(number_day)
            flag_input_data = True
        else:
            error_input()
            text(30, 'Введи правильно число месяца !!!', (290, 350), (0, 0, 205))
            pygame.display.update((100, 85, 800, 480))
            flag_error = True
    else:
        error_input()
        text(30, 'Введи правильно число месяца !!!', (290, 350), (0, 0, 205))
        pygame.display.update((100, 85, 800, 480))
        flag_error = True


def output_data(work_data):
    month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
             '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
    data = list()
    data.append(work_data[2])
    data.append(month[work_data[1]])
    data.append(work_data[0])
    with open('Рабочий график.txt', 'w', encoding='utf-8') as file:
        file.write('\n')
        file.write('Твоя дата : {}\n'.format(' '.join(data)))
        file.write('\n')
        file.write('----------------------------------------\n')
    return ' '.join(data)


def convert_day(day, max_month):
    if day > max_month:
        if max_month == 31:
            if day == 32:
                day = 1
            elif day == 33:
                day = 2
            elif day == 34:
                day = 3
            elif day == 35:
                day = 4
        elif max_month == 30:
            if day == 31:
                day = 1
            elif day == 32:
                day = 2
            elif day == 33:
                day = 3
            elif day == 34:
                day = 4
        elif max_month == 28:
            if day == 29:
                day = 1
            elif day == 30:
                day = 2
            elif day == 31:
                day = 3
            elif day == 32:
                day = 4
        elif max_month == 29:
            if day == 30:
                day = 1
            elif day == 31:
                day = 2
            elif day == 32:
                day = 3
            elif day == 33:
                day = 4
    return day


def month_work_print():
    global month
    global work_data, dict_col_day
    global work_day, work_night, week_day_1, week_day_2, col_work
    global work_calendar
    global flag_step_down
    dict_col_day = {'Д': 0, 'Н': 0, 'В': 0}
    text(25, month[int(work_data[1]) - 1], (550, 100), (0, 0, 205))
    text(20, '     Пн   |     Вт     |     Ср    |     Чт     |     Пт    |     Сб    |     Вс     ',
         (350, 150), (255, 0, 0))
    text(20, '___________________________________________________', (350, 160), (0, 0, 128))
    month_list = calendar.monthcalendar(int(work_data[0]), int(work_data[1]))
    k = 30
    s = '   '
    max_month = max(max(month_list))
    if col_work == 0:
        work_day = int(work_data[2])
        work_night = work_day + 1
        week_day_1 = work_night + 1
        week_day_2 = week_day_1 + 1
        col_work += 1
    elif not flag_step_down:
        col_work += 1
    elif flag_step_down:
        col_work -= 1
    work_calendar.append([int(work_data[1]), work_day, work_night, week_day_1, week_day_2])
    for i in month_list:
        temp = []
        for j in i:
            if int(j) == work_day:
                s = 'Д'
                work_day += 4
                if work_day > max_month:
                    work_day = convert_day(work_day, max_month)
            elif int(j) == work_night:
                s = 'Н'
                work_night += 4
                if work_night > max_month:
                    work_night = convert_day(work_night, max_month)
            elif int(j) == week_day_1:
                s = 'В'
                week_day_1 += 4
                if week_day_1 > max_month:
                    week_day_1 = convert_day(week_day_1, max_month)
            elif int(j) == week_day_2:
                s = 'В'
                week_day_2 += 4
                if week_day_2 > max_month:
                    week_day_2 = convert_day(week_day_2, max_month)
            if j == 0:
                temp.append('            ')
            elif len(str(j)) == 1:
                if s == '   ':
                    temp.append('    ' + str(j) + '   ' + '--')
                else:
                    temp.append('    ' + str(j) + '   ' + s)
            else:
                if s == '   ':
                    temp.append('    ' + str(j) + ' ' + '--')
                else:
                    temp.append('    ' + str(j) + ' ' + s)
            if s == 'Д' and j != 0:
                dict_col_day['Д'] += 1
            elif s == 'Н' and j != 0:
                dict_col_day['Н'] += 1
            elif s == 'В' and j != 0:
                dict_col_day['В'] += 1
        week = '  |'.join(temp)
        text(20, week, (350, 160 + k), (0, 0, 128))
        k += 10
        text(20, '___________________________________________________', (350, 160 + k), (0, 0, 128))
        k += 30
    if work_night > max_month:
        work_night = convert_day(work_night, max_month)
    if week_day_1 > max_month:
        week_day_1 = convert_day(week_day_1, max_month)
    if week_day_2 > max_month:
        week_day_2 = convert_day(week_day_2, max_month)


def record():
    global work_calendar
    global month
    global dict_col_day
    with open('Рабочий график.txt', 'a', encoding='utf-8') as file:
        file.write('      {}    '.format(month[work_calendar[-1][0] - 1]))
        file.write('\n')
        file.write(' Количество рабочих дней : {}'.format(dict_col_day['Д']))
        file.write('\n')
        file.write(' Количество рабочих ночей : {}'.format(dict_col_day['Н']))
        file.write('\n')
        file.write(' Количество рабочих часов за месяц : {}'.format((dict_col_day['Н'] + dict_col_day['Д']) * 12))
        file.write('\n')
        file.write('----------------------------------------\n')


def audio_record():
    global flag_audio_error
    try:
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
        query = r.recognize_google(audio, language="ru-RU")
        return query
    except sr.UnknownValueError:
        flag_audio_error = True
    except sr.RequestError:
        """Ошибка подключения к интернету """
        flag_audio_error = True
        pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
        smail_def = pygame.image.load('smail9.png')
        screen.blit(smail_def, (360, 90))
        button(300, 420, 120, 35, '<<< Назад')
        text(30, 'НЕТ СВЯЗИ С ИНТЕРНЕТОМ !!!', (290, 330), (0, 0, 205))
        pygame.display.update((100, 85, 800, 480))


def examination_audio_record(audio_data):
    global work_data
    global flag_audio_error, flag_audio_output_data
    if not flag_audio_error:
        try:
            audio_data = audio_data.replace('.', ' ')
            audio_data = audio_data.split()
            audio_data = audio_data[:3]
            number_year = audio_data[2]
            if number_year.isdigit():
                if len(number_year) == 2:
                    number_year = '20' + number_year
                if len(number_year) == 4:
                    if int(number_year) in range(2000, 2100):
                        work_data.append(number_year)
                    else:
                        flag_audio_error = True
            month_name = audio_data[1]
            month = {'января': '01', 'февраля': '02', 'марта': '03', 'апреля': '04', 'мая': '05', 'июня': '06',
                     'июля': '07', 'августа': '08', 'сентября': '09', 'октября': '10', 'ноября': '11', 'декабря': '12'}
            month_2 = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
                       '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
            if month_name in month:
                work_data.append(month[month_name])
            elif month_name in month_2:
                work_data.append(audio_data[1])
            else:
                flag_audio_error = True
            number_day = audio_data[0]
            if number_day.isdigit():
                leap_year = [2000, 2020, 2040, 2060, 2080, 2004, 2024, 2044, 2064, 2084, 2008, 2028, 2048, 2068,
                             2088, 2012, 2032, 2052, 2072, 2092, 2016, 2036, 2056, 2076, 2096]
                if int(work_data[0]) in leap_year:
                    examination = {'01': '31', '02': '29', '03': '31', '04': '30', '05': '31', '06': '30',
                                   '07': '31', '08': '31', '09': '30', '10': '31', '11': '30', '12': '31'}
                else:
                    examination = {'01': '31', '02': '28', '03': '31', '04': '30', '05': '31', '06': '30',
                                   '07': '31', '08': '31', '09': '30', '10': '31', '11': '30', '12': '31'}
                col_day_month = list(range(int(examination[work_data[1]]) + 1))
                if int(number_day) in col_day_month:
                    work_data.append(number_day)
                    flag_audio_output_data = True
                else:
                    flag_audio_error = True
            else:
                flag_audio_error = True
        except IndexError:
            flag_audio_error = True
        except AttributeError:
            flag_audio_error = True
    if flag_audio_error:
        error_input()
        text(30, 'НЕТ ТАКОЙ ДАТЫ !!!', (350, 350), (0, 0, 205))
        pygame.display.update((100, 85, 800, 480))


pygame.init()
pygame.display.set_caption(' ГРАФИК РАБОТЫ НА ГОД ')  # установить новое название поверхности
screen = pygame.display.set_mode((1000, 650))  # размер поверхности
pygame.Surface.fill(screen, (192, 192, 192))  # залить поверхность сплошным цветом
pygame.display.set_icon(pygame.image.load('calendar.png'))  # установить новый
pygame.mixer.music.load('click.mp3')
frame()
text(30, 'Добро пожаловать в программу ', (305, 100), (0, 0, 205))
text(30, ' " РАБОЧИЙ КАЛЕНДАРЬ " ', (320, 210), (0, 0, 205))
text(25, 'Выбери действие !', (410, 310), (0, 0, 205))
smail = pygame.image.load('smail.png')
screen.blit(smail, (110, 170))
button(300, 420, 120, 35, '<<< Выход')
button(600, 420, 120, 35, 'Дальше >>>')
flag_main_menu = True
flag_main_menu_2 = False
flag_quit = False
flag_input_year = False
flag_input_month = False
flag_input_day = False
flag_input_data = False
flag_error = False
flag_write = False
flag_input_calendar = False
flag_step_down = False
flag_record = False
flag_sound_recording = False
flag_sound_recording_2 = False
flag_audio_error = False
flag_audio_output_data = False
input_box = pygame.Rect(425, 320, 160, 32)
text_data = ''
f1 = pygame.font.Font(None, 32)
pygame.display.update()
work_data = []
month = ['Январь :', 'Февраль :', 'Март :',
         'Апрель :', 'Май :', 'Июнь :',
         'Июль :', 'Август :', 'Сентябрь :',
         'Октябрь :', 'Ноябрь :', 'Декабрь :']
work_day = 0
work_night = 0
week_day_1 = 0
week_day_2 = 0
col_work = 0
work_calendar = []
dict_col_day = {'Д': 0, 'Н': 0, 'В': 0}


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos_mouse = event.pos
                if 300 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 455 and flag_main_menu:
                    """Меню выхода из программы"""
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(300, 420, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((300, 420, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    text(30, ' ТЫ УХОДИШЬ ?', (390, 100), (0, 0, 205))
                    smail = pygame.image.load('smail1.png')
                    screen.blit(smail, (390, 170))
                    button(350, 470, 90, 35, '<<< Нет')
                    button(600, 470, 90, 35, 'Да >>>')
                    flag_main_menu = False
                    flag_quit = True
                    flag_input_year = False
                    flag_input_month = False
                    flag_input_day = False
                    flag_input_data = False
                    flag_error = False
                    flag_write = False
                    flag_input_calendar = False
                    flag_record = False
                    flag_sound_recording = False
                    flag_sound_recording_2 = False
                    flag_step_down = False
                    flag_audio_error = False
                    pygame.display.update((100, 85, 800, 480))
                elif 600 <= pos_mouse[0] <= 690 and 470 <= pos_mouse[1] <= 505 and flag_quit:
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(600, 470, 90, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((600, 470, 90, 35))
                    pygame.time.wait(350)
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(100, 85, 800, 480))
                    text(30, 'Я обиделась !!!!', (420, 100), (0, 0, 205))
                    smail = pygame.image.load('smail4.png')
                    screen.blit(smail, (390, 170))
                    pygame.display.update((100, 85, 800, 480))
                    pygame.time.wait(2000)
                    pygame.quit()
                    sys.exit()
                elif (350 <= pos_mouse[0] <= 440 and 470 <= pos_mouse[1] <= 505 and flag_quit) \
                        or (300 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 455 and flag_input_year)\
                        or (300 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 455 and flag_error)\
                        or (300 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 455 and flag_input_month)\
                        or (300 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 455 and flag_input_day)\
                        or (300 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 455 and flag_input_data)\
                        or (300 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 455 and flag_input_calendar
                            and col_work != 1)\
                        or (700 <= pos_mouse[0] <= 820 and 470 <= pos_mouse[1] <= 505 and flag_quit)\
                        or (300 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 455 and flag_main_menu_2)\
                        or (300 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 455 and flag_sound_recording)\
                        or (300 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 455 and flag_sound_recording_2)\
                        or (400 <= pos_mouse[0] <= 520 and 470 <= pos_mouse[1] <= 505 and flag_input_calendar
                            and col_work == 1):
                    """Переход в меню приветствия из меню выхода и меню ввода даты"""
                    if flag_quit and col_work == 0:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(350, 470, 90, 35))
                        pygame.display.update((350, 470, 90, 35))
                    elif flag_main_menu_2:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(300, 420, 120, 35))
                        pygame.display.update((300, 420, 120, 35))
                    elif flag_sound_recording:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(300, 420, 120, 35))
                        pygame.display.update((300, 420, 120, 35))
                    elif flag_sound_recording_2:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(300, 420, 120, 35))
                        pygame.display.update((300, 420, 120, 35))
                    elif flag_input_year:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(300, 420, 120, 35))
                        pygame.display.update((300, 420, 120, 35))
                    elif flag_error:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(300, 420, 120, 35))
                        pygame.display.update((300, 420, 120, 35))
                    elif flag_input_month:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(300, 420, 120, 35))
                        pygame.display.update((300, 420, 120, 35))
                    elif flag_input_day:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(300, 420, 120, 35))
                        pygame.display.update((300, 420, 120, 35))
                    elif flag_input_data:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(300, 420, 120, 35))
                        pygame.display.update((300, 420, 120, 35))
                    elif flag_input_calendar and not flag_quit and col_work != 1:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(300, 420, 120, 35))
                        pygame.display.update((300, 420, 120, 35))
                    elif flag_quit and col_work != 0:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(700, 470, 120, 35))
                        pygame.display.update((700, 470, 120, 35))
                    elif flag_input_calendar and col_work == 1:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(400, 470, 120, 35))
                        pygame.display.update((400, 470, 120, 35))
                    pygame.mixer.music.play()
                    pygame.time.wait(350)
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(100, 85, 800, 480))
                    text(30, 'Добро пожаловать в программу ', (305, 100), (0, 0, 205))
                    text(30, ' " РАБОЧИЙ КАЛЕНДАРЬ " ', (320, 210), (0, 0, 205))
                    text(25, 'Выбери действие !', (410, 310), (0, 0, 205))
                    smail = pygame.image.load('smail.png')
                    screen.blit(smail, (110, 170))
                    button(300, 420, 120, 35, '<<< Выход')
                    button(600, 420, 120, 35, 'Дальше >>>')
                    flag_main_menu = True
                    flag_main_menu_2 = False
                    flag_quit = False
                    flag_input_year = False
                    flag_input_month = False
                    flag_input_day = False
                    flag_input_data = False
                    flag_error = False
                    flag_write = False
                    flag_input_calendar = False
                    flag_sound_recording = False
                    flag_sound_recording_2 = False
                    flag_step_down = False
                    flag_audio_error = False
                    text_data = ''
                    work_data = []
                    work_night = 0
                    week_day_1 = 0
                    week_day_2 = 0
                    col_work = 0
                    work_calendar = []
                    pygame.display.update((100, 85, 800, 480))
                elif 600 <= pos_mouse[0] <= 720 and 420 <= pos_mouse[1] <= 455 and flag_main_menu:
                    """Меню выбора ввода"""
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(600, 420, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((600, 420, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    text(30, 'И КАК БУДЕМ ВВОДИТЬ ДАТУ ???', (320, 130), (0, 0, 205))
                    text(25, 'Ручками или ', (450, 205), (0, 0, 205))
                    text(25, ' "... тихо молвила царица ... "', (380, 270), (0, 0, 205))
                    button(300, 420, 120, 35, '<<< Назад')
                    button(600, 420, 120, 35, ' Текст >>>')
                    button(455, 420, 120, 35, ' Голос >>>')
                    smail = pygame.image.load('smail6.png')
                    screen.blit(smail, (100, 180))
                    flag_main_menu = False
                    flag_main_menu_2 = True
                    pygame.display.update((100, 85, 800, 480))
                elif 455 <= pos_mouse[0] <= 575 and 420 <= pos_mouse[1] <= 455 and flag_main_menu_2:
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(455, 420, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((455, 420, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    text(30, 'ЭТО БЫЛО ОЧЕВИДНО !!!', (350, 170), (0, 0, 205))
                    text(30, 'нажми "Запись" ', (410, 260), (0, 0, 205))
                    smail = pygame.image.load('smail7.png')
                    screen.blit(smail, (110, 200))
                    button(300, 420, 120, 35, '<<< Назад')
                    button(600, 420, 120, 35, 'Запись >>>')
                    flag_sound_recording = True
                    flag_main_menu_2 = False
                    pygame.display.update((100, 85, 800, 480))
                elif 600 <= pos_mouse[0] <= 720 and 420 <= pos_mouse[1] <= 455 and flag_sound_recording:
                    """Голосовой ввод"""
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(600, 420, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((600, 420, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    smail = pygame.image.load('microfon.png')
                    screen.blit(smail, (520, 240))
                    smail = pygame.image.load('smail8.png')
                    screen.blit(smail, (300, 150))
                    text(30, 'Произнеси дату и нажми "Ввод" ', (300, 90), (0, 0, 205))
                    text(25, 'В формате " день . месяц . год "', (340, 140), (0, 0, 205))
                    button(300, 420, 120, 35, '<<< Назад')
                    button(600, 420, 120, 35, ' Ввод >>>')
                    flag_sound_recording = False
                    flag_sound_recording_2 = True
                    pygame.display.update((100, 85, 800, 480))
                    audio_data = audio_record()
                    if not flag_audio_error:
                        examination_audio_record(audio_data)
                    elif flag_audio_error:
                        error_input()
                        text(30, 'Произнеси громко и чётко !!!', (320, 350), (0, 0, 205))
                        pygame.display.update((100, 85, 800, 480))
                elif 600 <= pos_mouse[0] <= 720 and 420 <= pos_mouse[1] <= 455 and flag_main_menu_2:
                    """Меню ввода года"""
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(600, 420, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((600, 420, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    text(30, 'Введи год :', (430, 170), (0, 0, 205))
                    text(25, 'в формате 2XXX или XX', (370, 228), (0, 0, 205))
                    text(20, 'активируй поле ввода', (405, 280), (0, 0, 205))
                    pygame.draw.rect(screen, (0, 0, 205), input_box, 2)
                    button(300, 420, 120, 35, '<<< Назад')
                    button(600, 420, 120, 35, 'Дальше >>>')
                    smail = pygame.image.load('smail2.png')
                    screen.blit(smail, (120, 140))
                    flag_main_menu_2 = False
                    flag_input_year = True
                    pygame.display.update((100, 85, 800, 480))
                elif (425 <= pos_mouse[0] <= 585 and 320 <= pos_mouse[1] <= 352 and flag_input_year)\
                        or (425 <= pos_mouse[0] <= 585 and 320 <= pos_mouse[1] <= 352 and flag_input_month)\
                        or (425 <= pos_mouse[0] <= 585 and 320 <= pos_mouse[1] <= 352 and flag_input_day):
                    """Активирует прямоугольник ввода"""
                    pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                    pygame.mixer.music.play()
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(400, 280, 300, 30))
                    pygame.display.update((400, 280, 300, 30))
                    text(20, 'вводи и нажми "ENTER"', (393, 280), (0, 0, 205))
                    flag_write = True
                    pygame.display.update((390, 280, 350, 100))
                elif 600 <= pos_mouse[0] <= 720 and 420 <= pos_mouse[1] <= 455 and flag_input_month:
                    """Меню ввода месяца"""
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(600, 420, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((600, 420, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    text(30, 'Введи месяц :', (410, 170), (0, 0, 205))
                    text(25, 'если тебе не трудно , то буквами', (340, 228), (0, 0, 205))
                    text(20, 'активируй поле ввода', (405, 280), (0, 0, 205))
                    pygame.draw.rect(screen, (0, 0, 205), input_box, 2)
                    button(300, 420, 120, 35, '<<< Назад')
                    button(600, 420, 120, 35, 'Дальше >>>')
                    smail = pygame.image.load('smail2.png')
                    screen.blit(smail, (120, 140))
                    text_data = ''
                    pygame.display.update((100, 85, 800, 480))
                elif 600 <= pos_mouse[0] <= 720 and 420 <= pos_mouse[1] <= 455 and flag_input_day:
                    """Меню ввода дня"""
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(600, 420, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((600, 420, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    text(30, 'Введи число месяца :', (370, 170), (0, 0, 205))
                    text(20, 'активируй поле ввода', (405, 280), (0, 0, 205))
                    pygame.draw.rect(screen, (0, 0, 205), input_box, 2)
                    button(300, 420, 120, 35, '<<< Назад')
                    button(600, 420, 120, 35, 'Дальше >>>')
                    smail = pygame.image.load('smail2.png')
                    screen.blit(smail, (120, 140))
                    text_data = ''
                    pygame.display.update((100, 85, 800, 480))
                elif (600 <= pos_mouse[0] <= 720 and 420 <= pos_mouse[1] <= 455 and flag_input_data
                      and not flag_input_calendar) or (600 <= pos_mouse[0] <= 720 and 420 <= pos_mouse[1] <= 455 and
                                                       flag_audio_output_data):
                    """Вывод введенной даты"""
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(600, 420, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((600, 420, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    text(30, 'Введенная тобой дата :', (370, 170), (0, 0, 205))
                    text_data = output_data(work_data)
                    text(30, text_data, (415, 245), (0, 0, 205))
                    button(300, 420, 120, 35, '<<< Назад')
                    button(600, 420, 120, 35, 'Дальше >>>')
                    smail = pygame.image.load('smail2.png')
                    screen.blit(smail, (120, 140))
                    text_data = ''
                    flag_input_calendar = True
                    flag_input_data = False
                    flag_sound_recording_2 = False
                    flag_audio_output_data = False
                    pygame.display.update((100, 85, 800, 480))
                elif 600 <= pos_mouse[0] <= 720 and 420 <= pos_mouse[1] <= 455 \
                        and flag_input_calendar and col_work == 0:
                    """Вывод первого рабочего месяца"""
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(600, 420, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((600, 420, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    month_work_print()
                    flag_input_data = False
                    flag_record = True
                    flag_step_down = False
                    smail = pygame.image.load('smail3.png')
                    screen.blit(smail, (90, 170))
                    button(400, 470, 120, 35, '<<< Назад')
                    button(700, 470, 120, 35, 'Дальше >>>')
                    button(140, 380, 120, 35, 'Запись >>>')
                    text(20, 'В этом месяце : дневных смен - ' + str(dict_col_day['Д']) + '  ' +
                         'ночных смен - ' + str(dict_col_day['Н']) + '  ' +
                         'выходных - ' + str(dict_col_day['В']), (250, 530), (0, 0, 205))
                    pygame.display.update((100, 85, 800, 480))
                elif 700 <= pos_mouse[0] <= 820 and 470 <= pos_mouse[1] <= 505 \
                        and col_work != 0 and not flag_quit:
                    """Вывод следующего рабочего месяца"""
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(700, 470, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((700, 470, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    flag_input_calendar = False
                    flag_step_down = False
                    work_data[1] = int(work_data[1]) + 1
                    month_work_print()
                    smail = pygame.image.load('smail3.png')
                    screen.blit(smail, (90, 170))
                    if int(work_data[1]) + 1 < 13:
                        button(400, 470, 120, 35, '<<< Назад')
                        button(700, 470, 120, 35, 'Дальше >>>')
                    elif int(work_data[1]) + 1 == 13:
                        button(400, 470, 120, 35, '<<< Назад')
                        button(700, 470, 120, 35, 'Выход >>>')
                        flag_quit = True
                    button(140, 380, 120, 35, 'Запись >>>')
                    text(20, 'В этом месяце : дневных смен - ' + str(dict_col_day['Д']) + '  ' +
                         'ночных смен - ' + str(dict_col_day['Н']) + '  ' +
                         'выходных - ' + str(dict_col_day['В']), (250, 530), (0, 0, 205))
                    pygame.display.update((100, 85, 800, 480))
                elif 400 <= pos_mouse[0] <= 520 and 470 <= pos_mouse[1] <= 505 \
                        and col_work != 0 and not flag_input_calendar:
                    """Вывод предыдущего рабочего месяца"""
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(400, 470, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((400, 470, 120, 35))
                    pygame.time.wait(350)
                    pygame.draw.rect(screen, (192, 192, 192), (100, 85, 800, 480), 0)
                    flag_quit = False
                    flag_step_down = True
                    del work_calendar[-1]
                    work_data[1], work_day, work_night, week_day_1, week_day_2 = work_calendar.pop()
                    month_work_print()
                    smail = pygame.image.load('smail3.png')
                    screen.blit(smail, (90, 170))
                    if len(work_calendar) == 1:
                        flag_input_calendar = True
                        flag_step_down = False
                    button(400, 470, 120, 35, '<<< Назад')
                    button(700, 470, 120, 35, 'Дальше >>>')
                    button(140, 380, 120, 35, 'Запись >>>')
                    text(20, 'В этом месяце : дневных смен - ' + str(dict_col_day['Д']) + '  ' +
                         'ночных смен - ' + str(dict_col_day['Н']) + '  ' +
                         'выходных - ' + str(dict_col_day['В']), (250, 530), (0, 0, 205))
                    pygame.display.update((100, 85, 800, 480))
                elif 140 <= pos_mouse[0] <= 260 and 380 <= pos_mouse[1] <= 415 and flag_record:
                    pygame.Surface.fill(screen, (0, 0, 0), rect=(140, 380, 120, 35))
                    pygame.mixer.music.play()
                    pygame.display.update((140, 380, 120, 35))
                    pygame.time.wait(350)
                    button(140, 380, 120, 35, 'Запись >>>')
                    record()
                    pygame.display.update((140, 380, 120, 35))
        if event.type == pygame.KEYDOWN and flag_input_year and flag_write:
            color = (255, 0, 0)
            if event.key == pygame.K_BACKSPACE:
                text_data = text_data[:-1]
                pygame.Surface.fill(screen, (192, 192, 192), rect=input_box)
                text_data_1 = f1.render(text_data, True, (255, 0, 0))
                screen.blit(text_data_1, (input_box.x + 55, input_box.y + 5))
                pygame.draw.rect(screen, color, input_box, 2)
                pygame.display.update((425, 320, 160, 35))
                if len(text_data) > 4:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'Ты чё хуйню пишешь !?', (400, 280), (255, 0, 0))
                    pygame.display.update((380, 280, 250, 40))
                elif len(text_data) <= 4:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'вводи и нажми "ENTER"', (393, 280), (0, 0, 205))
                    pygame.display.update((380, 280, 250, 40))
            elif event.key == pygame.K_RETURN:
                flag_input_year = False
                flag_write = False
                pygame.Surface.fill(screen, (192, 192, 192), rect=(350, 150, 300, 250))
                input_year(text_data)
                if not flag_error:
                    text(30, 'Введен {} год'.format(work_data[0]), (410, 170), (0, 0, 205))
                    text(25, 'Нажми  "Дальше >>>"', (400, 235), (0, 0, 205))
                pygame.display.update()
            else:
                text_data += event.unicode
                pygame.Surface.fill(screen, (192, 192, 192), rect=input_box)
                text_data_1 = f1.render(text_data, True, (255, 0, 0))
                screen.blit(text_data_1, (input_box.x + 55, input_box.y + 5))
                pygame.draw.rect(screen, color, input_box, 2)
                pygame.display.update((425, 320, 160, 35))
                if len(text_data) > 4:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'Ты чё хуйню пишешь !?', (400, 280), (255, 0, 0))
                    pygame.display.update((380, 280, 250, 40))
                elif len(text_data) <= 4:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'вводи и нажми "ENTER"', (393, 280), (0, 0, 205))
                    pygame.display.update((380, 280, 250, 40))
        elif event.type == pygame.KEYDOWN and flag_input_month and flag_write:
            color = (255, 0, 0)
            if event.key == pygame.K_BACKSPACE:
                text_data = text_data[:-1]
                pygame.Surface.fill(screen, (192, 192, 192), rect=input_box)
                text_data_1 = f1.render(text_data, True, (255, 0, 0))
                screen.blit(text_data_1, (input_box.x + 28, input_box.y + 5))
                pygame.draw.rect(screen, color, input_box, 2)
                pygame.display.update((425, 320, 160, 35))
                if len(text_data) > 8:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'Ты чё хуйню пишешь !?', (400, 280), (255, 0, 0))
                    pygame.display.update((380, 280, 250, 40))
                elif len(text_data) <= 8:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'вводи и нажми "ENTER"', (393, 280), (0, 0, 205))
                    pygame.display.update((380, 280, 250, 40))
            elif event.key == pygame.K_RETURN:
                flag_input_month = False
                flag_write = False
                pygame.Surface.fill(screen, (192, 192, 192), rect=(320, 150, 370, 250))
                input_month(text_data)
                if not flag_error:
                    text(30, 'Введен {} месяц'.format(text_data), (370, 170), (0, 0, 205))
                    text(25, 'Нажми   " Дальше >>> "', (370, 235), (0, 0, 205))
                pygame.display.update()
            else:
                text_data += event.unicode
                pygame.Surface.fill(screen, (192, 192, 192), rect=input_box)
                text_data_1 = f1.render(text_data, True, (255, 0, 0))
                screen.blit(text_data_1, (input_box.x + 28, input_box.y + 5))
                pygame.draw.rect(screen, color, input_box, 2)
                pygame.display.update((425, 320, 160, 35))
                if len(text_data) > 8:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'Ты чё хуйню пишешь !?', (400, 280), (255, 0, 0))
                    pygame.display.update((380, 280, 250, 40))
                elif len(text_data) <= 8:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'вводи и нажми "ENTER"', (393, 280), (0, 0, 205))
                    pygame.display.update((380, 280, 250, 40))
        elif event.type == pygame.KEYDOWN and flag_input_day and flag_write:
            color = (255, 0, 0)
            if event.key == pygame.K_BACKSPACE:
                text_data = text_data[:-1]
                pygame.Surface.fill(screen, (192, 192, 192), rect=input_box)
                text_data_1 = f1.render(text_data, True, (255, 0, 0))
                screen.blit(text_data_1, (input_box.x + 45, input_box.y + 5))
                pygame.draw.rect(screen, color, input_box, 2)
                pygame.display.update((425, 320, 160, 35))
                if len(text_data) > 2:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'Ты чё хуйню пишешь !?', (400, 280), (255, 0, 0))
                    pygame.display.update((380, 280, 250, 40))
                elif len(text_data) <= 2:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'вводи и нажми "ENTER"', (393, 280), (0, 0, 205))
                    pygame.display.update((380, 280, 250, 40))
            elif event.key == pygame.K_RETURN:
                flag_input_day = False
                flag_write = False
                pygame.Surface.fill(screen, (192, 192, 192), rect=(320, 150, 370, 250))
                input_day(text_data)
                if not flag_error:
                    text(30, 'Введено {} число'.format(text_data), (370, 170), (0, 0, 205))
                    text(25, 'Нажми   " Дальше >>> "', (370, 235), (0, 0, 205))
                pygame.display.update()
            else:
                text_data += event.unicode
                pygame.Surface.fill(screen, (192, 192, 192), rect=input_box)
                text_data_1 = f1.render(text_data, True, (255, 0, 0))
                screen.blit(text_data_1, (input_box.x + 45, input_box.y + 5))
                pygame.draw.rect(screen, color, input_box, 2)
                pygame.display.update((425, 320, 160, 35))
                if len(text_data) > 2:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'Ты чё хуйню пишешь !?', (400, 280), (255, 0, 0))
                    pygame.display.update((380, 280, 250, 40))
                elif len(text_data) <= 2:
                    pygame.Surface.fill(screen, (192, 192, 192), rect=(380, 280, 250, 40))
                    text(20, 'вводи и нажми "ENTER"', (393, 280), (0, 0, 205))
                    pygame.display.update((380, 280, 250, 40))
