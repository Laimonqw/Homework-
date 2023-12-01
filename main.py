def ask_password():
    correct_password = '12345'
    attempts = 3
    
    while attempts > 0:
        password = input('Введите пароль: ')
        
        if password == correct_password:
            print('Пароль принят,добро пожаловать!')
            return
        
        attempts -= 1
    
    print('Oтказано в доступе')

ask_password()