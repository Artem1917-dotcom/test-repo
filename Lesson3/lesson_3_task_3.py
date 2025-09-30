from Lesson3.Address import Address
from Lesson6K.Mailing import Mailing

# Создаем адреса
to_address = Address("123456", "Москва", "Ленина", "10", "20")
from_address = Address("654321", "СПб", "Пушкина", "5", "15")

# Создаем отправление
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500.0,
    track="TRACK123"
)

# Выводим информацию
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")