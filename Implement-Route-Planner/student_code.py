import heapq

def shortest_path(M, start, goal):
    
    min_heap = []
    
    init_score = distance(M,start,goal)
    heapq.heappush(min_heap, (init_score, [start]))
    last_pos = start

    while len(min_heap) > 0:
        current_score, visited_list = heapq.heappop(min_heap)
        current_pos = visited_list[-1]
        
        if current_pos == goal:
            return visited_list
        
        candidates = M.roads[current_pos]
        
        for candidate in candidates:
            score = calc_score(M, current_pos, candidate, goal)
            new_visited_list = visited_list + [candidate]
            heapq.heappush(min_heap, (score, new_visited_list))
            
    return None

def distance(M, start, goal):
    start_x = M.intersections[start][0]
    start_y = M.intersections[start][1]
    goal_x = M.intersections[goal][0]
    goal_y = M.intersections[goal][1]
    
    return ((goal_x - start_x) ** 2 + (goal_y - start_y) ** 2) ** 0.5

def calc_score(M, current_pos, next_pos, goal):
    '''
    Score is calculated as sum of these:
    * Distance between current_pos and next_pos
    * Distance between next_pos and goal as a heuristic estimation of the next_pos
    '''
    return distance(M, current_pos, next_pos) + distance(M, next_pos, goal)
