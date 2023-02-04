import math

def solution(fees, records):

    fee = {}
    in_dict = {}
    out_dict = {}

    for r in records:
        time, car, inout = r.split()
        if inout == 'IN':
            if car in in_dict.keys():
                in_dict[car].append(time)
            else:
                in_dict[car] = [time]
        else:
            if car in out_dict.keys():
                out_dict[car].append(time)
            else:
                out_dict[car] = [time]

    for car in in_dict.keys():
        if car not in out_dict.keys():
            out_dict[car] = ['23:59']
        else:
            if len(in_dict[car]) != len(out_dict[car]):
                out_dict[car].append('23:59')

        total_time = 0
        for i, in_time in enumerate(in_dict[car]):
            out_time = out_dict[car][i]
            in_h, in_m = map(int, in_time.split(":"))
            out_h, out_m = map(int, out_time.split(":"))
            total_time += 60*(out_h - in_h) + (out_m-in_m)

        print(total_time)
        if total_time - fees[0] > 0:
            fee[car] = fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]
        else:
            fee[car] = fees[1]


    fee = dict(sorted(fee.items()))
    answer = list(fee.values())

    return answer