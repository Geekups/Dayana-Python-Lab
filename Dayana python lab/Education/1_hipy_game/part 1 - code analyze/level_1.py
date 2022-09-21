#این کد ساده برای کاری کوتاه و استاتیک ساخته شده است.  از دو کتابخانه زیر برای دریافت محتوای یک صفحه و سپس بررسی و استخراج مواردی خاص از آن محتوا استفاده کرده ایم. وظیفه شما در این مرحله بسیار آسان است. ایتدا کد را بخوانید و سپس مراحل نوشته شدن آنرا به ترتیب بنویسید. و در نهایت هر نوع اشکالی که در کد میبینید یا هر گونه روش بهبود که در ذهن دارید را در ادامه تحلیل خود بنویسید. شماره و نام مرحله را در انتهای صفحه قرار داده و به مرحله بعد بروید.
import requests
import lxml.html as lh
 
request =requests.get('https://en.m.wikipedia.org/wiki/Machine_learning')

page_content = request.content

document = lh.fromstring(page_content)

for element in document.xpath('//a/@href'):
    print(element)