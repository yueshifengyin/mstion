import os, io, sys, re, time, datetime, base64

__all__ = ['LunarDate']


solar_year          = 2012
solar_month         = 1
solar_day           = 31
solar_weekday          = 0

lunar_year          = 0
lunar_month         = 0
lunar_day           = 0
lunar_isLeapMonth   = False


class LunarDate(object):
    _startDate = datetime.date(2012, 1, 31)

    def __init__(self, year, month, day, isLeapMonth=False):
        global lunar_year
        global lunar_month
        global lunar_day
        global lunar_isLeapMonth

        lunar_year          = int(year)
        lunar_month         = int(month)
        lunar_day           = int(day)
        lunar_isLeapMonth   = bool(isLeapMonth)

        self.year = year
        self.month = month
        self.day = day
        self.isLeapMonth = bool(isLeapMonth)

    def __str__(self):
        return 'LunarDate(%d, %d, %d, %d)' % (self.year, self.month, self.day, self.isLeapMonth)

    __repr__ = __str__

    @staticmethod
    def fromSolarDate(year, month, day):
        solarDate = datetime.date(year, month, day)
        offset = (solarDate - LunarDate._startDate).days
        return LunarDate._fromOffset(offset)

    def toSolarDate(self):
        def _calcDays(yearInfo, month, day, isLeapMonth):
            isLeapMonth = int(isLeapMonth)
            res = 0
            ok = False
            for _month, _days, _isLeapMonth in self._enumMonth(yearInfo):
                if (_month, _isLeapMonth) == (month, isLeapMonth):
                    if 1 <= day <= _days:
                        res += day - 1
                        return res
                    else:
                        raise ValueError("day out of range")
                res += _days

            raise ValueError("month out of range")

        offset = 0
        if self.year < 2018 or self.year >= 2020:
            raise ValueError('year out of range [2018, 2020)')
        yearIdx = self.year - 2012
        for i in range(yearIdx):
            offset += yearDays[i]

        offset += _calcDays(yearInfos[yearIdx], self.month, self.day, self.isLeapMonth)
        return self._startDate + datetime.timedelta(days=offset)

    def __sub__(self, other):
        if isinstance(other, LunarDate):
            return self.toSolarDate() - other.toSolarDate()
        elif isinstance(other, datetime.date):
            return self.toSolarDate() - other
        elif isinstance(other, datetime.timedelta):
            res = self.toSolarDate() - other
            return LunarDate.fromSolarDate(res.year, res.month, res.day)
        raise TypeError

    def __rsub__(self, other):
        if isinstance(other, datetime.date):
            return other - self.toSolarDate()

    def __add__(self, other):
        if isinstance(other, datetime.timedelta):
            res = self.toSolarDate() + other
            return LunarDate.fromSolarDate(res.year, res.month, res.day)
        raise TypeError

    def __radd__(self, other):
        return self + other

    def __lt__(self, other):
        return self - other < datetime.timedelta(0)

    def __le__(self, other):
        return self - other <= datetime.timedelta(0)

    @classmethod
    def today(cls):
        res = datetime.date.today()
        return cls.fromSolarDate(res.year, res.month, res.day)

    @staticmethod
    def _enumMonth(yearInfo):
        months = [(i, 0) for i in range(1, 13)]
        leapMonth = yearInfo % 16
        if leapMonth == 0:
            pass
        elif leapMonth <= 12:
            months.insert(leapMonth, (leapMonth, 1))
        else:
            raise ValueError("yearInfo %r mod 16 should in [0, 12]" % yearInfo)

        for month, isLeapMonth in months:
            if isLeapMonth:
                days = (yearInfo >> 16) % 2 + 29
            else:
                days = (yearInfo >> (16 - month)) % 2 + 29
            yield month, days, isLeapMonth

    @classmethod
    def _fromOffset(cls, offset):
        def _calcMonthDay(yearInfo, offset):
            for month, days, isLeapMonth in cls._enumMonth(yearInfo):
                if offset < days:
                    break
                offset -= days
            return (month, offset + 1, isLeapMonth)

        offset = int(offset)

        for idx, yearDay in enumerate(Info.yearDays()):
            if offset < yearDay:
                break
            offset -= yearDay
        year = 2012 + idx

        yearInfo = Info.yearInfos[idx]
        month, day, isLeapMonth = _calcMonthDay(yearInfo, offset)
        return LunarDate(year, month, day, isLeapMonth)

class ChineseWord():
    def weekday_str(tm):
        a = '日 一 二 三 四 五 六'.split()
        return a[tm]


class Info():
    yearInfos = [

        0x0a5b0, 0x15176, 0x052b0, 0x0a930, 0x07954,#   /* 2020 */
        0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6,#   /* 2025 */

        ]

    def yearInfo2yearDay(yearInfo):
        yearInfo = int(yearInfo)

        res = 29 * 12

        leap = False
        if yearInfo % 16 != 0:
            leap = True
            res += 29

        yearInfo //= 16

        for i in range(12 + leap):
            if yearInfo % 2 == 1:
                res += 1
            yearInfo //= 2
        return res

    def yearDays():
        yearDays = [Info.yearInfo2yearDay(x) for x in Info.yearInfos]
        return yearDays

    def day2LunarDate(offset):
        offset = int(offset)
        res = LunarDate()

        for idx, yearDay in enumerate(yearDays()):
            if offset < yearDay:
                break
            offset -= yearDay
        res.year = 1900 + idx

class SolarDate():

    def __init__(self):
        global solar_year
        global solar_month
        global solar_day
        global solar_weekday

        solar_year      = int(time.strftime("%Y", time.localtime()))
        solar_month     = int(time.strftime("%m", time.localtime()))
        solar_day       = int(time.strftime("%d", time.localtime()))
        solar_weekday   = int(time.strftime("%w", time.localtime()))

        self.year = solar_year
        self.month = solar_month
        self.day = solar_day
        self.weekday = solar_weekday

    def __str__(self):
        return 'LunarDate(%d, %d, %d, %d)' % (self.year, self.month, self.day, self.isLeapMonth)


def getCalendar_today():
    solar = SolarDate()
    LunarDate.fromSolarDate(solar_year, solar_month, solar_day)

    twitter =[solar_year, solar_month, solar_day, ChineseWord.weekday_str(solar_weekday)]
    print(twitter)
    return twitter

def getCalendar_all_day():
    # solar = SolarDate()
    global solar_year
    global solar_month
    global solar_day
    global solar_weekday

    solar_year = 2012
    solar_month = 1
    weekday_offset = 0 #1月1号星期几?
    index_day = 0
    for solar_month in range(1, 13):
        if solar_month in [1, 3, 5, 7, 8, 10, 12]:
            solar_day_max = 31
        elif solar_month in [4, 6, 9, 11]:
            solar_day_max = 30
        elif solar_month == 2:
            if ((solar_year % 4 == 0) and (solar_year % 100 != 0)) or (solar_year % 400 == 0 ):
                solar_day_max = 29
            else:
                solar_day_max = 28
        else:
            None

        for solar_day in range(1, solar_day_max + 1):
            index_day += 1
            solar_weekday = (index_day )% 7 +  - 1
            solar_weekday = 0 if solar_weekday == 7 else solar_weekday
            solar_weekday = 6 if solar_weekday == -1 else solar_weekday

            LunarDate.fromSolarDate(solar_year, solar_month, solar_day)

            index_yy = str(solar_year)
            if int(solar_month) < 10:
                index_mm = "0" + str(solar_month)
            else:
                index_mm = str(solar_month)
            if int(solar_day) < 10:
                index_dd = "0" + str(solar_day)
            else:
                index_dd = str(solar_day)

            index_yyddmm = index_yy + index_mm + index_dd

            twitter = [solar_year, solar_month, solar_day, ChineseWord.weekday_str(solar_weekday)]
            print(twitter)
    return twitter


def main():
    "main function"
    
    getCalendar_all_day()
    getCalendar_today()

if __name__ == '__main__':
    main()
    

# print(base64.b64decode(b'Q29weXJpZ2h0IChjKSAyMDEyIERvdWN1YmUgSW5jLiBBbGwgcmlnaHRzIHJlc2VydmVkLg==').decode())