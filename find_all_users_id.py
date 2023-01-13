from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    ans = []
    users = data['messages']
    for i in users:
        if i['type'] == 'service' and i.get('actor_id') not in ans:
            ans.append(i.get('actor_id'))
    return ans
d = read_data('data/result.json')
print(find_all_users_id(d))