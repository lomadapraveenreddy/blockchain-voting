class Vote:
    """
    vote class which stores pollID and the option chosen.
    """

    def __init__(self,pollID,option):
        self.pollID = pollID
        self.option = option

    def __repr__(self):
        return f'vote-({self.pollID} {self.option})'


    def __eq__(self,other):
        if self.pollID == other.pollID and self.option == other.option:
            return True
        return False

    def __lt__(self, other):
        if self.pollID<other.pollID:
            return True
        elif self.pollID>other.pollID:
            return False
        else:
            if self.option<=other.option:
                return True
            else:
                return False
    def __gt__(self, other):
        if self.pollID>other.pollID:
            return True
        elif self.pollID<other.pollID:
            return False
        else:
            if self.option>other.option:
                return True
            else:
                return False

if __name__ == '__main__':
    a=Vote('123','2')
    b=Vote('123','1')
    print(sorted([a,b]))