def isAnagram(s, t):
    s_qt = {}
    for l in s:
        if l not in s_qt:
            s_qt[l] = 1
        else:
            s_qt[l] += 1
   
    t_qt = {}
    for l in t:
        if l not in t_qt:
            t_qt[l] = 1
        else:
            t_qt[l] += 1
    
    if s_qt == t_qt:
        return True
    else:
        return False

