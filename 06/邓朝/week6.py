number=[8,3,1,2,5,4,7,6]
group={2,3,5,7}

def sort_priority(number,group):
    lst=filter(lambda x:x not in group,number)
    def _sort(lst):
        return list(group)+sorted(lst)
    return _sort(lst)

print(sort_priority(number,group))