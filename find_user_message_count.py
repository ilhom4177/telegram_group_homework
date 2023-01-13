from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    a = 0
    data = data['messages']
    for i in data:
        if i['type'] == 'message' and i['from_id'] == users_id:
            a += 1
    return a
y = read_data('data/result.json')
user = find_all_users_id(y)
print(find_user_message_count(y,user[1]))