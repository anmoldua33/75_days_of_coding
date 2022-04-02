def numPairsDivisibleBy60(self, time: List[int]) -> int:
	two_sum = [0] * 60
	n = 0
	for t in time:
		n += two_sum[(-1) * (t % 60)]
		two_sum[t % 60] += 1
	return n
