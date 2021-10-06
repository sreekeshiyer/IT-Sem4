    RollNo = row[0]  
            First_Name = row[1]  
            Last_Name = row[2]  
            City = row[3]  
            State = row[4]  
            Phone_Number = row[5]  
            DOB = row[6]  
            self.tvStudent.insert("", 'end', text=RollNo, values=(RollNo, First_Name, Last_Name, City, State, Phone_Number,DOB)) 