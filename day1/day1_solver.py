def count_depth_increases(dp):
    length = len(dp)
    zipped = list(zip(dp[0:length-1], dp[1:length]))
    increases = list(filter(lambda t : t[0] < t[1]  ,zipped))
    return len(increases)

def count_tripple_depth_increases(dp):
    length = len(dp)
    zipped = list(zip(dp[0:length-2], dp[1:length-1], dp[2:length]))
    slidingSumms = list(map(lambda t: t[0] + t[1] + t[2], zipped))
    return count_depth_increases(slidingSumms)