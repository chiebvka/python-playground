def decode(file):
    with open(file, 'r') as file:
        lines = file.readlines()

    pyramid = [line.split()[1:] for line in lines]
    decoded_words = [line[-1] for line in pyramid]

    message = ' '.join(decoded_words)
    return message

file = 'encoded.txt'  
message = decode(file)
print(message)
