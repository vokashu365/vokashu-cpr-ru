# Cyberpunk RED — русский перевод по книгам

Модуль для Foundry VTT 12–14 и системы Cyberpunk RED Core (0.92+). Переводит компендиумы системы и DLC-модулей на русский с названиями и терминами из русских изданий книг и делает этот перевод главнее встроенного перевода системы. Нужны модуль **Babele** и русский язык Foundry.

Автор — **Vokashu**. Boosty: https://boosty.to/young_rome · Patreon: https://www.patreon.com/vokashu

## Установка
В Foundry: «Дополнения» → «Установить модуль» → в поле «Ссылка на манифест» вставьте

```
https://github.com/vokashu365/vokashu-cpr-ru/releases/latest/download/module.json
```

и включите модуль в мире.

Что переводится и как работает приоритет — в [module/README.md](module/README.md). Какие термины выбраны и почему — в [ТЕРМИНЫ.md](ТЕРМИНЫ.md).

## Сборка
Папка `module/` — готовый модуль. Она собирается из `src/` и файлов системы cyberpunk-red-core 0.92.4 (путь к папке системы — в переменной `CPR_SYSTEM_DIR`):

```
python -X utf8 src/build.py
python -X utf8 src/release.py
```

`build.py` пишет `module/lang/ru.json` и `module/babele/ru/*.json`, `release.py` кладёт `module.json` и `vokashu-cpr-ru.zip` в `dist/` для релиза.
