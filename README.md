![Cisco DevNet](https://img.shields.io/static/v1?logo=Cisco&label=Cisco&message=DevNet&color=00BCEB&style=flat-square)
[![Python 3.8+](https://img.shields.io/badge/Python%203.8+-blue.svg?logo=python&logoColor=yellow&color=3776ab&style=flat-square)](https://www.python.org/downloads)
![Language](https://img.shields.io/github/languages/top/Tes3awy/R-and-S?label=Python&style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/Tes3awy/R-and-S?label=Repo%20size&style=flat-square)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/Tes3awy/R-and-S?color=orange&label=Commit%20activity&style=flat-square)](https://github.com/Tes3awy/R-and-S)
![Last Commit](https://img.shields.io/github/last-commit/Tes3awy/R-and-S?label=Last%20commit&style=flat-square)
[![License](https://img.shields.io/github/license/Tes3awy/R-and-S?label=License&style=flat-square&color=purple)](https://github.com/Tes3awy/R-and-S/blob/main/LICENSE)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&labelColor=ef8336)](https://pycqa.github.io/isort/)

# Netmiko & Requests Examples for Cisco DevNet

## Table of Contents

1. [Getting Started](#getting-started)
2. [How to use?](#how-to-use)
3. [Documentation Links](#documentation-links)

## Getting Started

- In `netmiko_demos` folder, you will find 8 Python demos, `iplist.txt` file, and an explanation of each example.

- In `requests_demos` folder, you will find 3 Python demos, and an explanation of each example.

## How to use?

1. `Download ZIP` by clicking on the green **Code** button.

2. Once downloaded, extract the ZIP file, right click on `R-and-S-main` and click `Open with Code`.

3. Run `pip install -r requirements.txt`.

4. Open `netmiko_demos` or `requests_demos` folder in VSCode.

5. Explore each `demo*.py` file. _**(where **\*** is the number of the demo)**_

6. Run any Python demo by typing the following command in PowerShell terminal _(Either integrated terminal in VSCode or standalone Windows PowerShell/CMD)_:

```powershell
R-and-S-main\netmiko_demos> python demo*.py
```

```powershell
R-and-S-main\requests_demos> python demo*.py
```

or click the **Run** button in the topbar.

---

## Documentation Links

Examples in `netmiko` and `requests` folders use some Python libraries. These libraries are:

1. Netmiko **v4.2.0** (Multi-vendor library to simplify Paramiko SSH connections to network devices) [Documentation Link](https://github.com/ktbyers/netmiko/blob/develop/README.md)
2. NTC Templates **v3.5.0** (TextFSM templates for parsing show commands of network devices) [Documentation Link](https://github.com/networktocode/ntc-templates)
3. XlsxWriter **v3.1.6** (XlsxWriter is a Python module for creating Excel XLSX files) [Documentation Link](https://xlsxwriter.readthedocs.io/)
4. Requests **v2.31.0** (HTTP Requests) [Documentation Link](https://docs.python-requests.org/en/master/)
