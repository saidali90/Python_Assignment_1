class Calculator:

   
    def div(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("لا يمكن إجراء عملية القسمة على الصفر.")
        return a / b

  
    @staticmethod
    def power(base: int, exp: int) -> int:
        if exp < 0:
            raise ValueError("Negative exponent is not allowed")
        return base**exp


    def get_item(self, items: list, index: int):
        if len(items) == 0:
            raise IndexError("القائمة فارغة، لا يمكن جلب أي عنصر.")
        if index < 0 or index >= len(items):
            raise IndexError(
                f"الفهرس {index} خارج حدود القائمة (النطاق المتاح: 0 إلى {len(items) - 1})."
            )
        return items[index]

   
    def get_average(self, numbers: list[int]) -> float:
        if not numbers: 
            raise ValueError("لا يمكن حساب المتوسط الحسابي لقائمة فارغة.")
        return sum(numbers) / len(numbers)


calc = Calculator()


print("--- 1. اختبار دالة القسمة ---")
try:
    result = calc.div(10, 0)
    print(f"النتيجة: {result}")
except ZeroDivisionError as e:
    print(f"تم التقاط استثناء: {e}")

try:
    result = calc.div(10, 2)
    print(f"النتيجة الصحيحة: {result}")
except ZeroDivisionError as e:
    print(f"تم التقاط استثناء: {e}")


print("\n--- 2. اختبار دالة الأسس ---")
try:
    result = Calculator.power(2, -3)
    print(f"النتيجة: {result}")
except ValueError as e:
    print(f"تم التقاط استثناء: {e}")

try:
    result = Calculator.power(2, 3)
    print(f"النتيجة الصحيحة: {result}")
except ValueError as e:
    print(f"تم التقاط استثناء: {e}")


print("\n--- 3. اختبار دالة جلب العنصر ---")
# اختبار قائمة فارغة
try:
    calc.get_item([], 0)
except IndexError as e:
    print(f"تم التقاط استثناء (قائمة فارغة): {e}")


try:
    calc.get_item([10, 20, 30], 5)
except IndexError as e:
    print(f"تم التقاط استثناء (فهرس غير موجود): {e}")

try:
    item = calc.get_item([10, 20, 30], 1)
    print(f"العنصر المطلوب: {item}")
except IndexError as e:
    print(f"تم التقاط استثناء: {e}")


print("\n--- 4. اختبار دالة المتوسط الحسابي ---")
try:
    calc.get_average([])
except ValueError as e:
    print(f"تم التقاط استثناء: {e}")

try:
    avg = calc.get_average([10, 20, 30, 40])
    print(f"المتوسط الحسابي: {avg}")
except ValueError as e:
    print(f"تم التقاط استثناء: {e}")