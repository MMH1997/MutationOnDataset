## Dataset Mutations

This repository contains code related to several randomly applied mutations to $n$ numerical data within a dataset, which are displayed in .py files.

In the file "ChangeSign.py", $n$ numerical cells of a dataset $df$ are selected, and the sign in each of them is changed. This simulates an omission or incorrect placement of the sign.

In the file "DecimalPointChange.py", $n$ numerical cells of a dataset $df$ are selected, and mistakes in placing a decimal point are simulated, either by omitting it or putting it in the wrong place.

In the file "ImputData.py", $n$ numerical cells of a dataset $df$ are selected, and typical situations when data is missing are simulated: imputing $0$, imputing the previous data, and imputing the average value of the previous data in the same column. Each of these three situations is applied a random number of times.

In the file "ModifyNumericCell.py", $n$ numerical cells of a dataset $df$ are selected, and changes of a digit are applied to them. This simulates a typical mistake of placing a wrong digit in a number.

Finally, in the file "main.py", the four mutations described above are applied to $n$ numerical cells in a dataset $df$ the same number of times.
