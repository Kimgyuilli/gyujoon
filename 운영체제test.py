def add_job(page_frame, job, counter, countofjob):
    if 'empty' in page_frame: #빈 페이지가 있으면
        for _ in range(len(page_frame)):
            if page_frame[_] == 'empty': #비어있는 페이지를 발견하면 job을 넣고 다음 job으로 간다.
                page_frame[_] = job
                counter[_] = countofjob #페이지 counter에 job을 넣은 시간 저장
                return #반환하고 종료
    page_frame[counter.index(min(counter))] = job #페이지에 job 넣고
    counter[counter.index(min(counter))] = countofjob #counter 갱신
        
                    
            

print("페이지의 수 입력.")
NumOfPage = int(input()) #페이지를 몇개로 할지 입력받는다
if NumOfPage < 1:
    while NumOfPage < 1:
        print("1 이상의 숫자를 입력해주세요")
        NumOfPage = int(input())
    
PageFrame = ['empty' for i in range(NumOfPage)]  #공백으로 빈 페이지를 채우며 페이지 생성
counter = [0 for i in range(NumOfPage)] #가장 마지막에 쓰인 페이지를 판별하기 위한 counter
CountOfjob = 0
PageFault = 0 
while True:
    print("job입력. (종료하려면 엔터):", end = '')
    job = input() #job입력받기
    if job == '': #종료신호 받으면 종료
        break
    if job not in PageFrame: #job에 pageframe에 없을 떄
        print("\n*Pagefault!*\n") #pagefault!
        PageFault += 1
        add_job(PageFrame, job, counter, CountOfjob) #함수 호출
    else: #job이 pageframe에 있으면
        counter[PageFrame.index(job)] = CountOfjob #해당 job의 counter 갱신
    CountOfjob += 1
    print("PageFrame:", end = ' ') # 이 아래는 결과 출력
    for _ in range(NumOfPage):
        print(f"page{_}: [{PageFrame[_]}] ", end = ' ')
    print("counter=", counter)
    print("--------------------------------------------------------")
print("\n----------------------------------------------------------")
print(f"페이지 요구 수:{CountOfjob}  Pagefault 수:{PageFault} 페이지 접근 실패율:{round(PageFault/CountOfjob*100, 2)}%")
print("----------------------------------------------------------")
