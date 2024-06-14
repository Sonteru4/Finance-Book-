import os


def move_files_to_output_directory(list_of_files, output_path, end_with=".json"):
    if not os.path.exists(output_path):
        print("created dir %s " % output_path)
        os.mkdir(output_path)
    for file in list_of_files:
        dest = os.path.join(output_path, file + end_with)
        os.rename(file, dest)
        print(dest)


class FileSystemWatcher:
    "File system watcher - Get changed files in specific dir"

    def __init__(self, path, start_with):
        self.path = path
        self.start_with = start_with
        self.last_dir_list = self.get_dir_list()

    def get_dir_list(self):
        return [f for f in os.listdir(self.path) if f.startswith(self.start_with)]

    def get_diff(self):
        current_list = self.get_dir_list()
        diff = [x for x in current_list if x not in self.last_dir_list]
        self.last_dir_list = current_list
        return diff
