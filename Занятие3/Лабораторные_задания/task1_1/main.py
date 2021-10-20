def task_1_1():
    max_sum = 500
    current_sum = 0
    n = 1
    while current_sum <= max_sum:
        current_sum += n ** 2
        if current_sum > max_sum:
            break
        print(n, current_sum)
        if current_sum > max_sum:
            break
        n = n + 1
    return n

if __name__ == "__main__":
    print(task_1_1())