def main():
    users_data={'student1':{'password':'1234','grades': [2,2,5,7,8]},
                'student2':{'password':'2345','grades': [4,7,7,7,9]},
                'student3':{'password':'3456',"grades":[10,12,4,8,8]},
                'student4':{'password':'4567','grades':[8,10,12,7,2]}
                }
    print('вхід до системи')
    input_login=input('введіть логін: ').strip()
    input_password=input('введіть пароль:').strip()
    if input_login in users_data and users_data[input_login]['password']==input_password:
        print(f'вітаємо,{input_login}')
        grades=users_data[input_login]['grades']
        print(f'перелік усіх виставлених оцінок: {grades}')
        satisfactory_count=0
        unsatisfactory_count=0
        for grade in grades:
            if 5 <= grade <=10:
                satisfactory_count+=1
            elif 1<=grade<=4:
                unsatisfactory_count+=1
        print(f'кількість задовільних оцінок (5-12): {satisfactory_count}  ')
        print(f'кількість не задовільних оцінок (1-4): {unsatisfactory_count}')
    else:
        print('помилка!!')
if __name__ == '__main__':
        main()






























