def isValid(s):
    hash = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    for i in range(0, len(s) - 1, 2):
        if s[i+1] == hash[s[i]]:
            print("correct")
s = "()[]{}"

isValid(s)
