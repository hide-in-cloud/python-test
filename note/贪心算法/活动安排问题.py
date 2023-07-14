def get_max_intervalSchedule(job_list):
    job_schedule = []
    num_jobs = len(job_list)
    job_list.sort(key=lambda x: x[2])  # 按照结束时间对所有的job排序
    for i in range(num_jobs):
        if not job_schedule:  # 如果为空
            job_schedule.append(job_list[i])
        else:
            if job_list[i][1] >= job_schedule[-1][2]:  # 新任务的开始时间大于上一个任务的结束时间
                job_schedule.append(job_list[i])
    return job_schedule


if __name__ == '__main__':
    job_list = [['a', 8, 10], ['b', 1, 5], ['c', 4, 8], ['d', 1, 3], ['e', 6, 9], ['f', 2, 4], ['g', 4, 7], ['h', 1, 5], ['i', 6, 12]]
    job_schedule = get_max_intervalSchedule(job_list)
    print(job_schedule)
