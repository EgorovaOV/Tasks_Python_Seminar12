#Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str
# с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def premium(name, salary, bonus):
    name = ()#передаем в функцию три списка - имена
    salary = ()#оклады
    bonus = ()#процент премии
    my_money = {}# это сам словарь с именем и суммой премии
    i = 0
    while i < len(name):
        my_money[name[i]] = salary[i] * bonus[i]#вычисляем каждый элемент словаря
        i += 1
    print(my_money)#печатаем. Но он почему -то выходит пустой...


a = 'Dima', 'Sveta', 'Igor'
b = 100, 500, 300
c = 0.1, 0.2, 0.3
i = 0 #хотя я проверяла тут без фунции все работает
my_money = {}
while i < len(a):
    my_money[a[i]] = b[i] * c[i]
    i += 1
print(my_money)# тут есть список

premium(a, b, c)# а тут нет