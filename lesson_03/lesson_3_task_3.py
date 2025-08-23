from address import Address
from mailing import Mailing


to_address = Address("460000", "Оренбург", "Гая", "21", "201")
from_address = Address("462401", "Орск", "Гагарина", "7", "407")
mailing = Mailing(to_address, from_address, 600, "1234567890")

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)
