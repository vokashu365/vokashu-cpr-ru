"""Наборы персонажей: переводятся только вложенные предметы (по переведённым компендиумам), имена остаются.

Здесь несколько коллекций, поэтому модуль задаёт MULTI вместо COLL.
"""
from dlc_build import Pack

MULTI = [
    Pack("night-city-gang-and-corp-mook-pack.NCGangsnCorpsMooks", None),
    Pack("vokashu-mook-pack-for-cyberpunk-red.vokashu-mook-pack-for-cyberpunk-red", None),
    Pack("going-metal-cpred.going-metal-fbc-actors", "Going Metal — персонажи FBC", actors={"Base FBC": "Базовая FBC"}),
]
