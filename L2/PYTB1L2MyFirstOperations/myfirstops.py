input1 = float(input("Enter first number: "))

stage1 = input1 + input1
print(stage1)

stage2 = stage1 - input1 + stage1 * input1
print(stage2)

stage3 = stage2 * stage1 + input1 // stage1
print(stage3)

stage4 = stage3 / stage2
print(stage4)

stage5 = stage4 % stage3
print(stage5)

input1 += stage5
print(input1)

input1 += stage1
print(input1)

input1 /= stage2
print(input1)

stage6 = input1 ** stage5
print(stage6)

stage7 = stage6 ** input1
print(stage7)

input("...")