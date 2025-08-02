# Homework. Lesson 12
# Exercise 1: Threaded Prime Number Checker

import os
from collections import Counter
import threading


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def check_primes_in_range(start, end, result_list):
    local_primes = []
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    result_list.extend(local_primes)


def find_primes_with_threads(start, end, num_threads=4):
    threads = []
    result = []
    result_lock = threading.Lock()
    step = (end - start) // num_threads

    def thread_func(s, e):
        local_result = []
        check_primes_in_range(s, e, local_result)
        with result_lock:
            result.extend(local_result)

    for i in range(num_threads):
        sub_start = start + i * step
        sub_end = start + (i + 1) * step if i < num_threads - 1 else end
        t = threading.Thread(target=thread_func, args=(sub_start, sub_end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    result.sort()
    return result


# Example usage:
start_range = 1
end_range = 100
prime_numbers = find_primes_with_threads(start_range, end_range, num_threads=4)
print(f"Prime numbers between {start_range} and {end_range}:")
print(prime_numbers)

# Exercise 2: Threaded File Processing


def process_lines(lines, local_counter):
    for line in lines:
        words = line.strip().lower().split()
        local_counter.update(words)


def count_words_threaded(filename, num_threads=4):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    counters = [Counter() for _ in range(num_threads)]

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i < num_threads - \
            1 else total_lines
        thread_lines = lines[start_index:end_index]
        t = threading.Thread(target=process_lines,
                             args=(thread_lines, counters[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Merge all counters
    total_counter = Counter()
    for counter in counters:
        total_counter.update(counter)

    return total_counter


# === Example usage ===
if __name__ == "__main__":
    filename = 'large_text.txt'  # Replace with your file name
    if os.path.exists(filename):
        result = count_words_threaded(filename, num_threads=4)
        for word, count in result.most_common(20):  # Show top 20 words
            print(f"{word}: {count}")
    else:
        print(f"File '{filename}' not found.")
