def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for _ in phone_book:
        head = phone_book.pop(0)
        head_len = len(head)
        for i in phone_book:
            if i[:head_len] == head:
                return False
    
    return True