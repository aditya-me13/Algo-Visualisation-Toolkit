import time
import random
import argparse
import matplotlib.pyplot as plt

total_time = 0

def swap(xp, yp):
    return yp, xp

# Selection sort function
def selsort(numbers, args):
    global total_time
    size = args.size

    start_time = time.time()
    
    for i in range(size - 1):
        min_idx = i

        for j in range(i + 1, size):
            #plot the current checking
            total_time = (time.time() - start_time) + total_time
            start_time = time.time()
            colors = ['darkgrey' if index not in [min_idx, j] else 'tomato' for index in range(len(numbers))]
            plt.bar([i for i in range(len(numbers))], numbers, color=colors)
            plt.title(f'Sorting in Progress\nElapsed Time: {total_time:.2f} milliseconds')
            plt.show(block=False)
            plt.pause(args.delay/10)
            plt.clf()
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        
        colors = ['darkgrey' if index not in [min_idx, i] else 'tomato' for index in range(len(numbers))]
        plt.bar([i for i in range(len(numbers))], numbers, color=colors)
        
        # Calculate and display elapsed time
        end_time = time.time()
        total_time = (end_time - start_time) + total_time
        start_time = time.time()
        plt.title(f'Sorting in Progress\nElapsed Time: {total_time:.2f} milliseconds')
        plt.show(block=False)
        plt.pause(args.delay/10)
        plt.clf()

        colors = ['darkgrey' if index not in [min_idx, i] else 'limegreen' for index in range(len(numbers))]
        numbers[min_idx], numbers[i] = swap(numbers[min_idx], numbers[i])

        plt.bar([i for i in range(len(numbers))], numbers, color=colors)
        plt.title(f'Sorting in Progress\nElapsed Time: {total_time:.2f} milliseconds')
        plt.show(block=False)
        plt.pause(args.delay)
        plt.clf()

def generate_numbers(low, high, total, seed):
    random.seed(seed)
    numbers = random.sample(range(low, high + 1), total)
    random.shuffle(numbers)
    return numbers

# Driver program
def main(args):
    size = args.size
    numbers = generate_numbers(args.low, args.high, args.size, args.seed)

    plt.bar([i for i in range(len(numbers))], numbers)
    plt.show(block=False)
    plt.pause(args.delay)
    plt.clf()

    selsort(numbers, args)

    for i in range(size):
        colors = ['darkgrey' if index not in range(0, i+1) else 'limegreen' for index in range(len(numbers))]
        plt.bar([i for i in range(len(numbers))], numbers, color=colors)
        plt.title(f'Successfully Sorted\nElapsed Time: {total_time:.2f} milliseconds')
        plt.show(block=False)
        plt.pause(args.delay/10)
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
