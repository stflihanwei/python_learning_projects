from PythonCrashcourse.testing.name_function import get_formatted_name

print("enter 'q' to exit")
while True:
    first = input("\nGive first name:")
    if first == 'q':
        break
    last = input("Please give me a last name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name:" + formatted_name + '.')
