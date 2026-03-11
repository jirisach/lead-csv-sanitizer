\# 🧹 Lead CSV Sanitizer



A CLI tool that prevents dirty lead data from entering your CRM.



!\[Python](https://img.shields.io/badge/python-3.11-blue)

!\[License](https://img.shields.io/badge/license-MIT-green)

!\[Status](https://img.shields.io/badge/status-active-success)



Part of the \*\*Lead Entry Guard\*\* ecosystem.



\*\*Lead CSV Sanitizer\*\* is a local-first Python tool for cleaning, validating, and preparing lead CSV files before CRM import.



It is designed for \*\*RevOps, Sales Ops, CRM admins, and automation builders\*\* who want safer, cleaner, and more reliable lead imports.



\## 🚨 The Problem



Lead spreadsheets exported from marketing tools, scraping tools, or manual lists often contain:



\- invalid emails

\- broken phone numbers

\- inconsistent column names

\- duplicate contacts

\- missing required fields



Importing these directly into CRM systems often results in:



\- failed imports

\- duplicate contacts

\- broken reporting

\- messy CRM data



\## ✅ The Solution



\*\*Lead CSV Sanitizer\*\* creates a deterministic pipeline that:



1\. Cleans the dataset

2\. Validates key fields

3\. Detects duplicates

4\. Flags data issues

5\. Generates CRM-ready output



All \*\*locally\*\*, with \*\*no external API calls\*\*.



\## ⚙️ Features



\- ✔ Column normalization

\- ✔ Whitespace cleanup

\- ✔ Email validation

\- ✔ Phone normalization (E.164 format)

\- ✔ Duplicate detection

\- ✔ Issue flags per row

\- ✔ Missing field audit

\- ✔ CRM-ready export

\- ✔ JSON summary report

\- ✔ Data health score

\- ✔ Dataset size guard

\- ✔ Processing time metrics

\- ✔ Local-first processing (privacy friendly)



\## 📊 Data Health Score



The tool calculates a \*\*Data Health Score\*\* based on:



\- valid emails

\- valid phone numbers

\- duplicate rate

\- missing required fields



Example output:



```

Data health score: 73%

```



This provides a quick overview of \*\*CRM data quality\*\*.





\## 🏗 Project Structure



```

lead-csv-sanitizer/

│

├─ src/

│  └─ lead\_csv\_sanitizer/

│     ├─ cli.py

│     ├─ loader.py

│     ├─ column\_mapper.py

│     ├─ cleaner.py

│     ├─ validators.py

│     ├─ dedupe.py

│     ├─ report.py

│     └─ writer.py

│

├─ tests/

├─ samples/

├─ output/

├─ pyproject.toml

└─ README.md

```



\## 🚀 Installation



Create and activate a virtual environment:



```bash

python -m venv .venv

. .\\.venv\\Scripts\\Activate.ps1

```



Install dependencies:



```bash

python -m pip install --upgrade pip

python -m pip install -e .

```



\## ▶ Usage



Run the sanitizer on a CSV file:



```bash

python -m lead\_csv\_sanitizer.cli samples\\messy\_leads.csv

```



\## 📁 Outputs



The tool generates several files inside the `output/` folder:



| File | Purpose |

|-----|-----|

| cleaned\_leads.csv | Full dataset with audit columns |

| crm\_import\_ready.csv | Simplified dataset ready for CRM import |

| rejected\_rows.csv | Rows rejected due to missing identifiers |

| sanitizer\_report.json | Data quality metrics |



\## 🧪 Testing



Run the test suite:



```bash

pytest

```



\## 🔐 Privacy \& Security



This tool is built with \*\*privacy-first principles\*\*.



\- ✔ Local processing only

\- ✔ No external APIs

\- ✔ No data uploads

\- ✔ Deterministic outputs



Best practices:



\- never commit real customer data

\- never commit output files with PII

\- use sample data in the repository



\## 🎯 Use Cases



Typical users include:



\- RevOps engineers

\- Sales Operations teams

\- CRM administrators

\- Automation consultants

\- Data quality engineers



Common scenarios:



\- preparing CSV imports for CRM

\- auditing marketing lead lists

\- cleaning scraped datasets

\- preventing duplicate CRM contacts



\## 🛣 Roadmap



Potential future improvements:



\- batch processing for multiple CSV files

\- richer data quality reports

\- configurable required fields

\- CRM-specific export formats

\- desktop packaging for non-technical users



\## 👨‍💻 Author



Built by Jiří Šach  

Automation \& Data Workflow Builder





