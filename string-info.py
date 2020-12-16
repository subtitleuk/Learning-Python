#!/usr/bin/env python3.7

# EX Lab 2

message = input("Please Enter a message: ")

print("First character:", message[0])
print("Last character:", message[-1])

print("Middle character:", message[int(len(message) / 2)])

# Use a slicing to select even then odd index characters
print("Even index characters:", message[0::2])
print("Odd index characters:", message[1::2])

# Print the String in Reverse with no slick index and -1 step value
print("Reversed message:", message[::-1])