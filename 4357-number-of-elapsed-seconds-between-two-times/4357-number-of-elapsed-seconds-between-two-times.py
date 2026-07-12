class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        a=[int(x) for x in startTime.split(':')]
        b=[int(x) for x in endTime.split(':')]

        return (b[0]*3600+b[1]*60+b[2])-(a[0]*3600+a[1]*60+a[2])