"""Danger Gal Dossier — персонажи (модуль danger-gal-dossier), имена по русскому изданию «Досье Danger Gal»."""
COLL = "danger-gal-dossier.danger-gal-dossier-actors"
LABEL = "Досье Danger Gal — персонажи"
FOLDERS = {
    "6th Street": "6-я улица", "Danger Gal Puma Squad": "Danger Gal: отряд Puma", "Piranhas": "Пираньи",
    "Generation Red": "Поколение RED", "Team Monster": "Монстры", "The Digital Divas": "Цифровые дивы", "Zoners": "Зонеры",
    "Network 54": "Network 54", "Trauma Team Squad NC4-2": "Trauma Team: отряд NC4-2", "NCPD Precinct #1": "Участок №1 NCPD",
    "Arasaka": "Арасака", "Sightseers": "Туристы", "The Bozos": "Бозо", "Edgerunners": "Бегущие по Грани",
    "Tyger Claws": "Тигриные Когти", "Maelstrom": "Мальстрём",
}
ACTORS = {
    # 6-я улица
    "Arbiter": "Судья", "Coldfire": "Колдфаер", "Breacher": "Бричер", "Knock!Knock": "Тук!Тук!", "Roof Diver": "Срыв",
    # Бозо
    "Big Top": "Шапито", "Blammo": "Бламмо", "Jester": "Шут", "Dunce": "Балбес", "Centwit": "Полудурок",
    "Dead Ringer (Blue)": "Близняшки (Синенькая)", "Dead Ringer (Pink)": "Близняшки (Розовенькая)", "Finale": "Финал",
    "Burt the Squirt": "Бёрт-Брызгун", "Tomfool": "Болван", "The Fool": "Дурак",
    # Danger Gal, отряд Puma
    "Pantera": "Пантера", "Tigress": "Тигрица", "Doc Mittens": "Доктор Лапки", "Mouse": "Мышь", "Lynx": "Пума",
    # Цифровые дивы
    "André Nez": "Андре Нез", "Firewall": "Файрвол", "José Quispe": "Хосе Киспе", "Pat Rezin": "Пат Резин",
    "Sizzle Jams": "Сиззл Джемс",
    # Бегущие по Грани
    "Tetsuo": "Тетсуо", "CrAB Lord": "Краб Лорд", "CrAB Drone": "Краб-дрон", "Tía Puño": "Тиа Пуньо", "Backhand": "Бэкхэнд",
    "Jumpshot": "Джампшот", "24/7": "24/7", "Derby": "Дерби", "Forty": "Форти", "Grease": "Гриз", "Redeye": "Редай",
    "Saber": "Сейбер", "Torch": "Факел", "Crasher": "Крэшер", "Flasher": "Флэшер", "Hammer": "Хаммер", "Leverage": "Леверэйдж",
    # Поколение RED
    "Blades": "Блэйдс", "Apex": "Апекс", "Tetra": "Тетра", "Hi-Stick": "Хай-Стик", "Izzy": "Иззи", "Lookout": "Лукаут",
    "Shredder": "Шреддер", "Wheelie": "Уилли",
    # Мальстрём
    "Crusher": "Крашер", "Warlock": "Варлок", "The Pit": "Пит", "Quake": "Квейк", "Flenser": "Флэнсер", "Joe Pitt": "Джо Питт",
    "Ripper": "Риппер", "Drop": "Дроп", "Raguel": "Рагуэл", "Ghoul": "Гуль", "Maelstrom Ripperdoc": "Риппердок Мальстрёма",
    "Maelstrom Scavver": "Мусорщик Мальстрёма",
    # Участок №1 NCPD
    "Caliber": "Калибр", "Hellhound": "Хеллхаунд", "Escobar": "Эскобар", "Grinder": "Гриндер", "Cavalry": "Кавалерия",
    "Golden Boy": "Голден Бой", "Sarge": "Серж", "Shepard": "Шепард", "Gustav": "Густав", "Pitbull": "Питбуль",
    "Cherub": "Херувим",
    # Network 54
    "Fiona Hayes": "Фиона Хейз", "Angle": "Энгл", "Stringer": "Стрингер",
    # Пираньи
    "Bazooka Joe": "Базука Джо", "Corpse Reviver": "Корпс Ревайвер", "Dirty Shirley": "Грязная Ширли",
    # Туристы
    "Endo": "Эндо", "Gaze": "Гейз", "Racer": "Рейсер", "Glare": "Глэр", "Swirl": "Свирл",
    # Монстры
    "Cereal": "Цериал", "Isolate": "Изолейт", "Lucky": "Счастливчик", "Nox": "Нокс", "Paladin": "Паладин",
    "Too Tall": "Высокий", "Team Monster's Zetatech Herakles": "Зетатех «Геракл» Монстров",
    # Trauma Team
    "Cazadora": "Казадора", "Penitent": "Пенитент", "Stick": "Стик", "Twist": "Твист", "Rockabye": "Баю-Бай",
    "Paddles": "Пэддлз", "Trauma Team Squad NC4-2's SovOil Mi-60": "СовНефть Ми-60 отряда NC4-2",
    # Тигриные Когти
    "Shinobu the Second": "Синобу Второй", "Zen": "Дзен", "Burai": "Бурай", "Wakako": "Вакако", "Hamada": "Хамада",
    "Masa": "Маса", "Yasu": "Ясу", "Shinmai": "Шинмай", "Tyger Claw Bouncer": "Вышибала Тигриных Когтей",
    "Tyger Claw Vendor": "Торговец Тигриных Когтей",
    # Зонеры
    "Vanisher": "Ванишер", "Tearjerker": "Тирджеркер", "Forty Mike-Mike": "Форти Майк-Майк", "Mister Studd": "Мистер Перчик",
    "Freefall": "Фрифолл", "Nemo": "Немо", "Speed Demon": "Демон Скорости", "Alpha": "Альфа", "Blaze": "Блейз",
    "Wrecker": "Рекер", "Speed Demon's Diego Motors Chupacabra": "Диего Моторс «Чупакабра» Демона Скорости",
    # Арасака
    "Darius": "Дариус", "Nymph": "Нимфа",
}
