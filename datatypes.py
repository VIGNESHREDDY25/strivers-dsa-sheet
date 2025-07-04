class Solution:
    def dataTypeSize(self, str):
        data_type_sizes = {
            "Character": 1,
            "Integer": 4,
            "Long": 8,
            "Float": 4,
            "Double": 8
        }
        return data_type_sizes.get(str, -1)