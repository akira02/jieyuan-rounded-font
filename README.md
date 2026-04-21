# 結圓體 Jieyuan Rounded

結圓體是一個從「jf open 粉圓（open-huninn）」衍生出來的字體專案。

Jieyuan Rounded is a derivative font project based on `jf open huninn`.

這個 repository 目前主要用來維護可編輯的 UFO source、整理專案 metadata，並讓後續協作與審查更穩定。

This repository currently focuses on maintaining the editable UFO source, cleaning up project metadata, and making the font source easier to review and collaborate on over time.

## Project Status

這個專案目前仍在整理中。

The project is still being organized.

目前這個 repository 包含：

At the moment, this repository includes:

- the main UFO source in [`sources/`](./sources)
- project documentation
- licensing and upstream attribution records

隨著專案逐步穩定，build 工具與 release 流程之後可能還會再調整。

Build tooling and release workflow may continue to evolve as the project becomes more stable.

## Repository Layout

目前目錄結構如下：

The current repository layout is:

- [`sources/`](./sources): editable UFO source files
- [`docs/CONTRIBUTING.md`](./docs/CONTRIBUTING.md): contribution guide in English
- [`docs/CONTRIBUTING.zh-TW.md`](./docs/CONTRIBUTING.zh-TW.md): contribution guide in Traditional Chinese
- [`LICENSE`](./LICENSE): license text and attribution chain

## Upstream and Attribution

結圓體衍生自 `jf open huninn`，而 `jf open huninn` 本身也承接了更早的來源與署名資訊，例如 Kosugi Maru 與 Varela Round。

Jieyuan Rounded is derived from `jf open huninn`, which itself includes material and attribution from earlier upstream sources, including Kosugi Maru and Varela Round.

相關的來源資訊、授權文字與署名紀錄目前保留在 [`LICENSE`](./LICENSE) 與 source metadata 中。若要調整這些內容，請以正確性與必要性為前提。

Relevant attribution, licensing notes, and source history are kept in [`LICENSE`](./LICENSE) and related source metadata. If you need to revise them, please do so carefully and only when necessary.

## Naming and Licensing

本專案以 SIL Open Font License 1.1 發佈。若你要重新散布修改版本，請先閱讀 [`LICENSE`](./LICENSE)。

This project is distributed under the SIL Open Font License, Version 1.1. Please read [`LICENSE`](./LICENSE) before redistributing modified versions.

特別需要注意的是：
In particular:

- upstream reserved font names must be respected
- modified versions should use the project naming defined for this repository
- attribution and license notices should remain intact

## Contributing

歡迎貢獻，特別是以下幾種類型的改動：

Contributions are welcome, especially in these areas:

- adding missing characters (擴充缺字)
- glyph drawing improvements (輪廓與節點優化)
- spacing and kerning fixes (字距與間距調整)
- metadata cleanup (專案資訊清理)
- OpenType feature maintenance (OpenType 功能維護)
- documentation (文件更新)

開始之前，建議先閱讀：

Before contributing, please read:

- [Contribution Guide (English)](./docs/CONTRIBUTING.md)
- [Contribution Guide (繁體中文)](./docs/CONTRIBUTING.zh-TW.md)

## Scope

這個 repository 的目標，是維持一份可持續整理與維護的字型 source。

This repository is intended to preserve a maintainable source version of the font project.

如果你要修改內容，請盡量以小而清楚、容易審查的更新為主。相較於一次做大規模整理，source 的穩定性更重要。

If you are making changes, prefer small and reviewable updates. Source integrity matters more than aggressive cleanup.
