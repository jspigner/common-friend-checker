# Check to see if two friends has a mutual friend in their social media circle
# Used Friends cast as an example

# Define
def is_common_friend(user, friends_a, friends_b):
    is_friend_a = friends_a.count(user) >= 1
    is_friend_b = friends_b.count(user) >= 1

    is_common = is_friend_a & is_friend_b

    return is_common

friends_joey = ["Monica", "Rachel", "Chandler"]
friends_monica = ["Phoebe", "Rachel", "Chandler"]
common_chandler = is_common_friend("Chandler", friends_joey, friends_monica)
print(f"Chandler is a common friend: {common_chandler}")