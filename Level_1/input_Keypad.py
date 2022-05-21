import math

def solution(numbers, hand):

    answer = ""

    def phone_number_index(number):
        phone_numbers = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]] 
        for i in range(0, len(phone_numbers)):
            for j in range(0, len(phone_numbers[i])):
                if phone_numbers[i][j] == number:
                    return [i,j]

    def center_Length(left,right,center):
        if left == [] or right == []:
            return None

        left_x_location = left[0]
        left_y_location = left[1]

        right_x_location = right[0]
        right_y_location = right[1]

        center_x_location = center[0]
        center_y_location = center[1]

        l_c_x = abs(left_x_location - center_x_location)
        l_c_y = abs(left_y_location - center_y_location)

        r_c_x = abs(right_x_location - center_x_location)
        r_c_y = abs(right_y_location - center_y_location)

        l_c_length = math.sqrt(l_c_x+l_c_y)
        r_c_length = math.sqrt(r_c_x+r_c_y)

        if l_c_length < r_c_length:
            return "left"
        elif l_c_length > r_c_length:
            return "right"
        else:
            return "same"

    Left_hand = [3,0]
    Right_hand = [3,2]

    if hand == "right":
        for i in numbers:
            if i == 3 or i == 6 or i == 9:
                answer += "R"
                Right_hand = phone_number_index(i)
            elif i == 1 or i == 4 or i == 7:
                answer += "L"
                Left_hand = phone_number_index(i)
            else:
                if Right_hand == i:
                    answer += "R"
                elif Left_hand == i:
                    answer += "L"
                else:
                    center_position = phone_number_index(i)
                    center_result = center_Length(Left_hand,Right_hand,center_position)
                    if center_result == "left" or Left_hand == phone_number_index(i):
                        answer += "L"
                        Left_hand = phone_number_index(i)
                    else:
                        answer += "R"
                        Right_hand = phone_number_index(i)

    if hand == "left":
        for i in numbers:
            if i == 3 or i == 6 or i == 9:
                answer += "R"
                Right_hand = phone_number_index(i)
            elif i == 1 or i == 4 or i == 7:
                answer += "L"
                Left_hand = phone_number_index(i)
            else:
                center_position = phone_number_index(i)
                center_result = center_Length(Left_hand,Right_hand,center_position)
                if center_result == "right" or Right_hand == phone_number_index(i):
                    answer += "R"
                    Right_hand = phone_number_index(i)
                else:
                    answer += "L"
                    Left_hand = phone_number_index(i)

    return answer
