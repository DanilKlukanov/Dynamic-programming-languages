stroke = input()
######OK
if len(stroke) < 6:
    print('Недопустимый пароль')
######
elif stroke.isalpha() == True  and stroke.islower() == True or stroke.isupper() == True and stroke.isalpha() == True :
    print('Ненадежный пароль')
elif stroke.isdigit() == True:
    print('Ненадежный пароль')

elif stroke.isalpha() == True and stroke.islower() == False and stroke.isupper() == False :
    print('Слабый пароль')
elif stroke.isalnum() == True and stroke.islower() == True or stroke.isupper() == True and stroke.isalnum() == True :
    print('Слабый пароль')

elif stroke.isalnum() == True and stroke.islower() == False or stroke.isupper() == False and stroke.isalnum() == True:
     print('Надежный пароль')