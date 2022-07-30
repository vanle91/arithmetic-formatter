def arithmetic_arranger(problems, show=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  first_numbers = ""
  second_numbers = ""
  dashes = ""
  answers = ""
  problem_spaces = " " * 4
  
  for problem in problems:
    data = problem.split()
    operator = data[1]
    first_number = data[0]
    second_number = data[2]
  
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
    if first_number.isdigit() is False or second_number.isdigit() is False:
      return "Error: Numbers must only contain digits."
    if len(first_number) > 4 or len(second_number) > 4:
      return "Error: Numbers cannot be more than four digits."

    answer = str(int(first_number) + int(operator + second_number))
    
    max_num_len = max(len(first_number), len(second_number))
    min_num_len = min(len(first_number), len(second_number))
    dash = "-" * (max_num_len + 2)

    if len(first_number) >= len(second_number):
      spaces = " " * 2
      operator = operator + (" " * (max_num_len - min_num_len + 1))
    else:
      spaces = " " * (max_num_len - min_num_len + 2)
      operator = operator + " "

    first_number = f"{spaces}{first_number}"
    second_number = f"{operator}{second_number}"

    first_numbers += first_number + problem_spaces
    second_numbers += second_number + problem_spaces
    dashes += dash + problem_spaces
    answers += (" " * (len(dash) - len(answer))) + answer + problem_spaces
  
  first_numbers = first_numbers.rstrip()
  second_numbers = second_numbers.rstrip()
  dashes = dashes.rstrip()
  answers = answers.rstrip()
  if show:
    arranged_problems = f"{first_numbers}\n{second_numbers}\n{dashes}\n{answers}"
  else:
    arranged_problems = f"{first_numbers}\n{second_numbers}\n{dashes}"

  return arranged_problems