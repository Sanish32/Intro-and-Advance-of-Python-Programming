# Copy here code of line function from previous exercise

def triangle(size):
    # You should call function line here with proper parameters
    i=0
    while i<size:
        line(i+1, "#")
        i+=1
def line(j,character):
    if character=="#":
        word="#"
    else:
        word=character[0]
    print(word*j)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
