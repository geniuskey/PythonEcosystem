from multiprocessing import Process

def print_func(continent='Asia'):
    print('The name of continent is : ', continent)

if __name__ == "__main__":
    names = ['America', 'Europe', 'Africa']
    procs = []
    proc = Process(target=print_func)  # 프로세스 객체 생성
    procs.append(proc)
    proc.start()

    # 다른 프로세스 시작
    for name in names:
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # 모든 프로세스의 종료 대기
    for proc in procs:
        proc.join()
