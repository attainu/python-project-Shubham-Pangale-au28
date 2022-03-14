
def MazeSolver(s,loc):
    a=''
    arr=[l for l in s.strip() if l != ' ']
    # print(arr)
    for i in range(len(arr)):
        # print(loc,i)
        if i != loc:
            if i ==0:
                a+='0'
                # print('1')
            else :
                a+=' 0'
                # print('2')
                
        else:
            # print('s',i)
            if arr[i] == '0':
                # print(len(arr),arr)
                for j in range(len(arr)-i):
                    loc=i-1
                    a+=' 0'
                # print('3')   
                break
            else:
                
                if i ==0:
                    a+=arr[i]
                    # print('4')
                else :
                    a+=' '+arr[i]
                    # print('5')
                if i < len(arr)-1:
                    loc=i+1
                else:
                    loc=i
    return (a,loc)
maze = open('input.txt').readlines()
out_maze = open("output.txt","w")
maze3 = [i.rstrip() for i in maze]

loc=0
s=''
for i in maze3:
    s,loc=MazeSolver(i,loc)
    out_maze.write(s+'\n')
# maze.close()
out_maze.close()
                   
