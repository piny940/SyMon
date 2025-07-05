---
marp: true
theme: custom
paginate: true
---

# 研究室インターン最終発表

京都大学大学院 情報学研究科
通信情報システムコース
安済翔真

---

# 背景

---

## やりたいこと

- Kubernetes の設定はミスしやすい
  - いろんなプラグインの設定が関わり合って駆動する
- しかもミスに気づきにくい
  - 複数 Controller が非決定的な順序で reconcile 処理を行う
- クラスタが意図した動作をしているか検証する仕組みがほしい

---

## どうするか？

- 静的検証
  - Controller をモデル化 [Liu et al., 2024]
- **動的検証**
  - 時間オートマトン

---

## 時間オートマトンを用いた実行時モニタリング

- イベントが発生した時刻・出力値が意図通りかを**時間オートマトン**やその拡張を用いて検証する

---

## 順序つき

1. item1
2. item2
3. item3
4. item4
5. item5

---

## 下に画像

- item1

![w:700](./images/song-list.png)

---

## 横に画像

<!--_class: side -->

- item1
- item2
- item3
- item4
- item5

![w:700px](./images/song-list.png)
