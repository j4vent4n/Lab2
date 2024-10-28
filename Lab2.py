
def display_main_menu():
    print ("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def calc_average_temperature(temp_list):
    return sum(temp_list)/len(temp_list) if len(temp_list)> 0 else 0


def get_user_input() :
    user_input = input()


def find_min_max(temp_list):
    if not temp_list:
        return [None, None]
    return [min(temp_list), max(temp_list)]

def sort_temperature(temp_list):
    return sorted (temp_list)    

def calc_median_temperature(temp_list):
    print("calc_median_temperature")     




def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") 
    display_main_menu() 
    num_list = get_user_input() 


    def get_user_input() :user_input = input()


if __name__ == "__main__": 
    main()
