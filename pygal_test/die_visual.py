from die import Die

#创建一个D6
die=Die()

#扔几次骰子，并将结果存储在一个列表中
results=[]
for roll_num in range(100):
    result=die.roll()
    results.append(result)

print(results)