print ("Дополнительное задание по модулю")
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_s = [round (sum (grades[0]) / len (grades[0]), 2), round (sum (grades[1]) / len (grades[1]), 2),
            round (sum (grades[2]) / len (grades[2]), 2), round (sum (grades[3]) / len (grades[3]), 2),
            round (sum (grades[4]) / len (grades[4]), 2)]
students_a = sorted (students)
sl_cl = {students_a[0]: grades_s[0], students_a[1]: grades_s[1], students_a[2]: grades_s[2], students_a[3]: grades_s[3],
         students_a[4]: grades_s[4]}
print (sl_cl)
