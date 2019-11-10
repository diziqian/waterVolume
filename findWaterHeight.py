# Arr = [4,3,2,2,3,4]
# Arr = [1,4,3,2,2,3,4,1]
# Arr = [2,1,3,1,4,3,2,2,3,4,1]
Arr = [2,1,3,1,4,3,2,2,3,4,1,5,]

def main():
    voluem_total = 0
    lpos_max, max_num = get_max_height_left(0, len(Arr))

    lpos, max_num_l = get_max_height_left(0, lpos_max)
    voluem_total += get_water_volume(lpos, lpos_max, max_num_l)

    while lpos != 0:
        pos_max_left = lpos
        lpos, max_num_left = get_max_height_left(0, pos_max_left)
        voluem_total += get_water_volume(lpos, pos_max_left, max_num_left)

    rpos, max_num_r = get_max_height_right(lpos_max, len(Arr) - 1)
    voluem_total += get_water_volume_r(lpos_max, rpos, max_num_r)

    i = 0
    while rpos < len(Arr) - 1:
        pos_max_right = rpos
        rpos, max_num_right = get_max_height_right(pos_max_right, len(Arr)-1)
        voluem_total += get_water_volume_r(pos_max_right, rpos, max_num_right)

    print("VolumeTotal:\t", voluem_total)

def get_max_height_left(left_Pos, right_Pos):
    pos = left_Pos
    max_Num = Arr[left_Pos]

    pos_temp = left_Pos
    while pos_temp < right_Pos:
        if max_Num < Arr[pos_temp]:
            max_Num = Arr[pos_temp]
            pos = pos_temp
        pos_temp += 1

    return pos, max_Num


def get_max_height_right(left_Pos, right_Pos):
    pos = right_Pos
    max_Num = Arr[right_Pos]

    pos_temp = right_Pos
    while pos_temp > left_Pos:
        if max_Num < Arr[pos_temp]:
            max_Num = Arr[pos_temp]
            pos = pos_temp
        pos_temp -= 1

    return pos, max_Num

def get_water_volume(left_pos, right_pos, max_num):
    l_pos = left_pos
    volume = 0

    while l_pos < right_pos:
        volume += max_num - Arr[l_pos] if max_num - Arr[l_pos] >0 else 0
        l_pos += 1

    return volume

def get_water_volume_r(left_pos, right_pos, max_num):
    r_pos = right_pos
    volume  = 0

    while r_pos > left_pos:
        volume += max_num - Arr[r_pos] if max_num - Arr[r_pos] > 0 else 0
        r_pos -= 1

    return volume

if __name__ == "__main__":
    main()
