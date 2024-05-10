def shortest_job_first(jobs):
    jobs.sort(key=lambda x: x[1])
    schedule = []
    current_time = 0
    for job in jobs:
        job_name, duration = job
        schedule.append((job_name, current_time, current_time + duration))
        current_time += duration
    return schedule
jobs = [('Job1', 8), ('Job2', 4), ('Job3', 5), ('Job4', 3)]
schedule = shortest_job_first(jobs)
print("Job Schedule:")
for job in schedule:
    print("Job:", job[0], "| Start Time:", job[1], "| End Time:", job[2])
