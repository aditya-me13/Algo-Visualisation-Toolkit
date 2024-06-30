import time
import random
import argparse
import matplotlib.pyplot as plt

total_time = 0

def swap(xp, yp):
    return yp, xp

# Bubble sort function
def bubble_sort(numbers, args):
    global total_time
    size = args.size

    start_time = time.time()
    
    for i in range(size - 1):
        for j in range(0, size - i - 1):
            if numbers[j] > numbers[j + 1]:
                colors = ['darkgrey' if index not in [j, j + 1] else 'tomato' for index in range(len(numbers))]
                plt.bar([i for i in range(len(numbers))], numbers, color=colors)
                
                # Calculate and display elapsed time
                end_time = time.time()
                total_time = (end_time - start_time) + total_time
                start_time = time.time()
                plt.title(f'Sorting in Progress\nElapsed Time: {total_time:.2f} milliseconds')
                plt.show(block=False)
                plt.pause(args.delay/10)
                plt.clf()

                numbers[j], numbers[j + 1] = swap(numbers[j], numbers[j + 1])

                colors = ['darkgrey' if index not in [j, j + 1] else 'limegreen' for index in range(len(numbers))]
                plt.bar([i for i in range(len(numbers))], numbers, color=colors)
                plt.title(f'Sorting in Progress\nElapsed Time: {total_time:.2f} milliseconds')
                plt.show(block=False)
                plt.pause(args.delay/10)
                plt.clf()

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

    plt.bar([i for i in range(len(numbers))], numbers)
    plt.show(block=False)
    plt.pause(args.delay)
    plt.clf()

    bubble_sort(numbers, args)

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
