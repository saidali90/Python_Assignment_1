 
class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        self._normalize()
        
    def _normalize(self):
            """دالة تحول الثواني والدقايق اذا زادو عن 60."""
       
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60

            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
            
    def _total_seconds(self):
            return self.hours * 3600 + self.minutes * 60 + self.seconds 
        
    def __add__(self, other):
            if not isinstance(other, Time):
                return NotImplemented
            return Time(
                self.hours + other.hours,
                self.minutes + other.minutes,
                self.seconds + other.seconds,
            )
        
    
    def __iadd__(self, seconds=1):
        if isinstance(seconds, int):
            self.seconds += seconds
        elif isinstance(seconds, Time):
            self.hours += seconds.hours
            self.minutes += seconds.minutes
            self.seconds += seconds.seconds
        else:
            return NotImplemented

        self._normalize()
        return self 
    
    
    def inc(self, seconds=1):
        self.seconds += seconds
        self._normalize()
        return self
    
    def __gt__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return self._total_seconds() > other._total_seconds()
    
    def printTime(self):
        print(f"Time = [{self.hours}:{self.minutes}:{self.seconds}]")

        
t1=Time(1,50,60)
t2=Time(2,20,10)
t3=t1+t2
t3.printTime()

ti1=Time(1,50,60)
ti1+=1
ti1.printTime()

ti2=Time(1,50,60)
ti2.inc()
ti2.printTime()

print(t1>t2)