import pymongo
from datetime import datetime


class MarkAttendence:
    def __init__(self):
        self.today_date = datetime.now().date().strftime("%Y-%m-%d")
        self.dbData = pymongo.MongoClient(
            "mongodb+srv://talat:mongo@test.wupry.mongodb.net/attendancesystems?retryWrites=true&w=majority"
        )
        self.update_data()

    def update_data(self):
        self.attendence_data = list(
            self.dbData.attendancesystems.app1_attendance.find(
                {"Date": self.today_date}
            )
        )
        # print(self.attendence_data)

    def insert_attendence(self, id, name, current_time, current_date):
        if current_date != self.today_date:
            self.today_date = current_date
            self.update_data()

        if not list(filter(lambda x: x["emp_id"] == id, self.attendence_data)):
            data = {
                "emp_id": id,
                "name": name,
                "Time": current_time,
                "Date": current_date,
                "Status": "Present",
            }
            self.dbData.attendancesystems.app1_attendance.insert_one(data)
            self.attendence_data.append(data)
