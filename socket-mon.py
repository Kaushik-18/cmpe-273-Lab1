import psutil
import collections

pslist = psutil.net_connections()

print('pid  ', 'laddr       ', 'raddr        ', 'status            ', sep=',')
op_list = []
for socket in pslist:
    if socket.pid:
        if socket.laddr or socket.raddr:
            ls, rs = '', ''
            if socket.laddr:
                ls = str(socket.laddr[0]) + "@" + str(socket.laddr[1])
            if socket.raddr:
                rs = str(socket.raddr[0]) + "@" + str(socket.raddr[1])
            op_list.append((socket.pid, ls, rs, socket.status))

# taking a counter object ;
#  passing a list of all pids to constructor;
# will give dictionary of occurrences of pid
count = collections.Counter(x[0] for x in op_list)
# sort by number of occurrences from counter dictionary
final_list = sorted(op_list, key=lambda x: count[x[0]])

for output_obj in final_list:
    print(output_obj[0], output_obj[1], output_obj[2], output_obj[3], sep=' ,')
