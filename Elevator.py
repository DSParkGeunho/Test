length=0
last_floor=1
while(True):
    numPeople = int(input("type a number of mens : "))
    if numPeople>10 or numPeople=='':
        print("최대 수용인원을 초과하였거나 입력을 종료합니다.")
        break
    else:
        next_floor=[last_floor]
        real_floor=[last_floor]
        for i in range(numPeople):
            next_floor.append(int(input("type floors: ")))
        abs_floor=[]
        for j in range(numPeople):
            abs_floor.append(abs(next_floor[0]-next_floor[j+1]))
       
        for k in range(numPeople):
            real_floor.append([next_floor[k+1],abs_floor[k]])
        real_floor[0]=[last_floor,0]
        
        real_floor.sort(key=lambda x: x[1])

        for l in range(numPeople):
            if real_floor[l+1][0]==real_floor[l][0]:
                continue
            else:    
                print("{}층에 도착하였습니다.".format(real_floor[l+1][0]))
                length=length+(abs(real_floor[l+1][0]-real_floor[l][0]))
    
        last_floor=real_floor[-1][0]
        print("총이동거리 {}".format(length))

    
