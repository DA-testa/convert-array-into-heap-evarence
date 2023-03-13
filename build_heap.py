# python3


def mins(a, i, res):
    n = len(a)
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child >= n:
        return
    child = left_child
    if right_child < n and a[right_child] < a[left_child]:
        child = right_child
    if a[child] < a[i]:  
        res.append([i, child])
        a[i], a[child] = a[child], a[i]
        mins(a, child, res)

def build_heap(a):
    res = []
    n = len(a)
    for i in range((n - 2)//2, -1, -1):
        mins(a, i, res)
    return res



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
                data = list(map(int, input().split()))
                


    elif "I" in mode:
        n = int(input())
        data = list(map(int, input().split()))

    else:
        return

    swaps = build_heap(data)
    assert len(data) == n
    assert len(swaps) < 4*len(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    

if __name__ == "__main__":
    main()
 
