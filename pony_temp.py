import matplotlib.pyplot as plt
import random

# plot recored CPU temps
# should make the dates go on the x-axis like in the typing club graph

temps = []
with open("/home/mattb/maintenance/pony_temp_log") as f:
    for line in f:
        # add a jitter to the temp for visability
        # only take the first 12 values (the date is after that)
        temp = [int(core)+random.uniform(-0.2,0.2) for idx,core in
                enumerate(line.split()) if idx<=11]

        temps.append(temp)

# got this from google... it basically transposes the list
all_core_logs = list(map(list, zip(*temps)))

for core_log in all_core_logs:
    plt.plot(core_log, '.-', linewidth=2, markersize=10)

plt.title('Twice daily (11am and 4pm) Pony core temps')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Temp (+/- 0.2 deg)')
plt.grid(axis='y')
ax = plt.gca()
plt.show()
