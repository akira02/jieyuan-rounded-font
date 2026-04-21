# 貢獻指南

感謝你一起協助改進 Jieyuan Rounded。

這是一個衍生字型專案，因此在貢獻時，除了設計與技術品質，也需要注意授權文字與 source 穩定性。

## 開始之前

請先閱讀以下文件：

- [`README.md`](../README.md)
- [`LICENSE`](../LICENSE)

開始修改前，請先確認你理解以下原則：

- 這個專案是從上游字型衍生而來
- 上游的 Reserved Font Name 不能直接作為衍生版本的主要名稱使用

## 歡迎的貢獻類型

很適合的貢獻包含：

- glyph 輪廓修正或微調
- spacing 與 kerning 改善
- metadata 整理
- OpenType feature 清理與修正
- 文件補充
- UFO source 一致性修復

## 編輯 Source 的原則

請盡量讓修改保持聚焦、容易審查。

在編輯 UFO source 時，建議遵守以下原則：

- 不要在沒有必要時大幅重排 glyph 順序
- 除非你很確定目的與影響，否則不要大改 `features.fea`
- 專案命名請和目前 repository 使用的名稱保持一致

像 `fontinfo.plist`、`lib.plist`、`features.fea` 這類檔案，改動雖小，也可能影響編輯器相容性或後續輸出結果，請特別小心。

## 送出前檢查

在提交修改前，請盡量完成以下檢查：

- 用 Glyphs 或其他相容工具重新開啟 UFO
- 確認 glyph 排序看起來正常
- 確認沒有新增 feature parsing 錯誤
- 確認修改過的 source 檔案仍能正常載入
- 如果有調整 metadata，請再檢查命名與 credit 是否合理

若未來補上 build 工具，也建議把編譯測試加入檢查流程。

## 授權與來源資訊

請不要隨意刪除 copyright 或 license 相關文字。

可以整理 Jieyuan Rounded 自己的 metadata，但以下幾類資訊請特別審慎處理：

- 法律與授權聲明
- Reserved Font Name
- 會影響對外識別的 manufacturer 與 naming 欄位

如果你不確定某段文字屬於一般編修還是法律／授權範圍，請把它視為敏感修改，並在提交時說明。

## Pull Request 或 Patch 說明

如果你要送出 pull request 或 patch，請盡量附上：

- 你改了什麼
- 為什麼要改
- 這次修改影響的是 outlines、spacing、kerning、features 還是 metadata
- 你如何確認修改後結果正常

我們會優先接受範圍清楚、容易審查的小型改動，而不是一次性的全面大整理。

## 語言版本

這份文件是繁體中文版本。

英文版本請參考 [CONTRIBUTING.md](./CONTRIBUTING.md)。
