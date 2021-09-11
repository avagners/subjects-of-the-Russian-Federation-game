import turtle
import pandas

data = pandas.read_csv('subjects_list_coor.csv')

screen = turtle.Screen()
screen.title("Russian Federation Game")
image = '900px-Map_of_federal_subjects_of_Russia_(2014).gif'
screen.addshape(image)
turtle.shape(image)


subjects = """Республика Адыгея (Адыгея)
Республика Алтай
Республика Башкортостан
Республика Бурятия
Республика Дагестан
Республика Ингушетия
Кабардино-Балкарская Республика
Республика Калмыкия
Карачаево-Черкесская Республика
Республика Карелия
Республика Коми
Республика Крым
Республика Марий Эл
Республика Мордовия
Республика Саха (Якутия)
Республика Северная Осетия – Алания
Республика Татарстан (Татарстан)
Республика Тыва
Удмуртская Республика
Республика Хакасия
Чеченская Республика
Чувашская Республика – Чувашия
Алтайский край
Забайкальский край
Камчатский край
Краснодарский край
Красноярский край
Пермский край
Приморский край
Ставропольский край
Хабаровский край
Амурская область
Архангельская область
Астраханская область
Белгородская область
Брянская область
Владимирская область
Волгоградская область
Вологодская область
Воронежская область
Ивановская область
Иркутская область
Калининградская область
Калужская область
Кемеровская область
Кировская область
Костромская область
Курганская область
Курская область
Ленинградская область
Липецкая область
Магаданская область
Московская область
Мурманская область
Нижегородская область
Новгородская область
Новосибирская область
Омская область
Оренбургская область
Орловская область
Пензенская область
Псковская область
Ростовская область
Рязанская область
Самарская область
Саратовская область
Сахалинская область
Свердловская область
Смоленская область
Тамбовская область
Тверская область
Томская область
Тульская область
Тюменская область
Ульяновская область
Челябинская область
Ярославская область
Город Москва
Город Санкт-Петербург
Город Севастополь
Еврейская автономная область
Ненецкий автономный округ
Ханты-Мансийский автономный округ – Югра
Чукотский автономный округ
Ямало-Ненецкий автономный округ"""
subjects_list = subjects.split('\n')

# Вычисляем и Записываем координаты субъектов РФ в CSV файлы
# def get_mouse_click_coor(x, y):
#     print(subjects_list[len(subjects_list_coor)+1], len(subjects_list_coor)+1)
#     subjects_list_coor.append((subjects_list[len(subjects_list_coor)], x, y))
#     new_data = pandas.DataFrame(subjects_list_coor)
#     new_data.to_csv("subjects_list_coor.csv")
#
#
# subjects_list_coor = []
# print(subjects_list_coor)
# print(subjects_list[0], 0)
# turtle.onscreenclick(get_mouse_click_coor)


guessed_subjects = []

while len(guessed_subjects) < 85:
    answer_subject = screen.textinput(title=f'{len(guessed_subjects)}/85 субъектов РФ', prompt="Напишите название субъекта РФ")

    if answer_subject == 'Exit':
        missing_subjects = []
        for i in subjects_list:
            if i not in guessed_subjects:
                missing_subjects.append(i)
        new_data = pandas.DataFrame(missing_subjects)
        new_data.to_csv("subjects_to_learn.csv")
        break
    if answer_subject in subjects_list:
        guessed_subjects.append(answer_subject)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        subject_data = data[data.name == answer_subject]
        t.goto(float(subject_data.x), float(subject_data.y))
        t.write(answer_subject)

# turtle.mainloop()
