import calendar
 
def count_digit(y, m, x):
    cnt = 0
    target = str(x)
    days = calendar.monthrange(y, m)[1]
    for d in range(1, days + 1):
        # 格式 yyyy-mm-dd
        s = f"{y:04d}-{m:02d}-{d:02d}"
        cnt += s.count(target)
    return cnt
 
def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        y, m, x = map(int, line.split())
        print(count_digit(y, m, x))
 
if __name__ == "__main__":
    main()