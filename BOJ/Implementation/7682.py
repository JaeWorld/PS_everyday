# BOJ 7682 틱택토

# 구현

if __name__ == "__main__":
    while True:
        s = input()
        if s == 'end':
            break
        
        cntx, cnto = 0, 0
        seqx, seqo = 0, 0
        b = [[] for _ in range(3)]

        # 배열로 입력받으면서 X, O 개수 세기
        for i in range(3):
            for j in range(3):
                if s[3*i+j] == 'X':
                    cntx += 1
                if s[3*i+j] == 'O':
                    cnto += 1
                b[i].append(s[3*i+j])

        # O의 개수가 X의 개수보다 많을 수 없음
        if cnto > cntx:
            print('invalid')
            continue

        # X의 개수와 O의 개수의 차가 1 초과일 수 없음
        if cntx - cnto > 1:
            print('invalid')
            continue

        # 세로 3연속 체크
        for i in range(3):
            prev = b[0][i]
            flag = True
            for j in range(1, 3):
                if b[j][i] != prev:
                    flag = False
                    break
                prev = b[j][i]
            if flag:
                if prev == 'X':
                    seqx += 1
                if prev == 'O':
                    seqo += 1

        # 가로 3연속 체크
        for i in range(3):
            prev = b[i][0]
            flag = True
            for j in range(1, 3):
                if b[i][j] != prev:
                    flag = False
                    break
                prev = b[i][j]
            if flag:
                if prev == 'X':
                    seqx += 1
                if prev == 'O':
                    seqo += 1
                
        # 대각선 3연속 체크
        flag = True
        prev = b[0][0]
        for i in range(1, 3):
            if b[i][i] != prev:
                flag = False
                break
            if i == 2 and flag:
                if prev == 'X':
                    seqx += 1
                if prev == 'O':
                    seqo += 1
        
        flag = True
        prev = b[2][0]
        for i in range(1, 3):
            if b[2-i][i] != prev:
                flag = False
                break
            if i == 2 and flag:
                if prev == 'X':
                    seqx += 1
                if prev == 'O':
                    seqo += 1
            
        # 승자가 두명 있을 수 없음
        if seqo > 0 and seqx > 0:
            print('invalid')
            continue
        # O가 이기고 X의 개수가 O의 개수보다 많을 수 없음 (게임 종료되기 때문)
        if seqo > 0 and cntx > cnto:
            print('invalid')
            continue
        # X가 이기고 O의 개수와 X의 개수가 같을 수 없음 (게암 종료되기 때문)
        if seqx > 0 and cntx == cnto:
            print('invalid')
            continue
        # 칸이 다 채워지지 않았는데 승자가 존재하지 않을 수 없음
        if cntx+cnto < 9 and seqx == 0 and seqo == 0:
            print('invalid')
            continue
        
        # 나머지 경우는 모두 가능
        print('valid')
    
        
