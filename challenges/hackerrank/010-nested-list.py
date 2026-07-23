if __name__ == '__main__':
    
    records = []
    scores = []
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
        
    sort_list=sorted(list(set(scores)))
    second_lowest=sort_list[1]
    
    for name,score in records:
        if (score == second_lowest):
            names.append(name)
            
    sort_names= sorted(names)
    
    for i in sort_names:
        print(i)
        
    
