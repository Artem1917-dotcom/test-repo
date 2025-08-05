from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "20")
from_address = Address("654321", "СПб", "Пушкина", "5", "15")
mailing = Mailing(to_address, from_address, 500, "TRACK123")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")