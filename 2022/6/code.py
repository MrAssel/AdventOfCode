# Check if a string only contains unique characters
def unique(s):
    return len(set(s)) == len(s)

# Slides through string to find where a sequence of unique characters first occurs
def sliding_window(stream:str,window_size:int):
    for i in range(len(stream)-window_size):
        sliding_str = stream[i:i+window_size]
        if unique(sliding_str):
            return(i+window_size)
    return -1

if __name__ == "__main__":
    input_path = r'2022\6\input'

    with open(input_path) as file:
        datastream_buffer = file.readline()

    # Part 1
    print(sliding_window(stream=datastream_buffer,window_size=4))

    # Part 2
    print(sliding_window(stream=datastream_buffer,window_size=14))

