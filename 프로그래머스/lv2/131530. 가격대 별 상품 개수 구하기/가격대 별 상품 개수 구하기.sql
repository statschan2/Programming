-- 코드를 입력하세요
SELECT price div 10000 * 10000 as PRODUCT_ID, count(*)
from product
group by 1
order by 1