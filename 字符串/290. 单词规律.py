class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_list = list(pattern)
        s_list = s.split(' ')
        # 　用这俩个列表去生成字典　如果字典中对于pattern项本来有值　但是即将赋值的值与原来不一样 则返回false
        if len(pattern_list) != len(s_list):
            return False
        res = {}
        for i in range(len(s_list)):
            if not res.get(pattern_list[i]):
                if s_list[i] in res.values():
                    return False
                res[pattern_list[i]] = s_list[i]
            else:
                if res.get(pattern_list[i]) != s_list[i]:
                    return False
        return True


'''
优化: 俩个列表去重后的项数应该是相等的但是单单这样还不够 俩个列表的长度也应该是相同的 在这种情况下只会存在一一对应的情况，只用字典就能完美解决了
        长度相同 说明x的个数和y的个数是一样多的 去重相同说明 唯一的x的个数和唯一的y的个数是一样的 这样就有可能一一对应了
'''


def wordPattern2(self, pattern: str, s: str) -> bool:
    s_list = s.split(' ')
    # 　用这俩个列表去生成字典　如果字典中对于pattern项本来有值　但是即将赋值的值与原来不一样 则返回false
    if len(pattern) != len(s_list) or len(set(pattern)) != len(set(s_list)):
        return False
    res = {}
    for i in range(len(s_list)):
        if not res.get(pattern[i]):
            res[pattern[i]] = s_list[i]
        else:
            if res.get(pattern[i]) != s_list[i]:
                return False
    return True
