while True:
    num = int(input('enter a number: '))
    for i in range(1,11):
        print(f'{num}*{i}={num*i}')
    ans = input('do you want to continue(y/n):')
    if ans=='n':
        break
    
