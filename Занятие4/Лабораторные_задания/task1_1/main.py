if __name__ == "__main__":
    def list_comprehension(n, m):
        return [i ** 2 for i in range(n, m)]

print(list_comprehension(3, 15))