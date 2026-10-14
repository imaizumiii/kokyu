# 第2章の量子回路図

単独の図は原稿と挿入用PDFを同じ名前で置く。`bloch-sphere` は2.1節で使用する。`three-qubit-circuit-example` は2.4.1節で使用し、2.4.4節で状態と測定結果を計算する例として参照できる。`hadamard-circuit` と `controlled-u-circuit` は個別に挿入できる回路図として保存している。

`gate-table-circuits.tex` は2.4節の表で使う小さな回路記号の共通定義である。本文の `\input` で読み込み、論文全体を組版すると各表に描画される。

このフォルダで各図を編集した後、次のコマンドでPDFを更新する。

```powershell
pdflatex -interaction=nonstopmode -halt-on-error bloch-sphere.tex
pdflatex -interaction=nonstopmode -halt-on-error hadamard-circuit.tex
pdflatex -interaction=nonstopmode -halt-on-error controlled-u-circuit.tex
pdflatex -interaction=nonstopmode -halt-on-error three-qubit-circuit-example.tex
```

本文からは論文のルートを基準に `\includegraphics{figures/02-quantum-basics/図の名前.pdf}` で読み込む。
