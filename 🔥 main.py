import argparse
from analyzer import analyze_iam
from reporter import generate_report

def main():
    parser = argparse.ArgumentParser(
        description="AWS IAM Least Privilege Analyzer"
    )
    parser.add_argument(
        "--export",
        help="Export report to JSON file",
        action="store_true"
    )

    args = parser.parse_args()

    results = analyze_iam()

    if args.export:
        generate_report(results)

if __name__ == "__main__":
    main()
