id = input('ป้อนรหัส : ')
name = input('ป้อนชื่อ : ')
Yb = input('ป้อนปีเกิด : ')
Age = 2023 - int(Yb)
print('-------------------------------------')
print(f"ยินดีต้อนรับ : {id} ชื่อ : {name}")
print(f'คุณเกิดปี : {Yb} อายุของคุณ : {Age}')
print('-------------------------------------')
print("ยินดีต้อนรับ :" ,id ,"ชื่อ :" ,name)
print('คุณเกิดปี :' ,Yb ,'อายุของคุณ :' ,Age)
print('-------------------------------------')
print("ยินดีต้อนรับ : " +id+" ชื่อ : " +name)
print('คุณเกิดปี : ' +Yb+' อายุของคุณ : ' +str(Age))
print('-------------------------------------')
print("ยินดีต้อนรับ : {0} ชื่อ : {1}".format(id,name))
print('คุณเกิดปี : {0} อายุของคุณ : {1}'.format(Yb,Age))
print('-------------------------------------')
print("ยินดีต้อนรับ : %s ชื่อ : %s" %(id,name))
print('คุณเกิดปี : %s อายุของคุณ : %s' %(Yb,Age))
print('-------------------------------------')