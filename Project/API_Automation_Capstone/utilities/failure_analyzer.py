class FailureAnalyzer:

    @staticmethod
    def classify_status_code(status_code):

        if 200 <= status_code < 300:
            return "SUCCESS"

        if status_code == 400:
            return "CLIENT_ERROR - BAD_REQUEST"

        if status_code == 401:
            return "AUTHENTICATION_ERROR - UNAUTHORIZED"

        if status_code == 403:
            return "AUTHORIZATION_ERROR - FORBIDDEN"

        if status_code == 404:
            return "RESOURCE_ERROR - NOT_FOUND"

        if 400 <= status_code < 500:
            return "CLIENT_ERROR"

        if 500 <= status_code < 600:
            return "SERVER_ERROR"

        return "UNKNOWN_ERROR"

    @staticmethod
    def get_severity(status_code):

        if 200 <= status_code < 300:
            return "NONE"

        if status_code in [400, 404]:
            return "MEDIUM"

        if status_code in [401, 403]:
            return "HIGH"

        if 500 <= status_code < 600:
            return "CRITICAL"

        return "HIGH"

    @staticmethod
    def get_recommendation(status_code):

        recommendations = {
            400: "Validate the request payload and input parameters.",
            401: "Verify authentication credentials or access token.",
            403: "Verify that the authenticated user has sufficient permissions.",
            404: "Verify that the requested resource exists.",
            500: "Investigate server-side errors and backend logs."
        }

        if status_code in recommendations:
            return recommendations[status_code]

        if 200 <= status_code < 300:
            return "API request completed successfully."

        if 400 <= status_code < 500:
            return "Review the request parameters and API contract."

        if 500 <= status_code < 600:
            return "Investigate the server-side implementation."

        return "Unknown response. Investigate manually."

    @staticmethod
    def analyze_response(response):

        status_code = response.status_code

        category = FailureAnalyzer.classify_status_code(
            status_code
        )

        severity = FailureAnalyzer.get_severity(
            status_code
        )

        recommendation = FailureAnalyzer.get_recommendation(
            status_code
        )

        return {
            "status_code": status_code,
            "category": category,
            "severity": severity,
            "recommendation": recommendation
        }