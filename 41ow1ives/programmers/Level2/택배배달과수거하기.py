def solution(cap, n, deliveries, pickups):
    answer = 0

    d = 0
    p = 0

    for i in range(n-1, -1, -1):

        cnt = 0

        d -= deliveries[i]
        p -= pickups[i]

        while d < 0 or p < 0:
            d += cap
            p += cap
            cnt += 1

        answer += (i + 1) * 2 * cnt

    return answer


######### 시간초과
"""
def find_farthest_place(places:list, n:int):
    for idx, place in enumerate(places, 0):
        if place != 0:
            return idx, place
    return n, n # 전부 0인 경우 대비


def solution(cap:int, n:int, deliveries:list, pickups:list)->int:
    answer = 0
    
    # 수거해야하는 개수와 배달해야 하는 전체 개수를 먼저 파악
    total_delivery, total_pickup = sum(deliveries), sum(pickups)
    deliveries, pickups = [0] + deliveries, [0] + pickups # indexing 편하게 하려고 앞에 0 추가
    deliveries.reverse(), pickups.reverse() # 가장 먼 곳 부터 접근해야 하니까 빠르게 하기 위해 뒤집음
    
    # 가장 먼 곳 (=뒤집은 상태에선 가장 가까운 곳) 에서부터 배달과 수거를 끝내야함
    while total_delivery>0 or total_pickup>0:
        farthest_delivery_place, farthest_delivery_count = find_farthest_place(deliveries, n)
        farthest_pickup_place, farthest_pickup_count = find_farthest_place(pickups, n)
        goal = farthest_delivery_place if farthest_delivery_place <= farthest_pickup_place else farthest_pickup_place
        answer += (n - goal)*2
        
        cur_cap = 0
        if total_delivery > 0:
            for idx, place in enumerate(deliveries[goal:],goal):
                if cur_cap + place > cap:
                    deliveries[idx] = place - (cap - cur_cap)
                    cur_cap += cap - cur_cap
                    break
                else:
                    cur_cap += place
                    deliveries[idx] = 0
            total_delivery -= cur_cap
            
        cur_cap = 0
        if total_pickup > 0:
            for idx, place in enumerate(pickups[goal:],goal):
                if cur_cap + place > cap:
                    pickups[idx] = place - (cap - cur_cap)
                    cur_cap += cap - cur_cap
                    break
                else:
                    cur_cap += place
                    pickups[idx] = 0
            total_pickup -= cur_cap

    return answer
"""



######### 틀린코드
"""
def find_most_far_house(house_list, cap, n, mode = "deliver"):
    house_list = reversed(house_list)
    visit_list = []
    if mode == "deliver":
        for idx, house in enumerate(house_list):
            if house>0:
                visit_list.append(n-idx)
                cap -= house
                if cap <= 0:
                    break
    else:
        count = 0
        for idx, house in enumerate(house_list):
            if house > 0:
                visit_list.append(n-idx)
                count += house
                if count >= cap:
                    break     
    return visit_list



def solution(cap, n, deliveries, pickups):
    # 먼 것 부터 처리해야겠지?
    total_delivery = sum(deliveries)
    total_pickup = sum(pickups)
    deliveries.insert(0,0)
    pickups.insert(0,0)
    answer = 0
    cur_cap = cap # 물류창고에서 가득 들고 출발! -> 꼭 가득 안 들어도 되는거? 상관 없음
    while total_delivery > 0 or total_pickup > 0:
        # 먼저 배달 부터 해야 하고 "가는 길"에 하나씩 배달을 해 주는거
        post_deliver_list = find_most_far_house(deliveries, cap, n)
        for cur_deliver in post_deliver_list:
            cur_house = deliveries[cur_deliver]
            if cur_cap >= cur_house:
                deliveries[cur_deliver] = 0
                total_delivery -= cur_house
                cur_cap -= cur_house
            else:
                # 배달할 수 있는 범위 내에 가장 가까운 집
                deliveries[cur_deliver] = cur_house - cur_cap
                total_delivery -= cur_cap
                cur_cap = 0
        # 배달 가는 곳 중 제일 먼저 찍었고 이제는 픽업!
        post_pickup_list = find_most_far_house(pickups, cap, n, mode="pickup")
        for cur_pickup in post_pickup_list:
            cur_house = pickups[cur_pickup]
            if cur_cap+cur_house <= cap:
                pickups[cur_pickup] = 0
                total_pickup -= cur_house
                cur_cap += cur_house
            else:
                # 픽업할 수 있는 범위 내에 가장 가까운 집
                pickups[cur_pickup] = cur_house - cur_cap
                total_pickup -= cur_cap
                cur_cap = cap
        if post_deliver_list[0] > post_pickup_list[0]:
            answer += post_deliver_list[0] * 2
        else:
            answer += post_pickup_list[0] * 2
    return answer

"""