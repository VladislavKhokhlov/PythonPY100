if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    def list_comprehension(n, m):
        return [i for i in range(n, m) if i % 2 == 0]

print(len(list_comprehension(1, 13)))

