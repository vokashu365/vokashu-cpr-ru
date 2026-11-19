"""Дополнительные записи в переводы компендиумов системы: варианты предметов, которые встречаются внутри персонажей
DLC и наборов моков, но которых нет в самих компендиумах. Babele находит их по названию и переводит вложенные предметы."""

LANG = {"Arapaho": "арапахо", "Cantonese": "кантонский", "Greek": "греческий", "Louisiana Creole": "луизианский креольский",
        "Native": "родной", "Samoan": "самоанский", "Sanskrit": "санскрит", "Unknown": "неизвестный", "Sign": "жестовый",
        "Probably Won’t Live Long Enough to Talk": "скорее всего, не доживёт до разговора"}
LOCAL = {"Barcelona": "Барселона", "GM’s Choice": "на выбор мастера", "Heywood Industrial Zone": "Промзона Хейвуда",
         "Heywood": "Хейвуд", "Hot Zone": "Горячая зона", "Japantown": "Джапантаун", "Kabuki": "Кабуки",
         "Night City Harbor": "Порт Найт-Сити", "Night City": "Найт-Сити", "NorCal Military Base": "Военная база Северной Калифорнии",
         "North Heywood": "Северный Хейвуд", "Old Japantown": "Старый Джапантаун", "Pacifica Playground": "Площадка Пасифики",
         "Precinct #1": "Участок №1", "Rancho Coronado": "Ранчо Коронадо", "Santo Domingo": "Санто-Доминго",
         "Sewers of Little China": "Канализация Маленького Китая", "The Place They Die In": "место, где они умрут",
         "Tunnels Beneath Totentanz": "тоннели под «Тотентанцем»", "Unknown": "неизвестно", "Watson Development": "Застройка Уотсона"}
INSTR = {"Bike Horn": "велосипедный гудок", "Biwa": "бива", "DJ Deck": "диджейский пульт", "Keytar": "кейтар",
         "Sanshin": "сансин", "Shamisen": "сямисэн", "Sing": "пение", "Taiko": "тайко"}
SCIENCE = {"Anatomy": "анатомия", "Biochemistry": "биохимия", "Culinary": "кулинария", "Engineering": "инженерия",
           "Forensics": "судебная экспертиза", "Library": "библиотечное дело"}

TECH_UP = "улучшено Техником"

EXTRA = {
    "core_skills-languages": {f"Language ({k})": f"Язык ({v})" for k, v in LANG.items()},
    "core_skills-local-expert": {f"Local Expert ({k})": f"Знание местности ({v})" for k, v in LOCAL.items()},
    "core_skills-play-instrument": {f"Play Instrument ({k})": f"Игра на инструменте ({v})" for k, v in INSTR.items()},
    "core_skills-science": {f"Science ({k})": f"Наука ({v})" for k, v in SCIENCE.items()},
    "core_armor": {
        "Bodyweight Suit (Tech Upgraded)": f"Комбинезон «Бодивейт» ({TECH_UP})",
        "Heavy Armorjack (Body) (Tech Upgraded)": f"Тяжёлый бронекостюм (тело) ({TECH_UP})",
        "Heavy Armorjack (Head) (Tech Upgraded)": f"Тяжёлый бронекостюм (голова) ({TECH_UP})",
        "Kevlar® (Body) (Tech Upgraded)": f"Кевлар® (тело) ({TECH_UP})",
        "Light Armorjack (Body) (Tech Upgraded)": f"Лёгкий бронекостюм (тело) ({TECH_UP})",
        "Light Armorjack (Head) (Tech Upgraded)": f"Лёгкий бронекостюм (голова) ({TECH_UP})",
        "Medium Armorjack (Body) (Tech Upgraded)": f"Средний бронекостюм (тело) ({TECH_UP})",
        "Medium Armorjack (Head) (Tech Upgraded)": f"Средний бронекостюм (голова) ({TECH_UP})",
        "Subdermal Armor (Tech Upgraded)": f"Подкожная броня ({TECH_UP})",
        "TUp Light Armorjack (Body)": f"Лёгкий бронекостюм (тело) ({TECH_UP})",
        "TUp Light Armorjack (Head)": f"Лёгкий бронекостюм (голова) ({TECH_UP})",
        "TUp Bodyweight Suit": f"Комбинезон «Бодивейт» ({TECH_UP})",
        "Kevlar (Body)": "Кевлар® (тело)", "Kevlar (Head)": "Кевлар® (голова)",
        "Improved Medium Armorjack (Body)": "Улучшенный средний бронекостюм (тело)",
        "Improved Medium Armorjack (Head)": "Улучшенный средний бронекостюм (голова)",
    },
    "core_cyberware": {
        "Cortex Bomb": "Кортикальная бомба",
        "Exotic Bodysculpting": "Экзотическая бодискульптура",
        "Popup Melee Weapon (Heavy Melee Weapon)": "Выкидное ОББ (тяжёлое оружие ближнего боя)",
        "Popup Ranged Weapon (Hellbringer)": "Выкидное ОДБ (Hellbringer)",
        "Popup Very Heavy Pistol": "Выкидной очень тяжёлый пистолет",
        "Skill Chip (Drive Land Vehicle)": "Щепка навыка (Вождение)",
        "Skill Chip (Language [English])": "Щепка навыка (Язык [английский])",
        "Skill Chip (Language [Spanish])": "Щепка навыка (Язык [испанский])",
        "Skill Chip (Language [Streetslang])": "Щепка навыка (Язык [уличный сленг])",
        "Skill Chip (Pilot Air Vehicle)": "Щепка навыка (Пилотирование)",
        "Difficult Skill Chip (Heavy Weapons)": "Щепка сложного навыка (Тяжёлое оружие)",
        "Difficult Skill Chip (Autofire)": "Щепка сложного навыка (Автоогонь)",
        "FBC Cyberarm": "Киберрука FBC", "FBC Cybereye": "Киберглаз FBC", "FBC Cyberleg": "Кибернога FBC",
        "FBC Cyberaudio Suite": "Комплект кибераудио FBC", "FBC Cyberskull": "Киберчереп FBC", "FBC Neural Link": "Нейролинк FBC",
        "Biosystem": "Биосистема",
    },
    "core_gear": {
        "Bear Ears Headband": "Ободок с медвежьими ушками", "Cat Ears Headband": "Ободок с кошачьими ушками",
        "Bike Horn": "Велосипедный гудок", "Biwa": "Бива", "Sanshin": "Сансин", "Shamisen": "Сямисэн", "Taiko": "Тайко",
        "DJ Deck": "Диджейский пульт", "Keytar": "Кейтар", "Businesswear Outfit": "Комплект одежды Businesswear",
        "Leisurewear Outfit": "Комплект одежды Leisurewear", "Kabuki Outfit": "Костюм кабуки", "CrAB Drone": "Краб-дрон",
        "Mirrorshades": "Зеркальные очки", "Photograph": "Фотография", "Portable NET Architecture": "Переносная архитектура сети",
        "Random Anime/Manga Merch": "Случайный аниме- или манга-мерч",
        "Random Piece of Still Bloody Cyberware": "Случайный киберимплант, ещё в крови",
        "Trauma Team (Executive)": "Страховка Trauma Team (Executive)", "Trauma Team (Silver)": "Страховка Trauma Team (Silver)",
        "Observation Camera": "Камера наблюдения",
    },
    "core_vehicles": {"SovOil Mi-60": "СовНефть Ми-60"},
    "internal_cyberware-core": {"External (14 Option Slots)": "Внешние импланты (14 слотов опций)",
                                "Internal (14 Option Slots)": "Внутренние импланты (14 слотов опций)"},
}
