def main():
    users_data={ "student1":{'password':"1234",
                             'grades':[2,10,9,10,6]
                             },
                 "student2":{'password':"2345",
                             'grades':[10,2,12,5,6]
                             },
                 "student3":{'password':'3456',
                             'grades':[5,5,8,8,9]
                             },
                 "student4": {'password':'4567',
                              'grades':[7,7,8,2,3]
                              }
                 }
    print('СИСТЕМА ПЕРЕГЛЯДУ ОЦІНОК')
    input_login=input('Введіт логін: ').strip()
    input_password=input('Введіть пароль: ').strip()
    if input_login in users_data and users_data[input_login]['password']==input_password:
         print(f"вітаємо, {input_login}! авторизація успішна/n")
         grades=users_data[input_login]['grades']
         satisfactory_count=0
         unsatisfactory_count=0
         for grade in grades:
             if 5 <= grade <=10:
                 satisfactory_count+=1
             elif 1<=grade<=4:
                 unsatisfactory_count+=1
         print(f'твої оцінки: {grades}')
         print(f'хороші оцінки (5-12): {satisfactory_count}')
         print(f'погані оцінки: {unsatisfactory_count}')
    else:
        print('/n неправильний логін або пароль')
if __name__ == '__main__':
    main()






















