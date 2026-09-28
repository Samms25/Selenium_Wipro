from api.user_api import UserAPI


def main():

    user_api = UserAPI()

    print("\n===== API SMOKE TEST =====")

    response = user_api.get_all_users()

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("API Connection: SUCCESS")
        print("Number of users:", len(response.json()["users"]))
    else:
        print("API Connection: FAILED")
        print("Response:", response.text)


if __name__ == "__main__":
    main()