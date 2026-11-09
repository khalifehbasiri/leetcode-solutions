class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        
        all_entries = {}
        alert = []

        i = 0
        for i in range(len(keyName)):
            name = keyName[i]

            timeStr = keyTime[i]
            hours, minutes = map(int, timeStr.split(":"))
            time = (hours * 60) + minutes

            if name not in all_entries:
                all_entries[name] = []
            all_entries[name].append(time)

        for name in all_entries:
            i = len(all_entries[name])
            times = sorted(all_entries[name])

            while i >= 3:
                if (times[i - 1] - times[i - 3]) <= 60:
                    alert.append(name)
                    i -= len(all_entries[name])
                i -= 1
            
        alert.sort()
        return alert
                





                


        return []

