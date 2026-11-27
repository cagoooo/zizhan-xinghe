# 字戰星河｜全漢字橫向捲軸射擊遊戲

敵機、子彈、爆炸全都是漢字的星河射擊冒險。駕駛文字戰機穿越八大星域，用「狙」追蹤雷射、「捕」收編副機，擊敗最終魔王「源」。

- 線上遊玩：https://cagoooo.github.io/zizhan-xinghe/
- 電腦：滑鼠或方向鍵移動、左鍵射擊、右鍵／V 鎖定、B 捕獲／自爆、P 暫停
- 平板與手機：手指拖曳移動（預設自動連射），建議橫放或按「全螢幕」

向全漢字射擊遊戲的先驅《擊破傳》（宮本達也）致敬；本作名稱、機體、關卡配字、頭目與開場演出皆為原創。

## 開發

- 單一 `index.html`，推送到 `main` 後由 GitHub Actions 部署到 GitHub Pages。
- 部署時 `.github/stamp_version.py` 把 `__BUILD_VERSION__` 換成版本號，Service Worker 偵測到新版會跳出「重新整理載入」提示。
- 圖示與分享圖：`python scripts/make-brand-assets.py`（需先在本機 8796 埠開伺服器）。

---

Made with ❤️ by [阿凱老師](https://cagoooo.github.io/Akai/)
