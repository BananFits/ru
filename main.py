def remove_adjacent_solution(l):
    result = [l[0]]
    for i in range(1, len(l)):
        if l[i] != l[i - 1]:
            result.append(l[i])
    return result
  # a = []
  # for item in nums:
  #   if len(a):
  #     if a[-1] != item:
  #       a.append(item)
  #   else: a.append(item)
  # return a

example_2_given = [3, 3, 0, 2, 4, 3, 3, 2, 3, 2, 4, 1, 4, 1, 2, 1, 0, 4, 2, 4, 5, 4, 1, 2, 0, 5, 0, 5, 2, 3, 4, 0, 2, 3,
                   2, 4, 5, 1, 4, 3, 3, 4, 2, 0, 4, 0, 0, 5, 3, 5, 5, 5, 0, 4, 3, 2, 1, 5, 2, 5, 0, 1, 4, 1, 1, 1, 4, 3,
                   0, 0, 2, 4, 3, 0, 2, 4, 2, 5, 0, 4, 2, 4, 1, 4, 4, 4, 2, 3, 0, 4, 3, 2, 4, 1, 2, 1, 1, 1, 0, 4]
example_2_res = [3, 0, 2, 4, 3, 2, 3, 2, 4, 1, 4, 1, 2, 1, 0, 4, 2, 4, 5, 4, 1, 2, 0, 5, 0, 5, 2, 3, 4, 0, 2, 3, 2, 4,
                 5, 1, 4, 3, 4, 2, 0, 4, 0, 5, 3, 5, 0, 4, 3, 2, 1, 5, 2, 5, 0, 1, 4, 1, 4, 3, 0, 2, 4, 3, 0, 2, 4, 2,
                 5, 0, 4, 2, 4, 1, 4, 2, 3, 0, 4, 3, 2, 4, 1, 2, 1, 0, 4]

print(remove_adjacent_solution(example_2_given))

print(remove_adjacent_solution(example_2_given) == example_2_res)