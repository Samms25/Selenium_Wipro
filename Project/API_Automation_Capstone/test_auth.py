from api.auth_api import AuthAPI


def main():

    auth_api = AuthAPI()

    print("\n===== AUTHENTICATION TEST =====")

    response = auth_api.login(
        "emilys",
        "emilyspass"
    )

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    if response.status_code == 200:
        print("Authentication: SUCCESS")
    else:
        print("Authentication: FAILED")


if __name__ == "__main__":
    main()