# !/usr/bin/env python3
#
# Nested Boxes
# Author: Cameron MacDonald

class Box:
	def __init__(self, l, w, h, nests):
		self.l = l
		self.w = w
		self.h = h
		self.nests = nests
		self.found = -1

	def __lt__(self, other):
		return (self.l < other.l and self.w < other.w and self.h < other.h)

def dfs(b):
	b.found = 0
	for j in range(len(b.nests)):
		if b.nests[j].found == -1:
			dfs(b.nests[j])
		b.found = max(b.found, 1 + b.nests[j].found)
	return b.found

def main():
	caseNum = 1
	while True:		
		N = int(input())

		if (N == -1):
			return

		BoxList = []
		i = 0

		while i < N:
			boxes = [int(j) for j in input().split()]
			boxes.sort()
			BoxList.append(Box(boxes[0], boxes[1], boxes[2], []))
			i+=1

		for i in range(len(BoxList)):
			for j in range(len(BoxList)):
				if BoxList[i] < BoxList[j]:
					BoxList[i].nests.append(BoxList[j])

		for i in range(len(BoxList)):
			if BoxList[i].found == -1:
				longestPath = dfs(BoxList[i])

		print("Case " + str(caseNum) + ": " + str(longestPath + 1) + " boxes")

		caseNum+=1

if __name__ == "__main__":
	main()