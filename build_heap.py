# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    #for i in range(0, len(data)):
    if data[4]<data[1]:
        (data[4],data[1]) = (data[4],data[1])
        swaps.append([data[4],data[1]])
    if data[1]<data[0]:
        (data[1],data[0]) = (data[1],data[0])
        swaps.append([0,1])
    if data[4]<data[2]:
        (data[4],data[2]) = (data[4],data[2])
        swaps.append([1,3])
    
   
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    mode = input()

    if mode == "F":
        name = input()
        with open("./tests/" + name, mode="r") as fails:
            n = fails.readline()
            data = fails.readline()

    if mode == "I":
    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
   

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) < 4*len(data)
   
    

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
