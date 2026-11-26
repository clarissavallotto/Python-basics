# code.py

## Overview

`code.py` is an exhaustive, end-to-end educational script and reference guide covering the core pillars of Python programming and Data Science. It is structured sequentially from foundational syntax to advanced statistical hypothesis testing and data visualization.

---

## Prerequisites & Dependencies

This project is designed for use in a [**Google Colab**](https://colab.research.google.com/) environment.

To run this script without errors, you need Python 3.8+ and several third-party data science libraries.

### Required Libraries
Install all required dependencies via `pip`:

```bash
pip install numpy pandas matplotlib seaborn scipy statsmodels mlxtend charset_normalizer fuzzywuzzy
```

### Optional Libraries
* **TensorFlow** (`pip install tensorflow`): Referenced in a commented-out section demonstrating operator overloading with Tensor objects.
* **Jupyter / IPython**: The script contains `%matplotlib inline` magic commands intended for Jupyter Notebook or Google Colab environments.

---

## Environment Setup & Data Extraction

At the very beginning of `code.py`, the script expects a compressed archive named `code_data.zip` in the current working directory and extracts it into a folder named `code_data`:

```python
import zipfile

with zipfile.ZipFile("code_data.zip", "r") as zip_ref:
    zip_ref.extractall("code_data")
```

> **Path Configuration Note:** Throughout the script, file paths are hardcoded using Google Colab's directory structure (`/content/code_data/code_data/<filename>.csv`). If running locally, ensure your directory structure matches or update the paths to relative paths (e.g., `code_data/<filename>.csv`).

---

## Datasets Used

The script loads and analyzes **11 distinct CSV datasets** extracted from `code_data.zip`:

| Dataset Filename | Domain / Description | Primary Sections Used |
| :--- | :--- | :--- |
| `winemag-data-130k-v2.csv` | 130,000 wine reviews with country, points, price, and taster info. | Pandas Basics, Indexing, Grouping, Missing Values, Renaming |
| `CAvideos.csv` | Trending YouTube video statistics in Canada. | Pandas Combining (`concat` and `join`) |
| `GBvideos.csv` | Trending YouTube video statistics in Great Britain. | Pandas Combining (`concat` and `join`) |
| `NFL Play by Play 2009-2017 (v4).csv` | Detailed play-by-play NFL game records. | Data Cleaning: Handling Missing Values |
| `catalog.csv` | Global landslide catalog with dates and locations. | Data Cleaning: Parsing Dates |
| `ks-projects-201612.csv` | Kickstarter crowdfunding projects (encoded in Windows-1252). | Data Cleaning: Character Encodings |
| `pakistan_intellectual_capital.csv` | Academic profiles of Pakistani professors (messy country names). | Data Cleaning: Inconsistent Data Entry (`fuzzywuzzy`) |
| `fifa.csv` | Historical FIFA world rankings over time. | Data Visualization: Hello Seaborn (Line Charts) |
| `spotify.csv` | Daily global streams of top songs in 2017–2018. | Data Visualization: Line Charts, Custom Styles, Final Project |
| `flight_delays.csv` | Average monthly arrival delays across major US airlines. | Data Visualization: Bar Charts & Heatmaps |
| `insurance.csv` | Medical insurance charges correlated with BMI and smoking status. | Data Visualization: Scatter Plots & Regression |
| `iris.csv` | Classic botanical dataset measuring sepal and petal dimensions. | Data Visualization: Distributions (Histograms & KDE) |
| `urban_wear_transactions.csv` | Raw retail transaction records (sales, profit, campaigns). | Additional Code: Cross-tabs, Pivot Tables, Reshaping |
| `urban_wear_transactions_clean.csv` | Cleaned retail transaction dataset. | Additional Code: Advanced Seaborn Plots, Pandas Plotting |
| `Titanic.csv` | Passenger demographics, class, fare, and survival status. | Additional Code: Confidence Intervals, Chi-Square, ANOVA |

---

## Module-by-Module Breakdown

### Part 1: Intro to Programming

#### 1. Arithmetic and Variables
* **Printing & Comments:** Basic `print()` usage and single-line `#` documentation.
* **Operators:** Addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), exponentiation (`**`), and PEMDAS/BODMAS precedence using parentheses `()`.
* **Variables:** Variable creation, dynamic reassignment (`my_var = my_var + 3`), multi-variable time calculations (seconds in 4 years), accounting for leap years (`365.25`), and avoiding `NameError`.

#### 2. Functions
* **Function Definition:** Using `def`, parameters, local calculations, and `return` statements (`add_three`, `get_pay`).
* **Scope:** Differentiating between local variables inside functions and global variables defined at the module level.
* **Signatures:** Multi-argument functions (`get_pay_with_more_inputs`) and zero-argument side-effect functions (`print_hello`).

#### 3. Data Types
* **Numeric Types:** `int` (whole numbers) vs. `float` (decimal numbers) and rounding with `round()`.
* **Booleans (`bool`):** `True`, `False`, comparison expressions (`1 < 2`), and logical negation (`not`).
* **Strings (`str`):** Measuring length with `len()`, empty strings `""`, casting strings to floats (`float()`), concatenation (`+`), and repetition (`*`).

#### 4. Conditions and Conditional Statements
* **Comparison Operators:** `>`, `<`, `>=`, `<=`, `==`, `!=`.
* **Control Flow:** `if`, `if...else`, and multi-branch `if...elif...else` structures demonstrated through temperature evaluation (`evaluate_temp`), progressive tax brackets (`get_taxes`), and weight-based dosage tiers (`get_dose`).

#### 5. Intro to Lists
* **List Mechanics:** Creation, zero-based indexing, negative indexing (`-1`), slicing (`[:3]`, `[-2:]`), and mutability via `.remove()` and `.append()`.
* **Aggregations:** Calculating list statistics using `len()`, `min()`, `max()`, and `sum()`.

---

### Part 2: Core Python

#### 1. Hello, Python
* Deep dive into division types: True division (`/`) returning floats vs. Floor division (`//`) truncating to integers, and Modulus (`%`) returning remainders.
* Built-in math helpers (`min`, `max`, `abs`) and explicit type casting (`int`, `float`).

#### 2. Functions and Getting Help
* **Introspection:** Using `help()` on built-ins and custom functions, emphasizing why passing a function call (`help(round(-2.01))`) inspects the return type rather than the function.
* **Docstrings & Defaults:** Writing multi-line docstrings and defining default parameter values (`greet(who="Colin")`).
* **NoneType:** Demonstrating that functions omitting `return` implicitly return `None`.
* **Higher-Order Functions:** Passing functions as arguments (`call`, `squared_call`) and using the `key` parameter in `max(key=mod_5)`.

#### 3. Booleans and Conditionals
* **Boolean Logic:** Truth tables for `and`, `or`, `not`, operator precedence (`and` before `or`), and grouping with parentheses.
* **Truthiness:** Evaluating non-Boolean objects in conditional blocks (`bool(0)` and `bool("")` evaluate to `False`; non-zero numbers and non-empty strings evaluate to `True`).

#### 4. Lists & Tuples
* **Nested Lists & Mutability:** Multi-dimensional lists (e.g., playing card hands) and slice assignment.
* **Object Model:** Accessing attributes (`.imag`) and methods (`.bit_length()`, `.pop()`, `.index()`, `.count()`, `.extend()`, `.insert()`, `.reverse()`, `.sort()`).
* **Tuples:** Immutable sequences (`t = (1, 2, 3)`), tuple unpacking (`numerator, denominator = x.as_integer_ratio()`), and idiomatic variable swapping (`a, b = b, a`).

#### 5. Loops and List Comprehensions
* **Iteration:** `for` loops over lists, tuples, strings, and `range()`, alongside condition-controlled `while` loops.
* **List Comprehensions:** Concise list generation, conditional filtering (`if len(planet) < 6`), and inline transformations.
* **Comparative Implementations:** Three approaches to counting negative numbers (`count_negatives_loop`, `count_negatives_list`, and `count_negatives_sum` exploiting `True == 1`).

#### 6. Strings and Dictionaries
* **String Manipulation:** Quote escaping (`\'`, `\"`), newlines (`\n`), multi-line triple quotes (`"""`), `.upper()`, `.lower()`, `.startswith()`, `.endswith()`, `.split()`, and `.join()`.
* **String Formatting:** Positional and numbered placeholders via `.format()`, including scientific/decimal precision (`{:.2}`), percentages (`{:.3%}`), and thousands separators (`{:,}`).
* **Dictionaries:** Key-value storage, dynamic insertion/updating, dictionary comprehensions (`planet_to_initial`), membership testing (`in`), and iterating with `.keys()`, `.values()`, and `.items()`.

#### 7. Working with External Libraries
* **Imports:** Standard imports (`import math`), aliases (`import math as mt`), and selective imports (`from math import log, pi`).
* **Object Inspection:** Using `type()` and `dir()` to explore unfamiliar objects like NumPy arrays.
* **NumPy & Operator Overloading:** Vectorized arithmetic (`rolls + 10`), element-wise boolean comparisons (`rolls <= 3`), 2D array indexing (`x[1, -1]`), and Python dunder methods (`__contains__`).

---

### Part 3: Data Manipulation with Pandas

#### 1. Creating, Reading and Writing
* Constructing `pd.DataFrame` from dictionaries and `pd.Series` from lists with custom indices.
* Loading external data via `pd.read_csv(..., index_col=0)` and inspecting dimensions with `.shape` and `.head()`.

#### 2. Indexing, Selecting & Assigning
* **Accessors:** Attribute (`reviews.country`) vs. bracket (`reviews['country']`) notation.
* **Position vs. Label Selection:**
  * `iloc`: Zero-based integer positional indexing (exclusive of stop index).
  * `loc`: Label-based indexing (inclusive of stop label).
* **Filtering:** Boolean masks with `&` (AND), `|` (OR), `.isin()`, `.notnull()`, and `.isnull()`.
* **Assignment:** Broadcasting scalar values (`reviews['critic'] = 'everyone'`) and assigning sequences.

#### 3. Summary Functions and Maps
* Descriptive statistics using `.describe()`, `.mean()`, `.unique()`, and `.value_counts()`.
* Element-wise transformations with `Series.map(lambda ...)` vs. row-wise transformations with `DataFrame.apply(..., axis='columns')` vs. vectorized operations.

#### 4. Grouping and Sorting
* Aggregating data with `.groupby()` paired with `.count()`, `.min()`, `.apply()`, and `.agg([len, min, max])`.
* Handling `MultiIndex` objects via `.reset_index()` and ordering results with `.sort_values()` and `.sort_index()`.

#### 5. Data Types and Missing Values
* Inspecting column `dtype` / `dtypes` and casting with `.astype('float64')`.
* Detecting nulls with `pd.isnull()` / `pd.notnull()`, imputing missing values via `.fillna("Unknown")` and backward filling (`.fillna(method='bfill')`), and correcting values with `.replace()`.

#### 6. Renaming and Combining
* Modifying column headers, index labels, and axis names using `.rename()` and `.rename_axis()`.
* Combining datasets vertically with `pd.concat()` and horizontally on shared keys using `DataFrame.join(..., lsuffix='_CAN', rsuffix='_UK')`.

---

### Part 4: Data Cleaning & Preprocessing

#### 1. Handling Missing Values
* Quantifying dataset completeness by calculating the exact percentage of missing cells across `nfl_data`.
* Comparing deletion strategies (`dropna()` row-wise vs. `dropna(axis=1)` column-wise) against imputation strategies (`fillna(0)` and `fillna(method='bfill')`).

#### 2. Scaling and Normalization
* Generating skewed synthetic data via `np.random.exponential(size=1000)`.
* **Min-Max Scaling:** Rescaling values strictly between $[0, 1]$ using `mlxtend.preprocessing.minmax_scaling` (preserves distribution shape).
* **Box-Cox Transformation:** Transforming skewed data into a normal (Gaussian) distribution using `scipy.stats.boxcox`.

#### 3. Parsing Dates
* Converting string dates into `datetime64` objects using `pd.to_datetime(..., format="%m/%d/%y")` and extracting date components via the `.dt` accessor (`.dt.day`).

#### 4. Character Encodings
* Demonstrating string-to-byte encoding (`.encode("utf-8")`) and decoding (`.decode()`), highlighting data corruption (`?` replacement) when forcing non-ASCII characters (like `€`) into `ascii`.
* Automatically detecting unknown CSV file encodings using `charset_normalizer.detect()` (`Windows-1252`) and exporting clean `UTF-8` files.

#### 5. Inconsistent Data Entry
* Text normalization using `.str.lower()` and `.str.strip()`.
* Implementing a reusable fuzzy string-matching function (`replace_matches_in_column`) powered by `fuzzywuzzy.process.extract` and `fuzz.token_sort_ratio` to unify variant spellings (e.g., `"south korea"`).

---

### Part 5: Data Visualization with Seaborn & Matplotlib

* **Line Charts:** Plotting time-series trends (`sns.lineplot`) for FIFA rankings and Spotify streams, customizing figure sizes (`plt.figure(figsize=...)`), axis labels, and legends.
* **Bar Charts & Heatmaps:** Visualizing categorical averages with `sns.barplot` and annotated 2D matrices with `sns.heatmap(..., annot=True)`.
* **Scatter Plots & Regression:** Exploring continuous relationships (`sns.scatterplot`), linear trends (`sns.regplot`), grouped regressions (`sns.lmplot`), and categorical distributions (`sns.swarmplot`, `sns.stripplot`).
* **Distributions:** Plotting univariate histograms (`sns.histplot`), smoothed Kernel Density Estimates (`sns.kdeplot`), and bivariate density contours (`sns.jointplot(..., kind="kde")`).
* **Custom Styles & Templates:** Iterating through Seaborn themes (`"darkgrid"`, `"whitegrid"`, `"dark"`, `"white"`, `"ticks"`), providing a structured Exploratory Data Analysis (EDA) template, and saving plots with `plt.savefig()`.

---

### Part 6: Applied Retail Analytics, NumPy & Statistical Testing

#### 1. Retail Transaction Analysis (`urban_wear_transactions.csv`)
* **Cross-Tabulations & Pivot Tables:** Building frequency tables (`pd.crosstab` with `normalize="all"` and `margins=True`) and multi-metric `pd.pivot_table` summaries.
* **Sampling & Feature Engineering:** Random sampling (`abt.sample(n=10, random_state=42)`), vectorized revenue calculation, and conditional flagging via `np.where()`.
* **Reshaping Data:** Converting between wide and long formats using `pd.melt()` and `.pivot()`.
* **Faceted & Multi-Variable Plots:** Creating box plots (`sns.boxplot`), small-multiple histograms (`sns.displot`), pairwise correlation grids (`sns.pairplot`), and categorical count grids (`sns.catplot`).

#### 2. Deep-Dive NumPy Operations
* 1D/2D array attributes (`.shape`, `.ndim`, `.size`, `.dtype`), slicing, and index-of-maximum lookups (`weekly_sales.argmax()`).
* Matrix generation using `np.zeros()` and `np.ones()`, constructing a concentric square pattern, and visualizing a $10 \times 10$ prime number grid using `plt.imshow()`.

#### 3. Inferential Statistics & Hypothesis Testing (`Titanic.csv`)
* **Confidence Intervals:** Computing 95% confidence intervals for mean passenger `Age` and `Fare` using `scipy.stats.norm.interval`.
* **Chi-Square Test of Independence:** Testing associations between categorical variables (`Survived` vs. `Pclass` and `Survived` vs. `Sex`) using `scipy.stats.chi2_contingency` at significance level $\alpha = 0.05$.
* **Analysis of Variance (ANOVA):** Fitting Ordinary Least Squares (`ols`) models via `statsmodels` and generating Type II ANOVA tables (`sm.stats.anova_lm`) to test mean differences across groups (`Age ~ C(Survived)` and `Fare ~ C(Pclass)`).

#### 4. Relational Joins & Specialized Pandas Plots
* **DataFrame Merging:** Demonstrating `inner`, `left`, `right`, and `outer` joins with `pd.merge()`, including the `indicator=True` audit column.
* **Pandas Plotting API:** Generating customized horizontal bar charts (`kind="barh"`), percentage-labeled pie charts (`kind="pie"`), area plots (`kind="area"`), stacked normalized bar charts, and multi-format figure exports.

---

## Generated Output Artifacts

Running this script will generate the following files in your working directory:

1. `code_data/` — Extracted directory containing all source CSV files.
2. `ks-projects-201801-utf8.csv` — Re-encoded UTF-8 version of the Kickstarter dataset.
3. `my_visualization.png` — Saved scatter plot from the visualization notebook template.
4. `lineplot.jpg` — First-30-days retail transaction line chart (JPEG format).
5. `lineplot.png` — First-30-days retail transaction line chart (PNG format).
6. `lineplot.pdf` — First-30-days retail transaction line chart (PDF vector format).

---

## Execution Notes & Troubleshooting

* **Jupyter Magic Commands:** Lines containing `%matplotlib inline` are valid in IPython/Jupyter notebooks but will raise a `SyntaxError` if executed directly via standard `python code.py` in a terminal. Remove or comment out `%matplotlib inline` before running as a standalone `.py` script.
* **Deprecated Pandas Arguments:** Newer versions of Pandas ($\ge 2.0$) deprecate `fillna(method='bfill')` in favor of `.bfill()` and `infer_datetime_format=True` in `pd.to_datetime()`. If running on Pandas 2.x+, you may see `FutureWarning` messages in the console.
* **Blocking Plot Windows:** Because `plt.show()` is called dozens of times throughout the script, running locally in a standard Python shell will pause execution until each plot window is manually closed.
