def evaluate_policy(document):
    statements = document.get("Statement", [])

    if not isinstance(statements, list):
        statements = [statements]

    for statement in statements:
        effect = statement.get("Effect")
        action = statement.get("Action")
        resource = statement.get("Resource")

        if effect == "Allow":
            if action == "*" and resource == "*":
                return "CRITICAL"
            if action == "*" or resource == "*":
                return "HIGH"
            if "iam:PassRole" in str(action):
                return "MEDIUM"

    return "LOW"
