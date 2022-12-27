# Генерация псевдослучайных последовательностей
# Регистры сдвига с линейной обратной связью
def feedback_shift(bits):
  xor_result = (bits[1] + bits[2]) % 2 #суммируем биты исключающим ИЛИ (XOR)
  output = bits.pop()  #извлекаем правый элемент и сохраняем результат
  bits.insert(0,xor_result) #вставляем его в список с левого края
  return(bits,output)

#функция, которая генерирует список выходных битов
#т.н. генерирование белого шума
def feedback_shift_list(bits_this):
  bits_output = [bits_this.copy()]
  random_output = []
  bits_next = bits_this.copy()
  while(len(bits_output) < 2**len(bits_this)):
    bits_next,next = feedback_shift(bits_next)
    bits_output.append(bits_next.copy())
    random_output.append(next)
  return(bits_output,random_output)

print('1')
bitslist = feedback_shift_list([1,1,1])[0]
print(bitslist)

print('2')
pseudorandom_bits = feedback_shift_list([1,1,1])[1]
print(pseudorandom_bits)