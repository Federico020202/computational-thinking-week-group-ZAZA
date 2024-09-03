correspondance_dict = {
  "a":3,
  "b":-1,
  "c":4,
  "d":7,
  "e":0.5
}

def solution_station_7(input):
  input = str(input) 
  result = []
  for char in input:
    is_in_dict = char in correspondance_dict
    if is_in_dict == True: 
      result.append(str(correspondance_dict[char]))
    else:
      result.append(str(char))

  result_list = "".join(result)
  print(result_list)
  solution = eval(str(result_list))

  return solution
  



