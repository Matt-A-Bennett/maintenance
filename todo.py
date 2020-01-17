# dates must be in dd-mm-yy format

import subprocess
from os import listdir
from os.path import isfile, join
from datetime import datetime

tasks = []
with open('/home/mattb/maintenance/todo_master.md', 'r') as todo:
    tasks.append(todo.read())
    tasks = tasks[0].split('\n')
    tasks.pop()

# gather tasks from all files in dirs
with open('/home/mattb/maintenance/todo_dirs.txt') as todo_dirs:
    for todo_dir in todo_dirs: 
        todo_dir=todo_dir.strip()

        files = [f for f in listdir(todo_dir) if isfile(join(todo_dir, f)) and f[0]!='.']
        for document in files: 
            print(join(todo_dir, document))
            document = join(todo_dir, document)

            query = subprocess.run(["grep", "-n", "(deadline:", f"{document}"], stdout=subprocess.PIPE).stdout.decode('utf-8')

            query = query.split('\n')
            query.pop()
            print('query before x box check')
            print(query)

            for query_idx, query_inst in enumerate(query):
                for task in tasks:
                    if (query_inst.split(']', 1)[-1].rstrip() == task.split(']', 1)[-1].rstrip()):
                        print('match task found')
                        print(f'query_inst: {query_inst}')
                        print(f'task: {task}')
                        query[query_idx] = ''
                        print(f'query after removing from inst from list: {query}')
                        if (query_inst.split('[', 1)[-1].rstrip() != task.split('[', 1)[-1].rstrip()):
                            print('x box check shows difference... synching with master')
                            # synch original with master
                            with open(f'{document}', 'r') as doc:
                                data = doc.readlines()
                                data[int(query_inst.split(':',1)[0])-1] = task
                            with open(f'{document}', 'w') as doc:
                                doc.writelines(data)
                        break 
# 
            # query = [query_inst.split(':',1)[-1] for query_inst in query]
            # query = str.join('\n', query)
            # tasks.append(query)
# 
# tasks = str.join('', tasks)
# tasks = tasks.split('\n')
# tasks = [task.rstrip() for task in tasks if task]
# # remove duplicate entries 
# tasks = list(set(tasks))
# 
# print(tasks)
# # sort tasks based on date
# dates = [date.split('(deadline: ')[-1][:-1] for date in tasks]
# dts = [datetime.strptime(date, '%d-%m-%y') for date in dates]
# ordered_tasks = [x for _,x in sorted(zip(dts, tasks))]
# 
# ordered_tasks = str.join('\n', ordered_tasks)
# print(ordered_tasks)
# 
# with open('/home/mattb/maintenance/todo_master.md', 'w') as todo:
    # todo.write(f'{ordered_tasks}\n')
