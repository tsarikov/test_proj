def chunk_f(slot: int, given_expression) -> list:
    given_type = str(type(given_expression))
    given_len = len(given_expression)
    
    
    
    match given_type:
        case "<class 'str'>":
            print(given_type, given_expression)
            return chunk_str(slot, given_expression, given_len)
            

        case "<class 'list'>":
            return chunk_list(slot, given_expression, given_len)
        
        case "<class 'tuple'>":
            pass 
        
        case "<class 'set'>":
            pass

def chunk_str(slot, str_expression, given_len):
    ''' Обработка строкового типа. 
     str_len - длина строки
     result_list - возвращаемый итоговый список с нарезкой из строк
     1. Проверяем: если длина строки меньше слота нарезки, то возвращаем исходную строку. Выход из функции.
      2. Иначе:
            - counter содержит количество слотов нарезки, умещающихся в исходной стрке.
            - создаем список str_list из исходной строки str_expression
              Цикл while выполняется по параметру i от нуля до counter (столько раз, сколько целых слотов помещается в строке)
              для каждого слота добавляем в рабочий список work_list столько элементов по порядку, сколько указано в слоте, посредством цикла for.
              Достигнув длины слота, переводим рабочий список в str, добавляем его в итоговый список и идем дальше по строке.
                Дойдя до конца целых слотов, проверяем, если есть короткий "хвост", то добавляем его в итоговый список. 
                Далее возвращаем итоговый список. Выход из функции  '''
    if given_len <= slot:
        result_list = []
        result_list.append(str_expression)
        return result_list
    else:
        result_list = []
        work_list = []
        counter = given_len // slot
        str_list = list(str_expression)

        i = 0
        while i < counter:
            work_list = []
            for j in range(slot):
                work_list.append(str_list[i*slot+j])
            result_list.append(''.join(work_list))
            i += 1
        
        if given_len % slot != 0:
            work_list = []
            for j in range(i * slot, given_len):
                work_list.append(str_list[j])
            result_list.append(''.join(work_list))
        return result_list

def chunk_list(slot, list_expression, given_len):
    if given_len <= slot:
        result_list = []
        result_list.append(list_expression)
        return result_list
    else:
        result_list = []
        work_list = []
        counter = given_len // slot
        main_list = list.copy(list_expression)
    
        i = 0
        while i < counter:
            work_list = []
            for j in range(slot):
                work_list.append(main_list[i*slot+j])
            result_list.append(work_list)
            i += 1
        
        if given_len % slot != 0:
            work_list = []
            for j in range(i * slot, given_len):
                work_list.append(main_list[j])
            result_list.append(work_list)
        return result_list


print(chunk_f(10, 'skjvhskjerruh eor eorh'))
print(chunk_f(10, [1,12,13,4,6,11,54,23,345,23,1,12,13,4,6,11,54,23,345,23]))
