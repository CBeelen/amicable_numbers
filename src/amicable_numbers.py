from argparse import ArgumentParser


def get_divisors(n):
    divisors = []
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def are_amicable(n, m):
    n_divisors = get_divisors(n)
    if sum(n_divisors) == m:
        m_divisors = get_divisors(m)
        if sum(m_divisors) == n:
            return True
    return False


def main():
    parser = ArgumentParser()
    parser.add_argument('n', help="First number")
    parser.add_argument('m', help="Second number")
    args = parser.parse_args()
    n = int(args.n)
    m = int(args.m)

    if are_amicable(n, m):
        print(f"{n} and {m} are so-called amicable numbers - "
              f"which means that the sum of the proper divisors of one number is the other number, and vice versa.")
    else:
        print(f"Sorry, {n} and {m} are not amicable numbers :(")


if __name__ == '__main__':
    main()
