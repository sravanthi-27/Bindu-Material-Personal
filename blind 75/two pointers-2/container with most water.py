height = [1,1]
area = 0
left,right = 0,len(height)-1
while left<right:
    width=right-left 
    heights = min(height[right],height[left])
    area = max(area,heights*width)
    if height[left]<=height[right]:
        left+=1
    else:
        right-=1
print(area) 