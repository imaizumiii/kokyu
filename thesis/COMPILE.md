# thesis_template のコンパイル方法

このリポジトリのルートディレクトリ（`.latexmkrc` と
`thesis_template_20231219.tex` がある場所）で、次のコマンドを実行する。

```powershell
latexmk thesis_template_20231219.tex
```

コンパイルに成功すると、同じディレクトリに次の PDF が生成・更新される。

```text
thesis_template_20231219.pdf
```

`.latexmkrc` に設定があるため、`latexmk` が次の処理を自動で行う。

1. `platex` で LaTeX ファイルをコンパイルする
2. 目次や相互参照が確定するまで、必要に応じて `platex` を再実行する
3. `dvipdfmx` で DVI を PDF に変換する

## 必要な環境

- TeX Live などの TeX 環境
- `latexmk`
- `platex`
- `dvipdfmx`

コマンドが使えるかは、次のように確認できる。

```powershell
latexmk -version
platex --version
dvipdfmx --version
```

## 生成された中間ファイルを削除する

PDF を残して中間ファイルだけを削除する場合：

```powershell
latexmk -c thesis_template_20231219.tex
```

PDF を含む生成ファイルをすべて削除する場合：

```powershell
latexmk -C thesis_template_20231219.tex
```

## `latexmk` を使わずに手動で行う場合

通常は `latexmk` の使用を推奨する。手動で行う場合は、目次や参照を反映するため
`platex` を2回実行してから PDF に変換する。

```powershell
platex thesis_template_20231219.tex
platex thesis_template_20231219.tex
dvipdfmx thesis_template_20231219.dvi
```

## 補足

- 現在の構成では、Windows 上で日本語名のファイルに関する文字コード警告が
  `latexmk` に表示されることがある。ただし、最後に
  `All targets ... are up-to-date` と表示されて PDF が生成されていれば成功している。
- エラーになった場合は、まず `thesis_template_20231219.log` の末尾付近を確認する。
