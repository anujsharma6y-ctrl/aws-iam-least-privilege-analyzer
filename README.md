
# AWS IAM Least Privilege Analyzer

An advanced CLI tool that analyzes AWS IAM policies for over-permissive access patterns and least-privilege violations.

## Key Features
- Detects wildcard actions (*)
- Detects wildcard resources (*)
- Identifies privilege escalation risks
- Risk scoring engine
- JSON export report
- Colored CLI output
- aws-iam-least-privilege-analyzer/
│
├── main.py
├── analyzer.py
├── risk_engine.py
├── reporter.py
├── requirements.txt
└── README.md
- 🚀 How To Run
- pip install -r requirements.txt
python main.py
python main.py --export
📂 Project Structure
Each project is organized into its own directory for modularity:

Plaintext
- aws-iam-least-privilege-analyzer/
│
├── main.py
├── analyzer.py
├── risk_engine.py
├── reporter.py
├── requirements.txt
└── README.md

🛠️ Tech Stack
Language: Python 3.8+
## ⚖️ License & Legal Information

This project is primarily licensed under the **MIT License**, with specific modules covered under **Apache 2.0** and **GPL v3**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-red.svg)](./LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

### Key Permissions:
- ✅ **Commercial Use:** You can use this code for business purposes.
- ✅ **Modification:** You can change the code however you like.
- ✅ **Distribution:** You can share the code with others.
- ✅ **Private Use:** You can use it privately.

### Conditions:
- ⚠️ **Notice:** You must include the original copyright and license notice in any copy of the software/source code.

### Warranty:
- 🛡️ **No Warranty:** The software is provided "as is", without any warranty of any kind. The author is not liable for any claims or damages.

**For more details, view the [Full LICENSE File](./LICENSE)**


Libraries: hashlib, watchdog, requests, psutil, subprocess, smtplib

OS: Linux (Ubuntu/Debian/Kali) & Windows (Admin/Root access required)

👨‍💻 Author
Anuj Sharma Cloud Security Automation Enthusiast | IT Automation Specialist | Python for SecOps
