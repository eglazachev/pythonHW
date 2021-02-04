number_of_elements = int(input('Enter a number of elements: '))
list_of_elements = []
i = 0
while i < number_of_elements:
    curr_el = input('Enter some elements:')
    try:
        curr_el = int(curr_el)
        list_of_elements.append(curr_el)
        i += 1
        continue
    except ValueError:
        try:
            curr_el = float(curr_el)
            list_of_elements.append(curr_el)
            i += 1
            continue
        except ValueError:
            list_of_elements.append(curr_el)
            i += 1
print(list_of_elements)
j = 0
while j < len(list_of_elements) // 2:
    swap = list_of_elements[2 * j]
    list_of_elements[2 * j] = list_of_elements[2 * j + 1]
    list_of_elements[2 * j + 1] = swap
    j += 1
print(list_of_elements)
