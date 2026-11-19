"""Solo of Fortune 2045 — таблицы СЛ (названия по «Соло удачи 2045»)."""
import dlc_build as B

COLL = "cyberpunk-red-solo-of-fortune-2045.solo-of-fortune-2045-tables"
LABEL = "Соло удачи 2045 — таблицы СЛ"
NAMES = ["DV Snubnose Pistol", "DV Grenade Launcher", "DV Long-Barrel Shotgun", "DV Missile Launcher", "DV Thrown Weapon",
         "DV Marksman Rifle", "DV Longbow", "DV Shotgun (Slug)", "DV Carbine", "DV Pistol", "DV Bows & Crossbows",
         "DV Assault Rifle", "DV Shortbow", "DV Rocket Launcher", "DV Long-Barrel Pistol", "DV Assault Rifle (Autofire)",
         "DV Anti-materiel Rifle", "DV Short-Barrel Shotgun", "DV Battle Rifle", "DV SMG (Autofire)",
         "DV Machine Pistol (Autofire)", "DV SMG", "DV Scout Rifle", "DV Sniper Rifle", "DV Machine Gun (Autofire)",
         "DV Subcompact SMG"]
TABLES = {n: {"name": B.DV_RU[n]} for n in NAMES}
