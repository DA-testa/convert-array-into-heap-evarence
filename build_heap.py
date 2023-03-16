# python3


def swaping(data, i, res):
    left_child = 2*i + 1
    right_child = 2*i + 2
    n = len(data) 
    
    if left_child >= n:
        return
    
    x = left_child 
    if right_child < n and data[left_child] > data[right_child]:
        x = right_child
    #print(x)
    if data[i] > data[x]:  
        res.append([i, x]) 
         
        data[i], data[x] = data[x], data[i]
        swaping(data, x, res) 

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(int((n - 2)/2), -1, -1):
        #print(i)
        swaping(data,i, swaps)


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
 
