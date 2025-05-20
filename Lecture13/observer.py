class Follower:
    def __init__ (self, name):
        self.follower_name = name
        def react (self):
            print (self.follower_name, "лайкает сообщение:")
        def __str__(self):
            return f"follower ({self.follower_name})"
        def __repr__(self):
            return f"follower ({self.follower_name})"

        
class Creator:
    def __init__(self, name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(slef.sub_list)
    def notify_all(self):
        for follower in self.sub_list:
            follower.react()
    def create_post(self, mes):
        print (self.creator_name, "опубликовал это сообщение:")
        print(mes)
        print ()

creator1=Creator("1st chan")
f1= Follower("Kate")
f2= Follower("Anna")
f3= Follower("Peter")
creator1.show_followers()
