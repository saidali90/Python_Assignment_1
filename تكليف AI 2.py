class Device:
    def __init__(self, brand, **kwargs):
        super().__init__(**kwargs)
        self.brand = brand

    def show_brand(self):
        print(f"العلامة التجارية: {self.brand}")



class Phone(Device):
    def __init__(self, screen_size, **kwargs):
        super().__init__(**kwargs)
        self.screen_size = screen_size

    def make_call(self):
        print("جاري إجراء مكالمة هاتفية...")



class Camera(Device):
    def __init__(self, resolution, **kwargs):
        super().__init__(**kwargs)
        self.resolution = resolution

    def take_photo(self):
        print(f"تم التقاط صورة بدقة {self.resolution}!")



class SmartPhone(Phone, Camera):
    def __init__(self, brand, screen_size, resolution):
      
        super().__init__(brand=brand, screen_size=screen_size, resolution=resolution)

    def show_smartphone_details(self):
        print("=== تفاصيل الهاتف الذكي ===")
        super().show_brand()
        print(f"حجم الشاشة: {self.screen_size} بوصة")
        print(f"دقة الكاميرا: {self.resolution}")



my_phone = SmartPhone("Samsung", 6.7, "108MP")


my_phone.show_smartphone_details()




my_phone.show_brand()


my_phone.make_call()


my_phone.take_photo()

