# This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string 
# and then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, one per line, 
# sorted by hour as shown below.


file = open('mbox-short.txt')
hours_dict = dict()
for line in file:
    if line.startswith('From '):
        words = line.split()
        time = words[5].split(':')
        #word = word.split(':')
        time = time[0]
        hours_dict[time] = hours_dict.get(time, 0) + 1
print(hours_dict)
hours_tuple_list = sorted(hours_dict.items())
print(hours_tuple_list)
for k,v in hours_tuple_list:
    print(k, v)
