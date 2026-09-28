class APIHealth:

    @staticmethod
    def calculate(total, passed, failed):

        if total == 0:
            return 0, "NO TESTS EXECUTED"

        pass_rate = (passed / total) * 100

        if failed == 0:
            health = "HEALTHY"
        elif pass_rate >= 80:
            health = "WARNING"
        else:
            health = "UNHEALTHY"

        return pass_rate, health

    @staticmethod
    def print_summary(total, passed, failed):

        pass_rate, health = APIHealth.calculate(
            total,
            passed,
            failed
        )

        print("\n========================================")
        print("          API HEALTH SUMMARY")
        print("========================================")
        print(f"Total Scenarios : {total}")
        print(f"Passed          : {passed}")
        print(f"Failed          : {failed}")
        print(f"Pass Rate       : {pass_rate:.2f}%")
        print(f"API Health      : {health}")
        print("========================================")