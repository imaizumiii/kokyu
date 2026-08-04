# Compile this pLaTeX document to PDF via DVI and dvipdfmx.
$latex = 'platex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$dvipdf = 'dvipdfmx %O -o %D %S';
$pdf_mode = 3;
