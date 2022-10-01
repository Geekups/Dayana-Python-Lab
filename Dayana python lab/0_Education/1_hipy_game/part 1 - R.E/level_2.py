# csv در کد زیر شما ۳ روش برای باز کردن و خواندن یک فایل 
# را مشاهده میکنید
# در وهله اول به عنوان چالشی برای شما
# csv سعی کنید یک فایل 
# حامل دیتای مثلا قیمت دلار یا بیت کوین
# یا هرچیز که خودتان مایلیدرا بیابید و دانلود کنید
# سپس آن را کنار این فایل پایتون قرار دهید
# data.csv و مشخصا اسم 
# که در کد صدا زده شده را به نام فایل دانلودیتان تغییر دهید
# هر سه قسمت از کد زیر را به طور جداگانه اجرا کنید. تفاوت آنها را بنویسید
# در ادامه لحظاتی خود را به عنوان یک دانشمند علم داده تصور کرده
# و این ۳ روش را از دیدگاه خود تجزیه و تحلیل نموده
# و روش برتر را با ذکر دلایل مشخص انتخاب کنید
# pandas نکته: کتابخانه 
# را باید در محیط کار خود نصب بنمایید
# راهنمایی های لازم در اینترنت موجود است
# موفق باشید
####################
import csv 
 
# opening the CSV file 
with open('data.csv', mode ='r')as file: 
 
 # reading the CSV file 
 csvFile = csv.reader(file) 
 
 # displaying the contents of the CSV file 
for lines in csvFile: 
    print(lines)
    
  ###################### v2 ########
  
import csv 
 
# opening the CSV file 
with open('data.csv', mode ='r')as file: 
 
 # reading the CSV file 
 csvFile = csv.DictReader(file) 
 
 # displaying the contents of the CSV file 
 for lines in csvFile: 
  print(lines)
 
 ############ v3 ##############
 
 import pandas 

 

# reading the CSV file 

csvFile = pandas.read_csv('data.csv') 

# displaying the contents of the CSV file 
print(csvFile)