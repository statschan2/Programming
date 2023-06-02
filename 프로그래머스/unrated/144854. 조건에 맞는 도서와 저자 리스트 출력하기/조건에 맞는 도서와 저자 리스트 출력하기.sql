-- 코드를 입력하세요
SELECT a.book_id as BOOK_ID, b.author_name as AUTHOR_ID, date_format(a.published_date,'%Y-%m-%d') as PUBLISHED_DATE
from book a
    join author b on a.author_id = b.author_id
where a.category = '경제'
order by 3
