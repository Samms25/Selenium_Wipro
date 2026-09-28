from utilities.response_validator import ResponseValidator


def main():

    print("\n===== RESPONSE VALIDATOR TEST =====")

    response_data = {
        "id": 1,
        "firstName": "Emily",
        "lastName": "Johnson",
        "age": 30
    }

    ResponseValidator.validate_required_fields(
        response_data,
        ["id", "firstName", "lastName"]
    )

    ResponseValidator.validate_field_types(
        response_data,
        {
            "id": int,
            "firstName": str,
            "lastName": str,
            "age": int
        }
    )

    print("Required Fields: PASS")
    print("Field Types: PASS")
    print("Response Validation: SUCCESS")


if __name__ == "__main__":
    main()