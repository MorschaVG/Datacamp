import os

work_dir = os.getcwd()

print(work_dir)

environ = os.environ

for key, value in environ.items():
    print(f"{key}: {value}")




