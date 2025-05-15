# assert abs(-42) == -42, "Should be absolute value of a number"
# assert проверяет истинность утверждений. AssertTrue не приводит к сообщениям.
# AssertFalse вызовет исключение AssertionError
# abs() - возвращает абсолютное значение числа по модулю

# Для добавления дополнительного сообщения можно при вызове assert через запятую написать нужное 
# сообщение, которое будет выведено в случае ошибки проверки результата


def test_input_text(expected_result, actual_result):
   assert (expected_result == actual_result), f"expected {expected_result}, got {actual_result}"
   
   expected_result = 1
   actual_result = 5
   
   
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
    
def test_substring(full_string, substring):
    full = str(full_string)
    sub = str(substring)
    assert sub in full, f"expected '{sub}' to be substring of '{full}'" # поиск подстроки во всём тексте