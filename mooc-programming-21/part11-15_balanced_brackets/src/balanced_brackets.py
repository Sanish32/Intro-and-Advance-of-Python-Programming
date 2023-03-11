
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True

    
    if (not (my_string[0] == '(' and my_string[-1] == ')')) and (not (my_string[0] == '[' and my_string[-1] == ']')):
        if (my_string[0]!="(" and my_string[-1]==")") or (my_string[0]!="[" and my_string[-1]=="]"):
            if len(my_string)==1:
                return False
            return balanced_brackets(my_string[1:])
        elif (my_string[0]=="(" and my_string[-1]!=")") or (my_string[0]=="[" and my_string[-1]!="]"):
            if len(my_string)==1:
                return False
            return balanced_brackets(my_string[:-1])

    # remove first and last character
    return balanced_brackets(my_string[1:-1])


if __name__=="__main__":

    ok = balanced_brackets("((x)")
    print(ok)
