import time
import random
import argparse
import matplotlib.pyplot as plt

total_time = 0

def merge(numbers, l, m, r, args):
    global total_time

    # Start timing the internal processing
    start_process_time = time.time()

    n1 = m - l + 1
    n2 = r - m

    L = numbers[l:m + 1]
    R = numbers[m + 1:r + 1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            numbers[k] = L[i]
            i += 1
        else:
            numbers[k] = R[j]
            j += 1
        k += 1

        # Visualization after each merge step
        colors = ['darkgrey' for _ in range(len(numbers))]
        colors[l:r + 1] = ['tomato' for _ in range(l, r + 1)]
        colors[m] = 'limegreen'
        plt.bar([i for i in range(len(numbers))], numbers, color=colors)
        plt.title(f'Merging\nElapsed Time: {total_time:.2f} milliseconds')
        plt.show(block=False)
        plt.pause(args.delay/5)
        plt.clf()

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        numbers[k] = L[i]
        i += 1
        k += 1

        # Visualization after each merge step
        colors = ['darkgrey' for _ in range(len(numbers))]
        colors[l:r + 1] = ['tomato' for _ in range(l, r + 1)]
        colors[m] = 'limegreen'
        plt.bar([i for i in range(len(numbers))], numbers, color=colors)
        plt.title(f'Merging\nElapsed Time: {total_time:.2f} milliseconds')
        plt.show(block=False)
        plt.pause(args.delay/5)
        plt.clf()

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        numbers[k] = R[j]
        j += 1
        k += 1

        # Visualization after each merge step
        colors = ['darkgrey' for _ in range(len(numbers))]
        colors[l:r + 1] = ['tomato' for _ in range(l, r + 1)]
        colors[m] = 'limegreen'
        plt.bar([i for i in range(len(numbers))], numbers, color=colors)
        plt.title(f'Merging\nElapsed Time: {total_time:.2f} milliseconds')
        plt.show(block=False)
        plt.pause(args.delay/5)
        plt.clf()

    # Stop timing the internal processing
    end_process_time = time.time()
    total_time += (end_process_time - start_process_time)

def merge_sort(numbers, l, r, args):
    global total_time
    if l < r:
        m = (l + r) // 2

        # start_process_time = time.time()
        merge_sort(numbers, l, m, args)

        # total_time += (time.time() - start_process_time)
        # colors = ['darkgrey' for _ in range(len(numbers))]
        # colors[m] = 'tomato'
        # plt.bar([i for i in range(len(numbers))], numbers, color=colors)
        # plt.title(f'Merging\nElapsed Time: {total_time:.2f} milliseconds')
        # plt.show(block=False)
        # plt.pause(args.delay * 2)
        # plt.clf()

        merge_sort(numbers, m + 1, r, args)
        merge(numbers, l, m, r, args)

def generate_numbers(low, high, total, seed):
    random.seed(seed)
    numbers = random.sample(range(low, high + 1), total)
    random.shuffle(numbers)
    return numbers

# Driver program
def main(args):
    global total_time
    total_time = 0

    numbers = generate_numbers(args.low, args.high, args.size, args.seed)

    plt.bar([i for i in range(len(numbers))], numbers, color = 'darkgrey')
    plt.show(block=False)
    plt.pause(args.delay)
    plt.clf()


    merge_sort(numbers, 0, len(numbers) - 1, args)

    for i in range(args.size):
        colors = ['darkgrey' if index not in range(0, i + 1) else 'limegreen' for index in range(len(numbers))]
        plt.bar([i for i in range(len(numbers))], numbers, color=colors)
        plt.title(f'Successfully Sorted\nElapsed Time: {total_time:.2f} milliseconds')
        plt.show(block=False)
        plt.pause(args.delay / 10)
        plt.clf()
        print(numbers[i], end=" ")
    print()

    print(f"Total processing time: {total_time:.2f} milliseconds")
    time.sleep(5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--low', default=0, type=int)
    parser.add_argument('--high', default=20, type=int)
    parser.add_argument('--size', default=20, type=int)
    parser.add_argument('--seed', default=1, type=int)
    parser.add_argument('--delay', default=0.1, type=float)
    args = parser.parse_args()
    main(args)
