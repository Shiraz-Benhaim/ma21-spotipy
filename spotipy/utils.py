import os


class Utils:
    @staticmethod
    def create_folder_if_not_exists(file_path):
        if not os.path.exists(file_path):
            os.makedirs(file_path)

    @staticmethod
    def write_to_file(path, data):
        with open(path, 'w') as file:
            file.write(data)
            file.close()
