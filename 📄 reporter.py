import json

def generate_report(findings):
    with open("iam_audit_report.json", "w") as f:
        json.dump(findings, f, indent=4)

    print("Report exported as iam_audit_report.json")
