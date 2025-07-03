h=int(input("hours to seconds conversion"))
m=int(input("minutes to seconds conversion"))

h_seconds = h*3600
m_seconds = m*60
message = "%d시간은 %d초이고, %d분은 %d초입니다"
print(message % (h, h_seconds, m, m_seconds))