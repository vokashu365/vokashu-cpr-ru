/**
 * Cyberpunk RED — русский перевод по книгам.
 * Регистрирует переводы компендиумов в Babele. Перевод модуля важнее встроенного перевода системы:
 * - Babele 2.7+ (Foundry 13–14) ставит источники модулей выше системного, а системный остаётся запасным;
 * - Babele 2.6 (Foundry 12) читает системный перевод последним, и он перебил бы модуль, поэтому там
 *   системный каталог отключается (модуль содержит полный перевод всех компендиумов системы).
 */
const MODULE_ID = "vokashu-cpr-ru";

Hooks.once("babele.init", (babele) => {
  babele.register({ module: MODULE_ID, lang: "ru", dir: "babele/ru" });
});

Hooks.once("setup", () => {
  const babele = game.modules.get("babele");
  if (!babele?.active || !foundry.utils.isNewerVersion("2.7.0", babele.version ?? "0")) return;
  const api = game.babele ?? globalThis.Babele?.get?.();
  if (typeof api?.setSystemTranslationsDir === "function") api.setSystemTranslationsDir(null);
});
