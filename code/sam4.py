def main(*args):
    return sum(args) / len(args)

if __name__ == '__main__':
    print(main(1, 2, 3, 4, 5, 6))