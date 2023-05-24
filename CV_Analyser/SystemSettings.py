Usernames = ['Chris', 'Divaskar', 'Juan', 'Amarnath']
Pwd = ['102', '068', '104', '091']
UserPrev = ['Admin', 'Applicant', 'Applicant', 'Applicant']
def loginCheck(u,p,prev):
    if u == Usernames[0]:
        if p == Pwd[0]:
            if prev == UserPrev[0]:
                return 0
    elif u == Usernames[1]:
        if p == Pwd[1]:
            if prev == UserPrev[1]:
                return 1
    elif u == Usernames[2]:
        if p == Pwd[2]:
            if prev == UserPrev[2]:
                return 1
    elif u == Usernames[3]:
        if p == Pwd[3]:
            if prev == UserPrev[3]:
                return 1
    else:
        return -1

