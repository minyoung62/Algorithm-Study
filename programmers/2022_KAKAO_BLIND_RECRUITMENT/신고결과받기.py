def solution(id_list, report, k):
    answer = []

    reportCount = dict((x,0) for x in id_list)
    revers = dict((x,set()) for x in id_list)

    # report 분리
    for r in report:
        reporter, reported=r.split()
        if reporter not in revers[reported]:
            reportCount[reported] += 1
        revers[reported].add(reporter)

    # 신고 결과
    result = dict((x,0) for x in id_list)

    # 신고당한 횟수 count
    for key in reportCount.keys():
        if reportCount[key] >= k:
            for reporter in revers[key]:
                result[reporter] += 1

    answer = list(result.values())

    return answer

def renew_solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = set(report)

    reportCount = dict((x, 0) for x in id_list)
    for r in report:
        reportCount[r.split()[1]] += 1

    for r in report:
        if reportCount[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1



    return answer