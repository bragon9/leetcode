class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict = collections.defaultdict(list)
        for entry in paths:
            entry_arr = entry.split()
            path = entry_arr[0]
            files = entry_arr[1:]
            for file in files:
                paren = file.find('(')
                filename = file[:paren]
                content = file[paren+1:-1]
                file_dict[content].append(f'{path}/{filename}')
        ans = []
        for content, files in file_dict.items():
            if len(files) > 1:
                ans.append(files)
        return ans
