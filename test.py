import re

# 網址判斷


def RegexMatchingTest(regex, input_text):
    pattern = re.compile(regex)
    result = re.search(pattern, input_text)

    if result:
        if result.lastindex is not None:
            for i in range(0, result.lastindex+1):
                return result.group(2)
    else:
        return None


regex = "(\w+):\/\/([^/:]+)?([^# !>]*)"
