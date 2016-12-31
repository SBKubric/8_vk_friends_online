import vk
import vk.exceptions
import getpass

APP_ID = 5802132


def get_user_login():
    return input('Login:')


def get_user_password():
    return getpass.getpass()


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    online_friends_ids = api.friends.getOnline()
    online_friends = api.users.get(user_ids=online_friends_ids)
    return online_friends


def output_friends_to_console(friends_online):
    print('Are online:')
    for num, friend_online in enumerate(friends_online, start=1):
        print('%s %s %s' % (num, friend_online['first_name'], friend_online['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    while True:
        try:
            print('Loading...')
            friends_online = get_online_friends(login, password)
            output_friends_to_console(friends_online)
            break
        except vk.exceptions.VkAuthError:
            print('Authentication failed! Looks like you have typo in login or password.')
            login = get_user_login()
            password = get_user_password()
