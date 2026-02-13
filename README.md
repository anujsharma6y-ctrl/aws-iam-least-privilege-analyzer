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
