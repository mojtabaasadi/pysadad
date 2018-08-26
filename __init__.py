import requests
from pyDes import triple_des ,ECB
import base64,datetime,json
messages = {
            "0": "تراكنش با موفقيت انجام شد",
            "3": "( Invalid merchantپذيرنده کارت فعال نیست لطفا با بخش امور پذيرندگان، تماس حاصل فرمائید)",
            "23": "( Inactive Merchantپذيرنده کارت نامعتبر است لطفا با بخش امور پذيرندگان، تماس حاصل فرمائید)",
            "58": "انجام تراکنش مربوطه توسط پايانه ی انجام دهنده مجاز نمی باشد",
            "61": "مبلغ تراکنش از حد مجاز بالاتر است",
            "1000": "ترتیب پارامترهای ارسالی اشتباه می باشد، لطفا مسئول فنی پذيرنده با بانک تماس حاصل فرمايند",
            "1001": "لطفا مسئول فنی پذيرنده با بانک تماس حاصل فرمايند،پارامترهای پرداخت اشتباه می باشد",
            "1002": "خطا در سیستم- تراکنش ناموفق",
            "1003": "Pپذيرنده اشتباه است.لطفا مسئول فنی پذيرنده با بانک تماس حاصل فرمايند",
            "1004": "لطفا مسئول فنی پذيرنده با بانک تماس حاصل فرمايند،شماره پذيرنده اشتباه است",
            "1005": "خطای دسترسی:لطفا بعدا تلاش فرمايید",
            "1006": "خطا در سیستم",
            "1011": "درخواست تکراری- شماره سفارش تکراری می باشد",
            "1012": "اطلاعات پذيرنده صحیح نیست،يکی از موارد تاريخ،زمان يا کلید تراکنش اشتباه است.لطفا مسئول فنی پذيرنده با بانک تماس حاصل فرمايند",
            "1015": "پاسخ خطای نامشخص از سمت مرکز",
            "1017": "مبلغ درخواستی شما جهت پرداخت از حد مجاز تعريف شده برای اين پذيرنده بیشتر است",
            "1018": "اشکال در تاريخ و زمان سیستم. لطفا تاريخ و زمان سرور خود را با بانک هماهنگ نمايید",
            "1019": "امکان پرداخت از طريق سیستم شتاب برای اين پذيرنده امکان پذير نیست",
            "1020": "پذيرنده غیرفعال شده است.لطفا جهت فعال سازی با بانک تماس بگیريد",
            "1023": "آدرس بازگشت پذيرنده نامعتبر است",
            "1024": "مهر زمانی پذيرنده نامعتبر است",
            "1025": "امضا تراکنش نامعتبر است",
            "1026": "شماره سفارش تراکنش نامعتبر است",
            "1027": "شماره پذيرنده نامعتبر است",
            "1028": "شماره ترمینال پذيرنده نامعتبر است",
            "1029": "آدرس  IPپرداخت در محدوده آدرس های معتبر اعلام شده توسط پذيرنده نیست .لطفا مسئول فنی پذيرنده با بانک تماس حاصل فرمايند",
            "1030": "آدرس  Domainپرداخت در محدوده آدرس های معتبر اعلام شده توسط پذيرنده نیست .لطفا مسئول فنی پذيرنده با بانک تماس حاصل فرمايند",
            "1031": "مهلت زمانی شما جهت پرداخت به پايان رسیده است.لطفا مجددا سعی فرمايید",
            "1032": "پرداخت با اين کارت . برای پذيرنده مورد نظر شما امکان پذير نیست.لطفا از کارتهای مجاز که توسط پذيرنده معرفی شده است . استفاده نمايید.",
            "1033": "به علت مشکل در سايت پذيرنده. پرداخت برای اين پذيرنده غیرفعال شده است.لطفا مسوول فنی سايت پذيرنده با بانک تماس حاصل فرمايند.",
            "1036": "اطلاعات اضافی ارسال نشده يا دارای اشکال است",
            "1037": "شماره پذيرنده يا شماره ترمینال پذيرنده صحیح نمیباشد",
            "1053": "خطا: درخواست معتبر، از سمت پذيرنده صورت نگرفته است لطفا اطلاعات پذيرنده خود را چک کنید.",
            "1055": "مقدار غیرمجاز در ورود اطلاعات",
            "1056": "سیستم موقتا قطع میباشد.لطفا بعدا تلاش فرمايید.",
            "1058": "سرويس پرداخت اينترنتی خارج از سرويس می باشد.لطفا بعدا سعی بفرمايید.",
            "1061": "اشکال در تولید کد يکتا. لطفا مرورگر خود را بسته و با اجرای مجدد مرورگر عملیات پرداخت را انجام دهید (احتمال استفاده از دکمه «»Back مرورگر)",
            "1064": "لطفا مجددا سعی بفرمايید",
            "1065": "ارتباط ناموفق .لطفا چند لحظه ديگر مجددا سعی کنید",
            "1066": "سیستم سرويس دهی پرداخت موقتا غیر فعال شده است",
            "1068": "با عرض پوزش به علت بروزرسانی . سیستم موقتا قطع میباشد",
            "1072": "خطا در پردازش پارامترهای اختیاری پذيرنده",
            "1101": "مبلغ تراکنش نامعتبر است",
            "1103": "توکن ارسالی نامعتبر است",
            "1104": "اطلاعات تسهیم صحیح نیست",
            "408": " به نظر مشکلی در اتضال به درگاه وجود دارد"
        }

class SadadPaymentGateway:

    def __init__(self,*args,**kwargs):
        if 'MerchantId' in kwargs:
            self.MerchantId = kwargs['MerchantId']
        if 'TerminalId' in kwargs:
            self.TerminalId = kwargs['TerminalId']
        if 'TerminalKey' in kwargs:
            self.TerminalKey = kwargs['TerminalKey']
    
    def sign(self,data):
        key = base64.b64decode(self.TerminalKey)
        pad = 8 - ( len(data) % 8)
        data = data + chr(pad) * pad
        hash =  triple_des(key,ECB).encrypt(data)
        return base64.b64encode(hash).decode('utf-8')

    @staticmethod
    def __get_local_data__():
        local_time = datetime.datetime.now()
        return local_time.strftime('%d/%m/%Y %H:%M:%S')+local_time.strftime(' %p').lower()

    def request_pay_ref(self,*args,**kwargs):
        url = "https://sadad.shaparak.ir/VPG/api/v0/Request/PaymentRequest"
        if 'Amount' not in kwargs or  not isinstance(kwargs['Amount'],int) or kwargs['Amount']<=100 :
            raise Exception('amount must be int ')
        if 'OrderId' not in kwargs or  not isinstance(kwargs['OrderId'],int) :
            raise Exception('OrderId must be int ')
        if 'ReturnUrl' not in kwargs :
            raise Exception('ReturnUrl must be present ')
        try:
            res =  self.call(url,{
                "MerchantId": self.MerchantId,
                "TerminalId": self.TerminalId,
                "Amount": kwargs['Amount'],
                "OrderId": kwargs['OrderId'],
                "LocalDateTime": self.__get_local_data__() ,
                "ReturnUrl": kwargs['ReturnUrl'] ,
                "SignData": self.sign(';'.join([str(self.TerminalId),str(kwargs['OrderId']),str(kwargs['Amount'])])) ,
                "AdditionalData": '',
                "MultiplexingData": None
            })
            return res['ResCode'] == '0' , res['Token'] if 'Token' in res else str(res['ResCode'])
        except :
            return False,'408'
            
    def call(self,url, data):
        return requests.post(url,json=data,headers={
            'Content-Type':'application/json',
            'Content-Length':str(len(json.dumps(data)))
        }).json()
        
    def verify_payment(self,*args,**kwargs):
        if 'Token' not in kwargs:
            raise Exception('token is required')
            
        url = "https://sadad.shaparak.ir/VPG/api/v0/Advice/Verify"
        try:
            res =  self.call(url,data={
                "Token": kwargs['Token'],
                "SignData": self.sign(kwargs['Token']),
            })
            return res['ResCode'] == '0' , res['SystemTraceNo'] if 'SystemTraceNo' in res else str(res['ResCode'])
        except:
            return False,'408'
            
    def get_message(self,code):
        return messages[code]

            




