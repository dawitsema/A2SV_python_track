class Solution:
    def findDuplicate(self, paths):
        content_to_paths = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_parts = file_info.split('(')
                file_name = file_parts[0]
                file_content = file_parts[1][:-1]
                full_path = directory + '/' + file_name
                content_to_paths[file_content].append(full_path)

        duplicates = [paths for paths in content_to_paths.values() if len(paths) > 1]
        return duplicates

