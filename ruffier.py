
# здесь задаются строки, с помощью которых изложен результат:
txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''
нет данных для такого возраста'''
txt_res = [] 
txt_res.append('низкая.\n Срочно начните заниматься спортом \nили обратитесь к врачу!!\n или у вас все будет плохо!!!!!\n DISRESPECT\n Ваш уровень тренировок:1')
txt_res.append('удовлетворительная.\nСтоит немного заняться спортом!\n И тогда все будет норм!\n Ваш уровень тренировок:1')
txt_res.append('средняя.\nВозможно, стоит дополнительно обследоваться у врача.\n Ваш уровень тренировок:2')
txt_res.append('''
ХОРОШ\n Почти идеал\n Ваш уровень тренировок:3''')
txt_res.append('''
НИФИГА ТЫ МОЩНЫЙ\n УЛЬТРАМЕГАХОРОШ\n Ваш уровень тренировок:3''')

def ruffier_index(p1, p2, p3):
    return (4*(p1+p2+p3) - 200) / 10

def neud_level(age):
    norm_age = (min(age, 15) - 7) // 2
    result = 21 - norm_age*1.5
    return result
    
def ruffier_result(r_index, level):
    if r_index >= level:
        return 0 
    level = level-4
    if r_index >=level:
        return 1
    level -= 5
    if r_index >=level:
        return 2
    level -= 5.5
    if r_index >=level:
        return 3
    return 4

def test(p1, p2, p3, age):
    if age <7:
        return (txt_index + '0', txt_nodata)
    else:
        ruff_index = ruffier_index(p1,p2,p3)
        result = txt_res[ruffier_result(ruff_index, neud_level(age))]
        res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
        return res

