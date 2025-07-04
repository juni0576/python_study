h=int(input("hours to seconds conversion"))
m=int(input("minutes to seconds conversion"))

h_seconds = h*60*60
m_seconds = m*60
message = "%d시간은 %d초이고, %d분은 %d초입니다"
total_seconds = h_seconds + m_seconds
print(message % (h, h_seconds, m, m_seconds,"총 초는 %d초입니다" % total_seconds))