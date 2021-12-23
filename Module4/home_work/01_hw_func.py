def lucky_ticket(ticket_number):
    sum1 = 0
    sum2 = 0
    i = 6
    curr_num = ticket_number
    while i > 0:
        if i > 3:
            sum1 += curr_num % 10
            curr_num = curr_num // 10
            i -= 1
        else:
            sum2 += curr_num % 10
            curr_num = curr_num//10
            i -= 1
    return sum1 == sum2

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(123215))
print(lucky_ticket(436751))
