def find_pairs_with_sum(numbers, target_sum):
    pairs = []
    seen_numbers = set()

    for num in numbers:
        complement = target_sum - num
        if complement in seen_numbers:
            pairs.append((num, complement))
        seen_numbers.add(num)

    return pairs


if __name__ == "__main__":
    # Example usage:
    given_list = [2, 4, 3, 1, 5, 6, 8, 7]
    target_sum = 9

    result = find_pairs_with_sum(given_list, target_sum)
    if result:
        print(f"The following pairs have a sum of {target_sum}:")
        for pair in result:
            print(pair)
    else:
        print("No pairs found with the given sum.") 