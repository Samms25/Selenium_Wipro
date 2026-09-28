from utilities.test_data_reader import TestDataReader


reader = TestDataReader()
data = reader.read_data()

print("\n===== TEST DATA =====")
print(data)
print("\nValid User:")
print(data["valid_user"])

print("\nUpdated User:")
print(data["updated_user"])