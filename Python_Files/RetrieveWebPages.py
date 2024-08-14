import urllib.request, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# Initialize an empty dictionary to store word counts
counts = dict()

# Iterate over each line in the file handle 'fhand'
for line in fhand:
    # Decode the line from bytes to string and split it into a list of words
    words = line.decode().split()

    # Iterate over each word in the list of words
    for word in words:
        # If the word is already in the 'counts' dictionary, retrieve its current count
        # Otherwise, initialize the count to 0
        # Then increment the count by 1 and store the updated count in the dictionary
        counts[word] = counts.get(word, 0) + 1

# Print the final 'counts' dictionary containing words as keys and their frequencies as values
print(counts)
