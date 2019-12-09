regex = '(\d[0,1]\d\d|2[0-4]\d|25[0-5])\.(\d[0,1]\d\d|2[0-4]\d|25[0-5])\.(\d[0,1]\d\d|2[0-4]\d|25[0-5])\.(\d[0,1]\d\d|2[0-4]\d|25[0-5])'

test_string1 = "Test IP 216.58.200.227"
RegexMatchingTest(regex, test_string1)  # 測試表達式是否會匹配此合法IP

test_string2 = "Test IP 999.888.777.666"
RegexMatchingTest(regex, test_string2)  # 測試表達式是否會匹配此不合法IP
e