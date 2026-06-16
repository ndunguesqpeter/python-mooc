stud_course = int(input("No of student in a course: "))
gr_size = int(input("Desired group size: "))
#
desired = (stud_course + gr_size -1) // gr_size
print(f"number of group formed: {desired}")