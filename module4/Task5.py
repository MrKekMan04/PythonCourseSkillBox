user_input = input("Введите строку: ")

print("Развёрнутая последовательность между первым и последним h: "
      f"{user_input[user_input.rindex('h') - 1:user_input.index('h'):-1]}")
