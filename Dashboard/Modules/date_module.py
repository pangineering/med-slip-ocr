

class Clean_Date:

    def __init__(self,date_string):
        self.day = date_string[0]
        self.month = date_string[2]
        self.year = date_string[1]

    def whatMonth(self):
        first_lettter = self.month[0]
        second_lettter = self.month[1]
        third_lettter = self.month[2]

        if first_lettter == 'S' or first_lettter == 'O' or first_lettter == 'N' or first_lettter == 'D' or first_lettter == "F":
            if first_lettter == 'S':
                month = ["Sep","09"]
            elif first_lettter == 'O':
                month = ["Oct","10"]
            elif first_lettter == 'N':
                month = ["Nov","11"]
            elif first_lettter == 'F':
                month = ["Feb","02"]
            else:
                month = ["Dec","12"]
        elif first_lettter == 'J':
            if third_lettter == 'n':
                if second_lettter == 'a':
                    month = ["Jan","01"]
                else:
                    month = ["Jun","06"]
            else:
                month = ["Jul","07"]
        elif first_lettter == "M":
            if third_lettter == 'r':
                month = ["Mar","03"]
            else:
                month = ["May","05"]
        elif first_lettter == 'A':
            if second_lettter == 'u':
                month = ["Aug","08"]
            else:
                month = ["Apr","04"]
        else:
            month = ["None","0"]

        return month


    def formatDate(self):
        month = self.whatMonth()
        date = month[1] + '/' + self.day + '/' + self.year

        return date
        