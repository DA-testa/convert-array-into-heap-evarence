# python3


def mins(data, i, res):
    n = len(data)

    left_child = 2*i + 1
    right_child = 2*i + 2

    if left_child >= n:
        return
    
    x = left_child 
    if right_child < n and data[right_child] < data[left_child]:
        x = right_child
    #print(x)
    if data[x] < data[i]:  
        res.append([i, x]) 
        data[i], data[x] = data[x], data[i]
        mins(data, x, res) 

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(int((n - 2)/2), -1, -1):
        #print(i)
        mins(data,i, swaps)


    return swaps



def main():
    
    mode = input()

    if "F" in mode:
        name = input()
        if name != "a":
            with open("./tests/" + name, mode="r") as fails:
                file = fails.read()
                text = file.splitlines()
                n = int(text[0])
                data = text[1]
                data = list(map(int, data.split()))
                

    elif "I" in mode:
        n = int(input()) 
        data = list(map(int, input().split()))

    else:
        return
    
    assert len(data) == n

    swaps = build_heap(data) 
    
    assert len(swaps) < 4*len(data)

    print(len(swaps))
    for i, j in swaps: 
        print(i, j)
    

if __name__ == "__main__":
    main()
 
