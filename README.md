
# درگاه پرداخت اینترنتی سداد
# Sadad internet payment gateway (python3)
نمونه کد برای دیگر زبان ها را میتوانید   [اینجا](https://sadadpsp.ir/fa/content/131/%D8%AF%D8%B1%DA%AF%D8%A7%D9%87-%D9%BE%D8%B1%D8%AF%D8%A7%D8%AE%D8%AA-%D8%A7%DB%8C%D9%86%D8%AA%D8%B1%D9%86%D8%AA%DB%8C) پیدا کنید

## نحوه استفاده
```
git clone git@github.com:mojtabaasadi/pysadad.git
cd pysadad
pip install -r requirements.txt
```
درخواست توکن
```python
from pysadad import SadadPaymentGateway
s = SadadPaymentGateway(MerchantId="",TerminalId="",TerminalKey="")
success , token = s.request_pay_ref(Amount=1000,OrderId=1,ReturnUrl="")
if not success:
    message = s.get_message(token)
```
تایید پرداخت:

```python
from pysadad import SadadPaymentGateway
s = SadadPaymentGateway(MerchantId="",TerminalId="",TerminalKey="")
success , traceno= s.verify_payment(Token="")
if not success:
    message = s.get_message(traceno)
```
