def solution(phone_book):
    answer = False
    
    phone_book.sort() #phone_book 정렬 
    for i in range(1,len(phone_book)): 
        if len(phone_book[i])>len(phone_book[i-1]): 
            if phone_book[i].startswith(phone_book[i-1]):
                return answer

    answer=True
        
    return answer