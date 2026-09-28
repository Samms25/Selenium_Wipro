class ResponseValidator:

    @staticmethod
    def validate_status(response, expected_status):
        assert response.status_code == expected_status, (
            f"Expected status {expected_status}, "
            f"but received {response.status_code}"
        )

    @staticmethod
    def validate_required_fields(response_data, required_fields):
        missing_fields = [
            field for field in required_fields
            if field not in response_data
        ]

        assert not missing_fields, (
            f"Missing required fields: {missing_fields}"
        )

    @staticmethod
    def validate_field_types(response_data, expected_types):
        errors = []

        for field, expected_type in expected_types.items():
            if field not in response_data:
                errors.append(f"{field}: field missing")
                continue

            if not isinstance(response_data[field], expected_type):
                errors.append(
                    f"{field}: expected {expected_type.__name__}, "
                    f"got {type(response_data[field]).__name__}"
                )

        assert not errors, "\n".join(errors)

    @staticmethod
    def validate_response(response, expected_status,
                          required_fields=None, expected_types=None):

        ResponseValidator.validate_status(
            response,
            expected_status
        )

        response_data = response.json()

        if required_fields:
            ResponseValidator.validate_required_fields(
                response_data,
                required_fields
            )

        if expected_types:
            ResponseValidator.validate_field_types(
                response_data,
                expected_types
            )

        return response_data