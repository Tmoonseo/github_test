province_str= 'Gangwon Gyeonggi Gyeongnam Gyeongbuk Gwangju Daegu Daejeon Busan Seoul Ulsan Incheon Jeonnam Jeonbuk Jeju Chungnam Chungbuk'
provinces = [province for province in province_str.split(' ')]
print(provinces)
print(len(provinces), len(['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '울산', '인천',
 '전남', '전북', '제주', '충남', '충북']))


character_str = 'ga geo go gu na neo no nu da deo do du la leo lo lu li ma meo mo mu ba beo bo bu bae sa seo so su a eo o u i yug ja jeo jo ju ji heo ha ho'
characters = [character for character in character_str.split(' ')]
print(characters)
print(len(characters), len('가거고구나너노누다더도두라러로루리마머모무바버보부배사서소수아어오우이육자저조주지허하호'))


def gittest():
 print('git test 중입니다')

def gittest2():
 print('git test 중입니다')

def gittest3():
 print('git test 중입니다')