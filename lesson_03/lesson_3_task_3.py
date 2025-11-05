from mailing import Mailing
from address import Address

from_addr = Address(
    index="460000",
    city="Оренбург",
    street="Гая",
    house="21",
    apartment="201"
)

to_addr = Address(
    index="462401",
    city="Орск",
    street="Гагарина",
    house="7",
    apartment="407"
)

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=600,
    track="1234567890"
)

print(f"Отправление {mailing.track} "
      f"из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, "
      f"{mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, "
      f"{mailing.to_address.city}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
