def convert_input(inputs: str):
    return [int( row.split("   ")[0]  )for row in inputs.split("\n")[:-1]], [int( row.split("   ")[1]  )for row in inputs.split("\n")[:-1]]

def solution_1(inputs: str):
    # Convert into two lists
    list_1, list_2 = convert_input(inputs)

    sum_distance = 0
    for l1, l2 in zip(sorted(list_1), sorted(list_2)):
        sum_distance += abs(l1-l2)

    print(sum_distance)

def solution_2(inputs):
    list_1, list_2 = convert_input(inputs)

    similarity_score = 0
    for number in list_1:
        number_count = list_2.count(number)
        similarity_score += number_count * number

    print(similarity_score)



test_input = """3   4
4   3
2   5
1   3
3   9
3   3
"""
# solution_1(test_input)
# solution_2(test_input)

puzzle_input = open("input").read()
# solution_1(puzzle_input)
solution_2(puzzle_input)

