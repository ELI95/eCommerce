## 位运算

### 位运算规则
![位运算规则](https://segmentfault.com/img/bVp6Uv)

### 计算机中数字的存储方式
在计算机系统中，数值一律用补码来表示、运算和存储。使用补码，可以将符号位和数值域统一处理，将加法和减法统一处理。此外，补码与原码相互转换，其运算过程是相同的，不需要额外的硬件电路。

- 原码表示法在数值前面增加了一位符号位（即最高位为符号位）：正数该位为0，负数该位为1。比如十进制3如果用8个二进制位来表示就是 00000011， -3就是 10000011。
- 反码表示方法：正数的反码是其本身；负数的反码是在其原码的基础上，符号位不变，其余各个位取反。
- 补码表示方法：正数的补码是其本身；负数的补码是在其原码的基础上，符号位不变，其余各位取反，最后+1。 (即在反码的基础上+1)

### 案例
1. 不用额外的变量实现两个数字互换
```python
def swap(num_1, num_2):
    num_1 ^= num_2
    num_2 ^= num_1
    num_1 ^= num_2
    return num_1, num_2
```

2. 找出数组中只出现了一次的数（除了一个数只出现一次外，其他数都是出现两次）
```python
def find_two_single_num(lst):
    temp = 0
    for i in lst:
        temp ^= i
    for j in range(64*8):
        temp >>= j
        if temp & 1 == 1:
            break
    result_1 = 0
    result_2 = 0
    for k in lst:
        if (k >> j) & 1 == 1:
            result_1 ^= k
        else:
            result_2 ^= k
    return result_1, result_2
```

3. 不用判断语句来实现求绝对值
```python
def bit_abs(num):
    negative = num >> 63
    return (num ^ negative) - negative
```

4. 不用乘法，除法，求模运算来实现两个整数相除
```python
def floor_divide(dividend, divisor):
    positive = (dividend < 0)  == (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    result = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            result += i
            i <<= 1
            temp <<= 1
    if not positive:
        result = -result
    return min(max(-2147483648, result), 2147483647)
```


5.  不使用运算符 + 和 -，计算两整数a 、b之和
```python
def get_sum(a, b):
    MAX = 0x7FFFFFFF
    mask = 0xFFFFFFFF
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    return a if a <= MAX else ~(a ^ mask)
```

6. 生成一个集合的所有子集合
```python
def find_all_subset(lst):
    subset_all = []
    n = len(lst)
    subset_num = 2 ** n
    for i in range(subset_num):
        subset = []
        for j in range(n):
            temp = 2 ** j
            if temp & i == temp:
                subset.append(lst[j])
        subset_all.append(subset)
    return subset_all
```

### 参考资料：
[leetcode](https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently)
