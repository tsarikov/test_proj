def chunk_f(slot: int, given_expression) -> list:
    given_type = str(type(given_expression))
    given_len = len(given_expression)
    working_expression = list(given_expression)
    
    chunk(slot, working_expression, given_len, given_type)
    
    
    # match given_type:
    #     case "<class 'str'>":
    #         print(given_type, given_expression)
    #         return chunk_str(slot, given_expression)
            

    #     case "<class 'list'>":
    #         return chunk_list(slot, given_expression)
        
    #     case "<class 'tuple'>":
    #         pass 
        
    #     case "<class 'set'>":
    #         pass

# def chunk_str(slot, str_expression):
#     ''' Обработка строкового типа. 
#      str_len - длина строки
#      result_list - возвращаемый итоговый список с нарезкой из строк
#      1. Проверяем: если длина строки меньше слота нарезки, то возвращаем исходную строку. Выход из функции.
#       2. Иначе:
#             - counter содержит количество слотов нарезки, умещающихся в исходной стрке.
#             - создаем список str_list из исходной строки str_expression
#               Цикл while выполняется по параметру i от нуля до counter (столько раз, сколько целых слотов помещается в строке)
#               для каждого слота добавляем в рабочий список work_list столько элементов по порядку, сколько указано в слоте, посредством цикла for.
#               Достигнув длины слота, переводим рабочий список в str, добавляем его в итоговый список и идем дальше по строке.
#                 Дойдя до конца целых слотов, проверяем, если есть короткий "хвост", то добавляем его в итоговый список. 
#                 Далее возвращаем итоговый список. Выход из функции  '''
#     str_len = len(str_expression)
#     if str_len <= slot:
#         result_list = []
#         result_list.append(str_expression)
#         return result_list
#     else:
#         result_list = []
#         work_list = []
#         counter = str_len // slot
#         str_list = list(str_expression)

#         i = 0
#         while i < counter:
#             work_list = []
#             for j in range(slot):
#                 work_list.append(str_list[i*slot+j])
#             result_list.append(''.join(work_list))
#             i += 1
        
#         if str_len % slot != 0:
#             work_list = []
#             for j in range(i * slot, str_len):
#                 work_list.append(str_list[j])
#             result_list.append(''.join(work_list))
#         return result_list

def chunk_list(slot, list_expression):
    pass

def chunk(slot, working_expression, given_len, given_type):
    if given_len <= slot:
        result_list = []
        result_list.append(type(given_type, working_expression))
        return result_list
    else:
        result_list = []
        work_list = []
        counter = str_len // slot
        str_list = list(str_expression)

        i = 0
        while i < counter:
            work_list = []
            for j in range(slot):
                work_list.append(str_list[i*slot+j])
            result_list.append(''.join(work_list))
            i += 1
        
        if str_len % slot != 0:
            work_list = []
            for j in range(i * slot, str_len):
                work_list.append(str_list[j])
            result_list.append(''.join(work_list))
        return result_list


print(chunk_f(10, 'skjvhskj'))