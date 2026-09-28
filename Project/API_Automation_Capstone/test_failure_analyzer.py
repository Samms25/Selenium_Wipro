from utilities.failure_analyzer import FailureAnalyzer


test_status_codes = [
    200,
    400,
    401,
    403,
    404,
    500
]

print("\n===== SMART API FAILURE ANALYZER =====")

for status_code in test_status_codes:

    category = FailureAnalyzer.classify_status_code(
        status_code
    )

    severity = FailureAnalyzer.get_severity(
        status_code
    )

    recommendation = FailureAnalyzer.get_recommendation(
        status_code
    )

    print(f"\nStatus Code   : {status_code}")
    print(f"Category      : {category}")
    print(f"Severity      : {severity}")
    print(f"Recommendation: {recommendation}")