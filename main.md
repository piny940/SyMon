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
- 例： `(A(B)%(1,20))$`（AB 間が 1s 以上）

```txt
A 0.5
B 0.8
C 1.5
A 2.0
B 3.2
A 3.5
C 4.6
```

---

## 実際のログで試してみた（monaa）

- ログの内容を 1 文字の char に対応づける前処理

```py
mappings = [
    ['no new tags found, next scan in 1m0s', 'N'],
    [r"^Latest image tag for (略) resolved to main-\S+$", 'U']
]
```

```
U 1746447443.495
N 1746447444.1
U 1746447444.108
U 1746447444.116
U 1746447504.121
N 1746447504.74
U 1746447504.755
```

---

# 実アプリケーションの動作検証

---

## やりたいこと

アプリの Image を更新するサービスの検証

1. Image をレジストリに push
1. 最新の Image が変わったことを検知

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
