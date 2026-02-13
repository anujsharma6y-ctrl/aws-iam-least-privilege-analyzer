import boto3
import json
from risk_engine import evaluate_policy
from colorama import Fore, Style

def analyze_iam():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']

    findings = []

    for user in users:
        policies = iam.list_attached_user_policies(
            UserName=user['UserName']
        )['AttachedPolicies']

        for policy in policies:
            policy_version = iam.get_policy_version(
                PolicyArn=policy['PolicyArn'],
                VersionId=iam.get_policy(PolicyArn=policy['PolicyArn'])['Policy']['DefaultVersionId']
            )

            document = policy_version['PolicyVersion']['Document']
            risk = evaluate_policy(document)

            if risk != "LOW":
                print(f"{Fore.RED}[{risk}] User: {user['UserName']} Policy: {policy['PolicyName']}{Style.RESET_ALL}")
                findings.append({
                    "user": user['UserName'],
                    "policy": policy['PolicyName'],
                    "risk": risk
                })

    if not findings:
        print(f"{Fore.GREEN}No risky policies detected.{Style.RESET_ALL}")

    return findings
